import json
import random   


def open_file_quiz():
    path_to_file = r"C:\Users\Bobosha\Desktop\GitProj\TestingQuizzes\2. Files with Quiz\test_quiz.json"
    with open(path_to_file, "r", encoding='utf-8') as open_file:
        return json.load(open_file)
    

def shuffle_ques_options(correct_file):
    random.shuffle(correct_file["questions"])
    for question in correct_file["questions"]:
        random.shuffle(question["options"])


def check_answer(questions, answers):
    score = 0
    for question, answer in zip(questions, answers):
        if question["answer"] == answer:
            score += question.get("points", 1)
    return score    


def check():
    quis_list = open_file_quiz()
    shuffle_ques_options(quis_list)

    print(f"Название квиза: {quis_list["name"]}")
    user_ans = []

    for question in quis_list["questions"]:
        print("\n" + question["question"])
        print("")
        for x, option in enumerate(question["options"], start=1):
            print(f"{x}. {option}")
        print("")
        answer = input("Твой ответ: ")
        user_ans.append(question["options"][int(answer) - 1])

    score = check_answer(quis_list["questions"], user_ans)
    print(f"Ты набрал {score} очков")

if __name__ == "__main__":
    check()
    
