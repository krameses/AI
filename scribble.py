import streamlit as st
import easyocr
import numpy as np
from PIL import Image
from transformers import pipeline

st.title("📝 Handwritten Notes → AI Summary")

# upload image
uploaded_file = st.file_uploader("Upload scanned handwritten notes")

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Notes")

    # OCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(np.array(image))

    extracted_text = " ".join([detection[1] for detection in result])

    st.subheader("Extracted Text")
    st.write(extracted_text)

    # summarization model
    summarizer = pipeline("summarization")

    if st.button("Generate AI Summary"):

        summary = summarizer(
            extracted_text,
            max_length=120,
            min_length=30,
            do_sample=False
        )

        st.subheader("AI Summary")
        st.write(summary[0]['summary_text'])
