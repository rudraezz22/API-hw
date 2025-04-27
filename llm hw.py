import requests 
from colorama import Fore , Style , init

init(autoreset=True)

api_key = "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"

default_model = "facebook/bart-large-cnn"

def build_url(model_name):
    return f"https://api-inference.huggingface.co/models/{model_name}"
   
def query(payload, model_name = default_model):
    api_url = build_url(model_name)
    headers = {"Authorization":f"Bearer {api_key}"}
    response = requests.post(api_url, headers=headers, json=payload)


    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("failed to genrate a reponse from api")
            print(f"{response.text}")
            return None
    else:
        print(f"api call failed with status {response.status_code}")
        print(f"response content {response.text}")
        return None
    

def summary_text(text , minlength , maxlength , model = default_model):
    payload = {
        "inputs":text,
        "parameters": {
            "min_length": minlength,
            "max_length": maxlength
        }

    }
    print(f"performing ai summarization with model {model}")

    result = query(payload , model_name=model)
    if isinstance(result,list) and result and "summary_text" in result[0]:
        return result[0]["summary_text"]
    else:
        print("error in summarization")
        print(result)
        return None
    
if __name__ == "__main__" :
    print("Hello! welcome to summary bot")
    user_name = input("enter a username").strip()
    if not user_name:
        user_name = "user"
    print(f"welcome {user_name} give text and see magic")
    user_text = input().strip()
    if not user_text:
        print("no text provided please provide a text")

    else:
        print("enter the model u want to choose")
        model_choice = input("enter your choice").strip()
        if not model_choice:
            model_choice = default_model
        print("choose a summarization style")
        print("1 for short and consize , 2 for detailed and prefined explanation")
        style_choice = input("enter you style choice from 1 or 2 ").strip()
        
        if style_choice == "1":
            min_length = 80
            max_length = 240
            print("quick and consize explanantion")
        else:
            min_length = 250
            max_length = 500
            print("detailed and prefined explanation")

        summary = summary_text(user_text , min_length , max_length , model= model_choice)
        if summary :
            print(f"your AI generated summary is {summary}")
        else:
            print("no summary was able to generate")



        





