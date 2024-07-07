import streamlit as st
from src.helper import voice_input, text_to_speech, llm_model_object

def main():
    st.title("Multilingual AI Assistant")

    #craeate a tab for voice input and a tab for text input

    tabs= st.tabs(["Voice Input", "Text Input"])

    with tabs[0]:

        if st.button("Ask me anything!"):
            with st.spinner("Listenning......"):
                text = voice_input()
                response = llm_model_object(text)
                text_to_speech(response)


                #Display audio player and download link
                audio_file = open("speech.mp3",'rb')
                audio_bytes = audio_file.read()

                st.text_area(label= "Response: ", value = response, height=350)
                st.audio(audio_bytes, format='audion/mp3')
                st.download_button(label="Download Speech", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3")
        
    with tabs[1]:
        user_input = st.text_input("Type your query heare")
        if st.button("Sibmit"):
            response = llm_model_object(user_input)
            text_to_speech(response)

            #Display audio player and download link
            audio_file = open("speech.mp3",'rb')
            audio_bytes = audio_file.read()

            st.text_area(label= "Response: ", value = response, height=350)
            st.audio(audio_bytes, format='audion/mp3')
            st.download_button(label="Download Speech", data=audio_bytes, file_name="speech.mp3", mime="audio/mp3")
        

if __name__=="__main__":
    main()