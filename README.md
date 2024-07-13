## Features

- **Voice Input**: The assistant can listen to voice inputs, recognize the speech, and generate a response.
- **Text Input**: Users can also type their queries directly and get responses.
- **Text-to-Speech**: The responses are converted to speech and can be downloaded as an MP3 file.
- **Logging**: The application logs important events and errors for easier debugging and maintenance.

## Project Structure
project/
│
├── src/
│   ├── __init__.py
│   ├── ai_assistant.py
│   └── ui_handler.py
│
├── app.py
└── app.log

- `src/ai_assistant.py`: Contains the `AIAssistant` class that handles voice input, text-to-speech conversion, and response generation.
- `src/ui_handler.py`: Contains the `UIHandler` class that manages the Streamlit UI.
- `app.py`: The main entry point for the Streamlit app.
- `app.log`: The log file where all the logging information is saved.

## Setup and Installation

1. **Clone the repository**:
bash
    git clone https://github.com/yourusername/multilingual-ai-assistant.git
    cd multilingual-ai-assistant
   
2. **Create and activate a virtual environment**:

   bash
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
   
3. **Install the required dependencies**:

   bash
    pip install -r requirements.txt
   
4. **Set up the Google API key**:

    Replace `***************************` in `app.py` with your actual Google API key.

5. **Run the application**:

   bash
    streamlit run app.py
   
## Usage

- **Voice Input**: Click on the "Ask me anything by voice!" button, speak into your microphone, and wait for the response.
- **Text Input**: Type your query in the text input box and click the "Submit" button to get a response.

## Requirements

- Python 3.7 or higher
- Streamlit
- SpeechRecognition
- google-generativeai
- gTTS

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- This project uses the Google Cloud Speech-to-Text and Text-to-Speech APIs.
- Streamlit for the easy-to-use web application framework.
### requirements.txt

Ensure you also have a requirements.txt file for easy dependency installation:
plaintext
streamlit
SpeechRecognition
google-generativeai
gTTS