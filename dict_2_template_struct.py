import streamlit as st
import structuredreport_from_voice
import streamlit as st
from PIL import Image

PAGES = {
    "LLM-assisted Structured Radiological Report": structuredreport_from_voice
}

image = Image.open('Unknown.jpg')
st.sidebar.image(image)
page = PAGES["LLM-assisted Structured Radiological Report"]
page.app()

st.sidebar.title("About")
st.sidebar.info(
    """
    LLM-assisted Structured Radiological Report.
    
    This app was developed and is maintained by João Santinha.
"""
)
