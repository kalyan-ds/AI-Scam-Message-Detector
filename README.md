# 📩 AI Scam Message Detector using NLP

## 🧠 Project Overview

This project builds an AI-powered Spam Message Detector using Natural Language Processing (NLP) and Machine Learning techniques.

The model analyzes SMS text messages and predicts whether the message is:

- ✅ **Ham (Normal Message)**
- ⚠️ **Spam (Scam Message)**

This system helps detect fraudulent or suspicious messages automatically.

---

## 🎯 Project Objectives

- Detect scam/spam SMS messages using machine learning
- Perform real-world NLP preprocessing
- Build a high-accuracy classification model
- Enable real-time message prediction
- Save trained model for future use

---

## 📊 Dataset Information

- Dataset Name: **SMS Spam Collection Dataset**
- Total Messages: **5,572**
- Classes:
  - **Ham (Normal Messages)** — 4,825
  - **Spam Messages** — 747

The dataset contains real SMS messages labeled as spam or normal.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Matplotlib
- Joblib

---

## ⚙️ Machine Learning Workflow

The following steps were performed:

### 1️⃣ Data Cleaning
- Removed unnecessary columns
- Renamed columns for clarity
- Converted labels (Ham = 0, Spam = 1)

### 2️⃣ Text Preprocessing
- Converted text to lowercase
- Removed special characters
- Removed extra spaces

### 3️⃣ Feature Engineering
- Applied **TF-IDF Vectorization**
- Used unigrams and bigrams
- Removed English stopwords

### 4️⃣ Model Training
Used:

- Logistic Regression Classifier

### 5️⃣ Model Evaluation
Evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score
- ROC Curve
- Confusion Matrix

---

## 📈 Model Performance

| Metric | Value |
|-------|------|
| Accuracy | **~95%** |
| Spam Precision | **~97%** |
| Spam Recall | **~66–85%** |
| ROC-AUC Score | **~0.98+** |

The model successfully detects spam messages with high reliability.

---

## 🔍 Example Prediction

### Input Message:
# 📩 AI Scam Message Detector using NLP

## 🧠 Project Overview

This project builds an AI-powered Spam Message Detector using Natural Language Processing (NLP) and Machine Learning techniques.

The model analyzes SMS text messages and predicts whether the message is:

- ✅ **Ham (Normal Message)**
- ⚠️ **Spam (Scam Message)**

This system helps detect fraudulent or suspicious messages automatically.

---

## 🎯 Project Objectives

- Detect scam/spam SMS messages using machine learning
- Perform real-world NLP preprocessing
- Build a high-accuracy classification model
- Enable real-time message prediction
- Save trained model for future use

---

## 📊 Dataset Information

- Dataset Name: **SMS Spam Collection Dataset**
- Total Messages: **5,572**
- Classes:
  - **Ham (Normal Messages)** — 4,825
  - **Spam Messages** — 747

The dataset contains real SMS messages labeled as spam or normal.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression
- Matplotlib
- Joblib

---

## ⚙️ Machine Learning Workflow

The following steps were performed:

### 1️⃣ Data Cleaning
- Removed unnecessary columns
- Renamed columns for clarity
- Converted labels (Ham = 0, Spam = 1)

### 2️⃣ Text Preprocessing
- Converted text to lowercase
- Removed special characters
- Removed extra spaces

### 3️⃣ Feature Engineering
- Applied **TF-IDF Vectorization**
- Used unigrams and bigrams
- Removed English stopwords

### 4️⃣ Model Training
Used:

- Logistic Regression Classifier

### 5️⃣ Model Evaluation
Evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score
- ROC Curve
- Confusion Matrix

---

## 📈 Model Performance

| Metric | Value |
|-------|------|
| Accuracy | **~95%** |
| Spam Precision | **~97%** |
| Spam Recall | **~66–85%** |
| ROC-AUC Score | **~0.98+** |

The model successfully detects spam messages with high reliability.

---

## 🔍 Example Prediction

### Input Message:
Congratulations! You won ₹50,000. Click here now!
### Output:⚠️ Spam Detected
---

## 💾 Saved Model Files

The trained model and vectorizer are saved using Joblib:


spam_detector_model.pkl
tfidf_vectorizer.pkl


These files allow future predictions without retraining.

---

## 📂 Project Structure


AI-Scam-Message-Detector/
│
├── scam_detector.ipynb
├── spam.csv
├── spam_detector_model.pkl
├── tfidf_vectorizer.pkl
├── README.md


---

## 🚀 Future Improvements

Planned enhancements:

- Build interactive web application using **Streamlit**
- Deploy model online
- Add support for multilingual messages
- Improve spam detection recall
- Add deep learning models (LSTM)

---

## 🧠 Key Learnings

Through this project, the following skills were developed:

- Natural Language Processing (NLP)
- Text Cleaning Techniques
