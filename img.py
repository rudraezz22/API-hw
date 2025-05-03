import requests
from PIL import Image
from io import BytesIO

api_key = "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" 
api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"

def img_gen(prompt:str) -> Image.Image:
    headers = {"Authorization":f"Bearer {api_key}"}
    payload = {"inputs":prompt}
    try:
        response = requests.post(api_url , headers= headers , json = payload)
        response.raise_for_status()
        if "image" in response.headers.get("Content-Type",''):
            img = Image.open(BytesIO(response.content))
            return img
        else:
            raise Exception("the exception is not an image")
    except requests.exceptions.RequestException as e:
        raise Exception(f"the exception is {e}")
    
def main():
    print("welcome")
    print("type exit to quit")
     
    while True:
        user_input = input("enter the prompt of the image you want to genrate").strip()
        if user_input.lower()  == "exit":
            print("BYE")
            break
        else:
            print("genrating the image")
            try:
                img1 = img_gen(user_input)
                img1.show()
            except Exception as e:
                print(f"an error occurred {e}")



main()



