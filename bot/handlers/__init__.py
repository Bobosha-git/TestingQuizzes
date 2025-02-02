from .handler import router as CommandRouter
from .func_for_quiz import load_tests as Load_test,\
                        shuffle_ques_options as Shuf_ques_opt,\
                        check_answer as Check_ans,\
                        generate_test_buttons as Generate_test_butt

__all__ = [
    "CommandRouter",
    "Load_test",
    "Shuf_ques_opt",
    "Check_ans",
    "Generate_test_butt"
]