import streamlit as st
from googletrans import Translator
from gtts import gTTS

st.title("English → Hindi Translator with Voice")

# user input
english_text = st.text_input("Enter English sentence")

if st.button("Translate and Speak"):

    # translate
    translator = Translator()
    translated = translator.translate(english_text, src='en', dest='hi')
    hindi_text = translated.text

    st.subheader("Hindi Translation")
    st.write(hindi_text)

    # text to speech
    tts = gTTS(text=hindi_text, lang='hi')
    tts.save("speech.mp3")

    # play audio in browser
    audio_file = open("speech.mp3", "rb")
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format="audio/mp3")
