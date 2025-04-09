import requests
import html
import random

education_id = 9
link1 = f"https://opentdb.com/api.php?amount=10&category={education_id}&type=multiple"

def get_trivia_questions():
    response = requests.get(link1)
    if response.status_code == 200:
        data = response.json()
        if data["response_code"] ==0 and data["results"]:
            return data["results"]
    else:
        return None
    


def get_quizz():
    questions = get_trivia_questions()
    if not questions :
        print ("error")
        return
    score = 0

    print("welcome!")
    for i , q in enumerate(questions , 1):
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        incorrect = [html.unescape(a) for a in q["incorrect_answers"]]
        options = incorrect + [correct]
        random.shuffle(options)

        print("question : " , i , question)
        for idx , option in enumerate(options,1):
            print(idx,option)


        while True:
            try:
                choice = int(input("enter you choice between 1-4 \n"))
                if 1<= choice <=4:
                    break
                else:
                    print("please enter a valid integer between 1-4")
            except ValueError:
                print("please enter value in numbers")

        if options[choice-1] == correct:
            print("correct answer!\n")
            score = score+1
        else :
            print(f"incorrect answer , the correct answer is {correct}\n")

    print(f"your total score is {score}")
    print(f"your total percentage is {(score/len(questions)*100)}")

get_quizz()





