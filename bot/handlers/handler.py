import asyncio

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards import Choose_main_menu_inline, Back_to_main_menu_inline, Back_to_choose_tests, Start_test_and_b
from texts import About_us, Support
from db import Add_in_base, Add_solved_test, Clear_answers, Add_user_answers, Count_p_one
from .func_for_quiz import load_tests, generate_test_buttons, shuffle_ques_options, generate_answ_butt_i, check_answer, check_results


router = Router()

class QuizQuestion(StatesGroup):
    question = State()


#Запуск бота
@router.message (CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\n\nЯ — твой бот для квизов и тестов! Готов провести тебе увлекательные викторины, помочь прокачать знания или просто весело провести время.")
    id_tg = message.from_user.id
    us_name = message.from_user.username
    Add_in_base(id_tg=id_tg, user_name=us_name)
    await asyncio.sleep(5)
    await message.answer(
        "<b>Что умеет этот бот?</b>\n\n"
        "<b>• Викторины:</b> Попробуй свои силы в разных темах — от истории до поп-культуры.\n"
        "<b>• Тесты:</b> Проверь свои знания или просто узнай что-то новое.\n\n"
        "Участвуй сам или вызывай друзей на дуэль знаний.\n\n"
        "Готов? Тогда вперёд!",
        parse_mode="HTML"
    )
    await asyncio.sleep(3)
    await message.answer("Теперь выбери нужный тебе пункт меню:", reply_markup=Choose_main_menu_inline)

#Выбор возможного теста
@router.callback_query(lambda c: c.data == "for_tests")
async def choose_test(callback: CallbackQuery):
    tests = load_tests()
    keyboard = generate_test_buttons(tests)
    keyboard.inline_keyboard.append(Back_to_main_menu_inline.inline_keyboard[0])
    await callback.message.edit_text("Возможные тесты", reply_markup=keyboard)

#Обработка выбранного теста
@router.callback_query(lambda c: c.data.startswith("test_"))
async def handle_test_selection(callback: CallbackQuery):
    test_name = callback.data[5:]
    tests = load_tests() 

    if test_name == tests['name']:
        description = tests.get("description", "Описание отсутствует.")
        # Back_to_choose_tests.inline_keyboard.append(Start_test.inline_keyboard[0])
        await callback.message.edit_text(
            f"Вы выбрали тест: <b>{test_name}</b>\n\nОписание: {description}",parse_mode="HTML", reply_markup=Start_test_and_b
        )
    else:
        await callback.message.edit_text("Выбранный тест не найден.", reply_markup=Back_to_choose_tests)

#Пользователь выбрал "О проекте"
@router.callback_query(lambda c: c.data == "about_proj")
async def choose_about(callback: CallbackQuery):
    await callback.message.edit_text(About_us, parse_mode="HTML", reply_markup=Back_to_main_menu_inline)

#Пользователь выбрал "Помощь"
@router.callback_query(lambda c: c.data == "helps")
async def choose_help(callback: CallbackQuery):
    await callback.message.edit_text(Support, parse_mode="HTML", reply_markup=Back_to_main_menu_inline)

#Пользователь выбрал вернуться в главное меню выбора
@router.callback_query(lambda c: c.data == "back_main_menu")
async def choose_back_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text("Вы вернулись в главное меню", reply_markup=Choose_main_menu_inline)

#Пользователь выбрал вернуться обратно к выбору теста
@router.callback_query(lambda c: c.data == "back_to_choose_tests")
async def back_to_choose_tests(callback: CallbackQuery):
    await choose_test(callback)

#Запуск выбранного теста
@router.callback_query(lambda c: c.data == "start_test_inline")
async def start_test(callback: CallbackQuery, state: FSMContext):
    id_tg = callback.from_user.id
    Clear_answers(id_tg=id_tg)

    questions = load_tests()
    shuffle_ques_options(questions)

    await state.update_data(questions = questions["questions"], index = 0)
    
    question = questions["questions"][0]
    keyboard = generate_answ_butt_i(question["options"], 0)

    await callback.message.edit_text(question["question"], reply_markup=keyboard)
    await state.set_state(QuizQuestion.question)

#Переключение на следующий вопрос
@router.callback_query(lambda c: c.data.startswith("ans_"))
async def next_question(callback: CallbackQuery, state: FSMContext):
    questions_js = load_tests()

    data = await state.get_data()
    questions = data["questions"]
    index = data["index"]
    score = data.get("score", 0)

    selected_option_index = int(callback.data.split("_")[1]) - 1
    selected_option_index_for_db = int(callback.data.split("_")[1])

    score += check_answer(questions, index, selected_option_index)
    await state.update_data(score=score)
    
    id_tg = callback.from_user.id
    Add_user_answers(id_tg=id_tg, user_answer=selected_option_index_for_db)

    if index + 1 < len(questions):
        index += 1
        await state.update_data(index = index)
        question = questions[index]
        keyboard = generate_answ_butt_i(question["options"], index + 1)

        await callback.message.edit_text(question["question"], reply_markup=keyboard)
    else:
        results_text = check_results(score, questions_js["results"])
        await callback.message.edit_text(f"Тест завершен. Ваш итоговый счет: {score}\n\n{results_text}", reply_markup=Back_to_choose_tests)

        id_tg = callback.from_user.id
        name_test = questions_js["name"]
        Add_solved_test(solved_test=name_test, id_tg=id_tg)
        Count_p_one(id_tg=id_tg)

        await state.clear()




############## TESTS

# #Кнопка "Слудующий вопрос"
# @router.callback_query(lambda c: c.data == "next_question")
# async def text_but_next(callback: CallbackQuery):
#     await callback.message.edit_text()

# #
# @router.callback_query(lambda c: c.data == "start_test_inline")
# async def start_test(callback: CallbackQuery):
#     questions = load_tests()
#     shuffle_ques_options(questions)

#     for question in questions["questions"]:
#         await callback.message.edit_text(question["question"], reply_markup=Next_question)