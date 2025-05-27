from transformers import BlipProcessor , BlipForConditionalGeneration , pipeline
import os
from PIL import Image
from colorama import Fore , init , Style
import torch


init(autoreset=True)

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"device set to {device}")

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


#text genrator 

text_generator = pipeline(
    "text-generation",
    model = "gpt2",
    tokenizer = "gpt2",
    device = 0 if device=="cuda" else -1,
    return_full_text =  True
)

def generate_caption(image_path):
  image = Image.open(image_path).convert("RGB")
  inputs = processor(images = image , return_tensors = "pt").to(device)
  output = caption_model.generate(**inputs , max_new_tokens = 50)
  caption = processor.decode(output[0], skip_special_tokens = True)
  return caption


def text_generation(prompt,max_new_tokens):
    result = text_generator(
        prompt,
        max_length = max_new_tokens,
        num_return_sequence = 1,
        truncation = True
    )
    if isinstance(result , list):
        if "generated_text" in result[0]:
            return result[0]["generated_text"]
        elif "text" in result[0]:
            return result[0]["text"]
    else:
       return "text generation failed"
    

def truncate(text,word_limit):
    words = text.strip().split()
    return " ".join(words[:word_limit])

def print_menu():
    print("SELECT YOUR CHOICE (1-4)")
    print("1.caption(5 words)")
    print("2.description(30 words)")
    print("3.summary(50 words)")
    print("4.exit")


def main():
    image_path1 = input("enter image path")
    if not os.path.exists(image_path1):
        print("the path doent exist")
        return 1
    try:
        caption = generate_caption(image_path1)
        print(f"the generated caption is {caption}")
    except Exception as e :
        print(e)

    while True:
        print_menu()
        choice = input("enter your choice (1-4)")

        if choice == "1":
            short_caption = truncate(caption,5)
            print(short_caption)
        elif choice == "2":
            prompt = f"expand the caption to 30 words {caption}"
            try:
              description = text_generation(prompt,max_new_tokens=60)
              description = truncate(description,30)
              print(description)
            except Exception as e:
                print(e)
        elif choice == "3":
            prompt = f"expand the caption to 50 words {caption}"
            try:
             summary = text_generation(prompt , max_new_tokens = 80)
             summary = truncate(summary , 50)
             print(f"the summary of 50 wrods is {summary}")
            except Exception as e:
              print(f"there was an error {e}")
        elif choice == "4":
            print("BYE!")
            break
        else:
            print('please enter a valid input')



main()
 