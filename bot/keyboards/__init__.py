# from .keyboard import choose_replay as Choose_main_menu_replay, back_menu_replay as Back_to_main_menu_replay
from .keyboard import choose_main_inline as Choose_main_menu_inline, \
    back_menu_inline as Back_to_main_menu_inline, \
    back_to_choose_tests as Back_to_choose_tests, \
    my_results_inline as My_results_test, \
    start_test_inline_and_backm as Start_test_and_b, \
    next_question as Next_question


__all__ = [
    "Choose_main_menu_replay",
    "Back_to_main_menu_replay",
    "Choose_main_menu_inline",
    "Back_to_main_menu_inline",
    "Back_to_choose_tests",
    "My_results_test",
    "Start_test",
    "Next_question",
    "Start_test_and_b"
]