import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

st.title("English → Hindi Translator with Voice")

text = st.text_input("Enter English sentence")

if st.button("Translate and Speak"):

    # translate
    hindi_text = GoogleTranslator(source='en', target='hi').translate(text)

    st.subheader("Hindi Translation")
    st.write(hindi_text)

    # text to speech
    tts = gTTS(text=hindi_text, lang='hi')
    tts.save("speech.mp3")

    audio_file = open("speech.mp3", "rb")
    st.audio(audio_file.read(), format="audio/mp3")
