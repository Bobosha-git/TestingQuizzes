from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

### REPLAY BUTTON

# choose_replay = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Выбрать тест")],
#     [KeyboardButton(text="О проекте")], [KeyboardButton(text="Поддержка")]
# ],
#     resize_keyboard=True)

# back_menu_replay = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Назад в главное меню")]
# ],
#     resize_keyboard=True)

#########################################

# INLINE BUTTON

#Кнопки отвечающие за главное меню
choose_main_inline = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "Перейти к тестам", callback_data = "for_tests")],
    [InlineKeyboardButton(text = "О проекте", callback_data = "about_proj")], [InlineKeyboardButton(text="Поддержка", callback_data="helps")]
])

#Кнопка отвечающая за возврат в меню
back_menu_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Назад", callback_data="back_main_menu")]
])

#Кнопка отвечающая за возврат к выбору тестов из теста
back_to_choose_tests = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Назад к выбору тестов", callback_data="back_to_choose_tests")]
])

#Кнопка показывающая последние 3 результата по тесту
my_results_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Мои результаты", callback_data="my_results_test")]
])

#Кнопка для начала теста
start_test_inline_and_backm = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Начать тест", callback_data="start_test_inline")],
    [InlineKeyboardButton(text = "Назад к выбору тестов", callback_data="back_to_choose_tests")]
])

#Кнопка для перехода к следующему вопросу
next_question = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = "Следующий вопрос", callback_data="next_question")]
])

# #Тестовая кнопка 
# test_button = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="Next", callback_data="next")]
# ])