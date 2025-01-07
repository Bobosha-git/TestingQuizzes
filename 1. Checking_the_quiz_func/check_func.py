import json

def check_quiz():
    path_to_file = r"C:\Users\Bobosha\Desktop\GitProj\TestingQuizzes\2. Files with Quiz\test_quiz.json"
    with open(path_to_file, "r", encoding='utf-8') as test:
        example = json.load(test)
        correct = json.dumps(example, ensure_ascii=False, indent=2)
        return correct
        

print(check_quiz())

