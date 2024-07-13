import streamlit as st
from src.ai_assistant import AIAssistant
from src.ui_handler import UIHandler
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

def main():
    assistant = AIAssistant(google_api_key="***************************")
    ui_handler = UIHandler(assistant)
    ui_handler.display_ui()

if __name__ == "__main__":
    main()