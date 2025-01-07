import json

with open("Quiz.json", "r") as test:
    quiz = json.load(test)
    print(quiz)