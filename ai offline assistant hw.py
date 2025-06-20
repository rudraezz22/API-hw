import pyttsx3
import datetime

engine = pyttsx3.init()

def process_query(query):
    query = query.lower()
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"the current time is {now}"
    elif "date" in query:
        date = datetime.datetime.now().strftime("%B,%D,%Y")
        return f"today's date it {date}"
    else:
        return "sorry could not understand that command"
    

def main():
    print("assistant is running enter u choice time,date,exit")

    while True:
        choice = input("you: ")
        if choice == "exit":
            print("assistant stopped!")
            break
        response = process_query(choice)
        print(f"the response is {response}")
        engine.say(response)
        engine.runAndWait()

main()