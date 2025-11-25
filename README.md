🌿 Plant Disease Detection Using Deep Learning

This project is an AI-powered **Plant Disease Detection System** that identifies diseases from plant leaf images using a deep learning model.
It helps **farmers, students, researchers, and gardeners** detect diseases early and take preventive action.

 🚀 Features

✔ Upload leaf images for **instant disease prediction**
✔ Predicts **disease name + confidence score**
✔ User-friendly **Streamlit web app**
✔ Separate **training script** to retrain with any dataset
✔ Supports **multiple plant species & disease types**
✔ Built using **Convolutional Neural Networks (CNN)**
✔ Works offline once model is trained

 🧠 Tech Stack

**Backend & AI**

* Python
* TensorFlow / Keras
* NumPy
* OpenCV
* Matplotlib

**Frontend / UI**

* Streamlit
* HTML templates (optional for Flask)

**Storage**

* JSON (class labels)

 📂 Project Structure

```
plant-disease-detection/
│
├── train_model.py              # Model training script
├── streamlit_app.py            # Streamlit front-end app
├── app.py                      # Optional Flask backend
│
├── plant_disease_model.h5      # Trained deep learning model
├── class_names.json            # Class labels for prediction
│
├── templates/                  # HTML files (used only for Flask)
├── dataset/                    # Training dataset (not included)
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

 🔍 How It Works

1. User uploads an image of a plant leaf
2. Image is preprocessed (resize → normalize → reshape)
3. Model predicts disease class
4. Outputs:

   * **Disease name**
   * **Confidence percentage**
5. (Optional) Suggests preventive measures


 ▶️ How to Run the Project

### **1) Install dependencies**

```sh
pip install -r requirements.txt
```

### **2) Run Streamlit Web App**

```sh
streamlit run streamlit_app.py
```

### **3) Run Flask App (optional)**

```sh
python app.py
```

 📊 Dataset

* Includes multiple plant species
* Contains healthy and diseased leaf images
* Preprocessed and augmented for better accuracy
* Compatible with **PlantVillage dataset** format

🖼 Output Example

* **Predicted Disease:** Tomato Early Blight
* **Confidence:** 97.12%
* Displays uploaded image + prediction summary

 📌 Future Improvements

* Add voice-based disease description
* Provide real-time prevention suggestions
* Deploy model using FastAPI + Docker
* Mobile app support using Flutter

