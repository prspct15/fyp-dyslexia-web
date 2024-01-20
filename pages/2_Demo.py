import streamlit as st
import numpy as np    
import tensorflow as tf
import os,urllib

def run():
    st.set_page_config(
        page_title="Demo",
        page_icon="💻",
    )

    st.title("Model Demonstration")
    st.sidebar.title("CS259 Final Year Project")

    application()

@st.cache_data(show_spinner=False)
def load_model():
    model = tf.keras.models.load_model('model.h5')
    return model

def application():
    model = load_model()
    st.write("## Upload your handwriting sample")
    uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg', 'jpeg'])
    if uploaded_file is not None:
        image = tf.io.decode_image(uploaded_file.read(), channels=3)
        resizedImage = tf.image.resize(image, [32, 32])
        input = tf.expand_dims(resizedImage, axis=0)

        # use uploaded_file so that it shows the uploaded image

        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        placeholder = st.empty()
        placeholder.text("Classifying...")
        
        predictions = model.predict(input)
        
        # set classify values as 0 = non-dyslexic, 1 = potentially dyslexic

        # st.write(predictions)

        # st.write(predictions[0][0])
        placeholder.empty()

        if (predictions[0][0] > 0.5):
            st.write("The model predicts that the handwriting is **potentially dyslexic**.")
        else:
            st.write("The model predicts that the handwriting is **non-dyslexic**.")

        st.write("*Disclaimer: This model is not 100% accurate and should not be used as a diagnosis tool.*")
       
   
if __name__ == "__main__":
    run()