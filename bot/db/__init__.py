from .func_with_db import db_table_val as Add_in_base,\
                        db_add_solved_test as Add_solved_test,\
                        db_add_user_answer as Add_user_answers, \
                        clear_user_answers as Clear_answers, \
                        increment_test_count as Count_p_one

__all__ = [
    "Add_in_base",
    "Add_solved_test",
    "Add_user_answers",
    "Clear_answers",
    "Count_p_one"
]