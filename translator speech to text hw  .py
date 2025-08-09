import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Text-to-Speech Function
def func1(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    voices = engine.getProperty("voices")
    for idx, voice in enumerate(voices):
        print(f"Voice {idx}: {voice.name} - {voice.id}")

    # Select voice (adjust index as per your OS if needed)
    if language == "en":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)  # Try changing index if silent

    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Function
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError as e:
        print(f"Could not understand audio: {e}")
    except sr.RequestError as r:
        print(f"Speech Recognition API error: {r}")
    return ""

# Translation Function
def translate_1(text, target_language="es"):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        print(f"Translated text: {translation.text}")
        return translation.text
    except Exception as e:
        print(f"Error during translation: {e}")
    return ""

# Language Menu Function
def print_menu():
    print("\nChoose a language to translate to:")
    print("1. Hindi")
    print("2. Gujarati")
    print("3. Telugu")
    print("4. French")
    print("5. Punjabi")
    print("6. Malayalam")
    print("7. Bengali")

    choice = input("Enter your choice (1-7): ")
    dict1 = {
        "1": "hi",
        "2": "gu",
        "3": "te",
        "4": "fr",
        "5": "pa",
        "6": "ml",
        "7": "bn"
    }
    return dict1.get(choice, "es")  # default to Spanish

# Main Program Flow
def main():
    target_language = print_menu()

    original_text = speech_to_text()


    if original_text:
        translated_text = translate_1(original_text, target_language)

        if translated_text:
            func1(translated_text, language="en")
            print("Translation spoken out successfully!")
        else:
            print("Translation failed or was empty.")
    else:
        print("No speech detected or recognized.")

# Run the program
main()
