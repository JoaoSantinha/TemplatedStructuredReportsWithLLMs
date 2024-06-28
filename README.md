# Templated radiological reporting system using AI-based Speech-to-text + LLM-based structuring using streamlit  

This is a Python program that uses local speech-to-text AI model to transcribe a dictated report and then scrub to remove PHI before passing the transcribed the unstructured report to OpenAI's GPT-3.5 to create the structured report using user-specified templates. The user-interface is provided through streamlit

## Requirements

- Python
- OpenAI API key
- numpy
- streamlit
- openai
- SpeechRecognition
- whisper
- Pyaudio
- scrubadubdub

## Usage

1. Run the program with `streamlit run main.py`.
2. Press the "Record" button and speak to start transcription.
3. Press the "Stop" button to stop recording, start transcription and create the templated structured report using the LLM.
