import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64

st.title("🎤 Voice Translator (English → Hindi)")

recognizer = sr.Recognizer()

if st.button("🎙️ Speak"):

    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            # speech to text
            text = recognizer.recognize_google(audio)
            st.write("You said:", text)

            # translate
            hindi = GoogleTranslator(source='en', target='hi').translate(text)
            st.subheader("Hindi Translation")
            st.write(hindi)

            # convert to speech
            tts = gTTS(text=hindi, lang='hi')
            tts.save("speech.mp3")

            # autoplay
            with open("speech.mp3", "rb") as f:
                audio_bytes = f.read()

            b64 = base64.b64encode(audio_bytes).decode()

            audio_html = f"""
            <audio autoplay>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """

            st.markdown(audio_html, unsafe_allow_html=True)

        except Exception as e:
            st.error("Could not recognize speech")
