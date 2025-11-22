
 Plant Disease Detection Using Deep Learning

This project is a Plant Disease Detection System that uses a trained deep learning model to identify plant leaf diseases from images. The system helps farmers, researchers, and gardeners diagnose diseases early and take preventive action.

 Features

*  Upload plant leaf images for instant disease prediction
*  Deep Learning model trained on thousands of plant images
*  Predicts disease class + gives confidence score
*  Streamlit web app for easy usage
*  Separate training script to retrain the model
*  Supports multiple plant species & disease types

  Tech Stack

* Python
* TensorFlow 
* Streamlit 
* OpenCV
* NumPy, Matplotlib
* JSON for class labels

  Project Structure

```
plant-disease-detection/
│
├── app.py                      # Main application backend
├── streamlit_app.py            # Streamlit UI
├── train_model.py              # Model training script
├── plant_disease_model.h5      # Trained model file
├── class_names.json            # Class labels used by the model
├── templates/                  # HTML templates (if Flask used)
├── archive.zip                 # Dataset or backup archive (optional)
└── README.md                   # Project documentation
```

 How It Works

1. User uploads an image of a plant leaf
2. The image is processed and resized
3. The deep learning model predicts the disease class
4. Results displayed with accuracy scores
5. Optional: Preventive measures can be shown

  How to Run

1️) Install Dependencies

```sh
pip install -r requirements.txt
```

2️) Run Streamlit App

```sh
streamlit run streamlit_app.py
```

3️) Run Flask App 

```sh
python app.py
```

 Dataset

* Dataset consists of multiple plant species 
* Contains healthy + various disease classes
* Images preprocessed and augmented for better accuracy

Output

* Predicted disease name
* Confidence percentage

