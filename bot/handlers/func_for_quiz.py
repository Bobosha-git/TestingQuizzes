import random
import json

from pathlib import Path
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 


#открытие файла
def load_tests():
    tests_path = Path(r"C:\Users\Bobosha\Desktop\GitProj\TestingQuizzes\bot\texts\tests\test_quiz.json")
    with tests_path.open("r", encoding = "UTF-8") as file:
        return json.load(file)

#перемешка вопросоув и ответоув
def shuffle_ques_options(correct_file):
    random.shuffle(correct_file["questions"])
    for question in correct_file["questions"]:
        random.shuffle(question["options"])

# Генерация кнопок с названием тестов
def generate_test_buttons(tests):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    button = InlineKeyboardButton(
        text=tests["name"],  
        callback_data=f"test_{tests["name"]}"  
    )
    keyboard.inline_keyboard.append([button])  
    return keyboard

# Генерация ответов к вопросу
def generate_answ_butt_i(options, question_index):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[], row_width=2)
    
    for q, option in enumerate((options), start=1):
        callback_data = f"ans_{q}"
        button = InlineKeyboardButton(text = f"{q}. {option["text"]}", callback_data=callback_data)
        keyboard.inline_keyboard.append([button])

    return keyboard

#
def check_answer(questions, index, selected_option_index):
    question = questions[index]
    selected_option = question["options"][selected_option_index]
    return selected_option.get("points", {}).get("score", 0)

#
def check_results(score, results_in_json):
    for variant in results_in_json:
        min_score, max_score = variant["points"]
        if min_score <= score <= max_score:
            return variant["text"]
