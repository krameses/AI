import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

st.title("English → Hindi Translator")

english_text = st.text_input("Enter English sentence")

if st.button("Translate and Speak"):

    # translate
    hindi_text = GoogleTranslator(source='en', target='hi').translate(english_text)

    st.subheader("Hindi Translation")
    st.write(hindi_text)

    # convert text to speech
    tts = gTTS(text=hindi_text, lang='hi')

    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    # play audio
    st.audio(audio_buffer, format="audio/mp3")
