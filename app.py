import streamlit as st
from googletrans import Translator, LANGUAGES 

def translate_sentence(sentence, target_language):
    translator = Translator()
    translation = translator.translate(sentence, dest=target_language)
    return translation.text

def detect_language(sentence):
    translator = Translator()
    detected_language = translator.detect(sentence).lang
    return detected_language

st.title("Language Translation App")

input_sentence = st.text_area("Enter a sentence to translate:")
target_language = st.selectbox("Select a target language:", list(LANGUAGES.values()))

if st.button("Translate"):
    detected_language = detect_language(input_sentence)
    st.write(f"Detected Language: {LANGUAGES[detected_language]}")
    
    translated_sentence = translate_sentence(input_sentence, target_language)
    st.write(f"Translated sentence: {translated_sentence}")
