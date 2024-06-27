import streamlit as st
from glob import glob
import openai
import speech_recognition as sr
import time
import openai
import os
from os.path import join, dirname, basename
import importlib
from scrubadubdub import Scrub
#import pandas as pd
#import json
#from datetime import datetime
#import os
#import io
#import zipfile
#import random
#import string
#import whisper

# Whether to redact or not redact PII
PII_REDACT = True

messages = [{"role": "system", 
                  "content": "I am a junior radiologist doing unstructured radiology reports and I need your help to create a structured radiology report. In the impression do not give non-specific descriptions in the impression, but instead tell me what you think about the findings. This is the unstructured report to be structured:"}]

def generate_answer(message_list):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  ##
        messages=message_list,
        max_tokens=1000,
        temperature=0.5
    )
    return [response.choices[0].message.content, response.usage]


def app():
    openai.organization = "YOUR_ORG"
    #openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "YOUR_API_KEY"
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    # Title
    st.title("LLM-assisted Structured Radiological Report")
    global option
    global question
    global has_question 
    has_question = False
    question = ''
    global messages

    # look for available templates and create structure for select box 
    templates_list = glob(join('.','Templates', "*.py"))
    global templates_popupMenuStr_dict
    templates_popupMenuStr_dict = {}
    for template_filepath in templates_list:
        templates_popupMenuStr_dict[basename(template_filepath).replace('.py', '')] = template_filepath
    options_reports = tuple([x.replace('_',' ') for x in templates_popupMenuStr_dict.keys()])

    option = st.selectbox('Select the report template:', options_reports)
    
    st.write("Press button to record and stop to generate report")
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)  # we only need to calibrate once, before we start listening
    
    if st.button("Record :studio_microphone:", key="0"):
        messages = update_report(option)
        
        # start listening in the background (note that we don't have to do this inside a `with` statement)
        global stop_listening
        stop_listening = r.listen_in_background(mic, callback)
        
    if st.button("Stop :studio_microphone:", key="1"):
        # calling this function requests that the background listener stop listening
        stop_listening(wait_for_stop=False)
        
        while not has_question:
            time.sleep(0.1)
        
        st.text_area("You:", question)

        # scrub pii if selected
        if PII_REDACT:
            scrubber = Scrub()
            question_pii_redacted = scrubber.scrub(str(question))
            #messages.append({"role": "user", "content": str(question)})
            messages.append({"role": "user", "content": str(question_pii_redacted)})
        else:
            messages.append({"role": "user", "content": str(question)})
        
        answer = generate_answer(messages)
        st.text_area("Structured Report: ", answer[0])
        messages.append({"role": "assistant", "content": answer[0]})

        
def update_report(option):
    print("option update_report: ", option)
    template_file_2_import = templates_popupMenuStr_dict[option.replace(' ', '_')]
    print(template_file_2_import)
    template = importlib.import_module(template_file_2_import.replace('/','.')[2:-3]).TEMPLATE
    print(template)
    return [{"role": "system",
             "content": template}]


# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        global question
        global has_question
        question += recognizer.recognize_whisper(audio, model="medium",language="english") + ' '#tiny, base, small, medium, large #recognizer.recognize_google(audio, language="en-US") + ' '
        has_question = True
    except sr.UnknownValueError:
        print("Whisper Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Whisper Speech Recognition service; {0}".format(e))
