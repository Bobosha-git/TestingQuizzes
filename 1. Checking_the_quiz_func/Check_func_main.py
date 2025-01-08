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
    for question, answer_index in zip(questions, answers):
        selected_option = question["options"][answer_index]
        if selected_option.get("is_right", False):
            score += selected_option.get("points", {}).get("score",1)
    return score    


def check_results(score, results_in_json):
    for range_str, results_text in results_in_json.items():
        min_score, max_score = map(int, range_str.split("-"))
        if min_score <= score <= max_score:
            return results_text
    return "Все пошло по одному месту"


def check():
    quis_list = open_file_quiz()
    shuffle_ques_options(quis_list)

    print(f"Название квиза: {quis_list["name"]}")
    user_ans = []

    for question in quis_list["questions"]:
        print("\n" + question["question"])
        print("")
        for x, option in enumerate(question["options"], start=1):
            print(f"{x}. {option["text"]}")
        print("")
        answer = int(input("Твой ответ: "))
        user_ans.append(answer - 1)

    score = check_answer(quis_list["questions"], user_ans)
    print(f"\nТы набрал {score} очков")
    results = check_results(score, quis_list["results"])
    print(f"\nТвой результат: {results}\n")


if __name__ == "__main__":
    check()
    
