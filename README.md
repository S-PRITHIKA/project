 🌿 Plant Disease Detection Using Deep Learning

📌 Overview

The Plant Disease Detection System is an AI-powered application that identifies plant diseases from leaf images using a Convolutional Neural Network (CNN) model.

This system enables early disease detection, helping farmers, researchers, students, and gardeners take timely preventive measures to improve crop health and productivity.

The application provides real-time predictions through a user-friendly web interface and can operate offline once the model is trained.

  Key Features

*  Upload plant leaf images for instant disease prediction
*  Predicts disease class with confidence score
*  Interactive web interface built with Streamlit
*  Separate training script for retraining with custom datasets
*  Supports multiple plant species and disease categories
*  Built using Convolutional Neural Networks (CNN)
*  Works offline after model training

 🛠 Tech Stack

🔹 Backend & AI

* Python
* TensorFlow
* NumPy
* OpenCV
* Matplotlib

🔹 Frontend / UI

* Streamlit
* HTML Templates

 🔹 Storage

* JSON files (for class labels and metadata)

 📂 Project Structure

```
plant-disease-detection/
│
├── train_model.py              # Model training script
├── streamlit_app.py            # Streamlit web interface
├── app.py                      # Flask-based web application
│
├── plant_disease_model.h5      # Trained CNN model
├── class_names.json            # Disease class labels
│
├── templates/                  # HTML templates (Flask)
├── dataset/                    # Training dataset
│
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

⚙️ How It Works

1. The user uploads an image of a plant leaf.
2. The image is resized and preprocessed for model compatibility.
3. The trained CNN model analyzes the image.
4. The system outputs:

   *  Predicted disease name
   *  Confidence percentage

Dataset

* Contains healthy and diseased leaf images
* Supports multiple plant species
* Preprocessed and augmented for improved accuracy
* Compatible with the PlantVillage dataset format

Future Enhancements

*  Voice-based disease explanation system
*  Real-time prevention and treatment recommendations
*  Deployment using FastAPI and Docker
*  Cross-platform mobile application using Flutter
*  Cloud-based model hosting and API integration

