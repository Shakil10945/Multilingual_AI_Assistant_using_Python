import speech_recognition as sr
import google.generativeai as genai
import os
from gtts import gTTS
import logging

# Configure logging to save to a file
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

class AIAssistant:
    def __init__(self, google_api_key):
        self.google_api_key = google_api_key
        os.environ['GOOGLE_API_KEY'] = google_api_key
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def voice_input(self):
        logging.info("Initializing voice recognition...")
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            logging.info("Listening for voice input...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            logging.info(f"Voice input recognized: {text}")
            return text
        except sr.UnknownValueError:
            logging.error("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            logging.error(f"Could not request results from Google Speech Recognition Service; {e}")
            return None

    def text_to_speech(self, text):
        logging.info(f"Converting text to speech: {text}")
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        logging.info("Text-to-speech conversion completed and saved as speech.mp3")

    def generate_response(self, user_text):
        logging.info(f"Generating response for user text: {user_text}")
        response = self.model.generate_content(user_text)
        result = response.text
        logging.info(f"Generated response: {result}")
        return result