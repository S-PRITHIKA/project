import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import json

# Load the pretrained model
model = load_model("C:\Users\prith\OneDrive\Desktop\plant disease\dataset")

# Load class names
with open("class_names.json") as f:
    class_names = json.load(f)

st.title("🌱 Plant Disease Identifier")
st.write("Upload a leaf image to detect its disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    img = Image.open(uploaded_file).resize((128,128))
    st.image(img, caption='Uploaded Leaf Image', use_column_width=True)

    # Preprocess
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255.0

    # Predict
    pred = model.predict(x)
    class_idx = np.argmax(pred)
    st.success(f"Prediction: {class_names[str(class_idx)]}")
