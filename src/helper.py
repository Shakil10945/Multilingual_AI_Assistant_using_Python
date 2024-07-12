import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
import logging

#Configuration logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

GOOGLE_API_KEY = "******************************" #Please enter your gemini api

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

def voice_input():
    logging.info("initializing voice recognition.....")
    #create a recognizer instance
    r = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Listenning for voice inpu...t")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio) #using google speech recognition
        logging.info(f"Voice input recognized: {text}")
        return text
    except sr.UnknownValueError:
        logging.error("Google Speech Recognition could not understand your voice.")
        return None
    except sr.RequestError as e:
        logging.info(f"Could not request results from Google Speech Recognition Service; {e}")
        return None
    

def text_to_speech(text):
    logging.info(f"Converting to specch: {text}")

    #create a gTTS object
    tts = gTTS(text=text, lang= 'en') #language can be changed
    #save the audio as an MP3 file
    tts.save("speech.mp3")

    logging.info("Text-to-speech conversion completed and saved as specch.mp3")

    
def llm_model_object(user_text):
    logging.info(f"Geenrating response for user text: {user_text}")

    genai.configure(api_key = GOOGLE_API_KEY)
    
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(user_text)

    result = response.text

    logging.info(f"Generated response: {result}")

    return result