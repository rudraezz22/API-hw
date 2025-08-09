import requests

api_key = "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"

model_url =  "nlpconnect/vit-gpt2-image-captioning"
api_url =  f"https://api-inference.huggingface.co/models/{model_url}"

headers = {"Authorization":f"Bearer {api_key}"}

def caption_img():
    img1 = "test.png"
    try:
        with open(img1 , "rb") as var:
            reading = var.read()
    except Exception as e :
        print(f"an error occureed{e}")
        return
    response = requests.post(api_url , headers = headers , data = reading)
    result = response.json()
    
    if isinstance(result , dict) and "error" in result:
        print(result["error"])
        return
    caption = result[0].get("generated_text" , "No text generated")
    print("image", img1)
    print(caption)



caption_img()
