import streamlit as st
from googletrans import Translator, LANGUAGES

translator = Translator()

st.title("🌍 AI Language Translation Tool")

text = st.text_area("Enter text to translate:")

languages = list(LANGUAGES.values())

source_lang = st.selectbox("Select Source Language:", languages)
target_lang = st.selectbox("Select Target Language:", languages)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = translator.translate(
            text,
            src=list(LANGUAGES.keys())[languages.index(source_lang)],
            dest=list(LANGUAGES.keys())[languages.index(target_lang)]
        )

        st.success("Translation Successful!")
        st.write("### Translated Text:")
        st.write(translated.text)
