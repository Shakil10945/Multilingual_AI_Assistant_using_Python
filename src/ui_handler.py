import streamlit as st
from src.ai_assistant import AIAssistant

class UIHandler:
    def __init__(self, assistant):
        self.assistant = assistant

    def display_ui(self):
        st.title("Multilingual AI Assistant")

        # Create a tab for voice input and a tab for text input
        tabs = st.tabs(["Voice Input", "Text Input"])

        # Voice Input tab
        with tabs[0]:
            if st.button("Ask me anything by voice!"):
                with st.spinner("Listening..."):
                    text = self.assistant.voice_input()
                    if text:
                        response = self.assistant.generate_response(text)
                        self.assistant.text_to_speech(response)

                        # Display response and audio
                        audio_file = open("speech.mp3", 'rb')
                        audio_bytes = audio_file.read()

                        st.text_area(label="Response:", value=response, height=350)
                        st.audio(audio_bytes, format='audio/mp3')
                        st.download_button(label="Download Speech", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3")

        # Text Input tab
        with tabs[1]:
            user_input = st.text_input("Type your query here")
            if st.button("Submit"):
                response = self.assistant.generate_response(user_input)
                self.assistant.text_to_speech(response)

                # Display response and audio
                audio_file = open("speech.mp3", 'rb')
                audio_bytes = audio_file.read()

                st.text_area(label="Response:", value=response, height=350)
                st.audio(audio_bytes, format='audio/mp3')
                st.download_button(label="Download Speech", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3")