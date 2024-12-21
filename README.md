# Email Spam Detection System 🚀

An advanced Email Spam Detection web application built with **Django** and powered by a trained **Machine Learning model**. This system uses a **TF-IDF Vectorizer** and a **Logistic Regression model** to classify emails as spam or not spam. It features a sleek, **dark-themed UI/UX design** for an engaging user experience.

---

## 🖥️ Features

- **Real-time Email Classification:** Upload or type your email content, and get instant predictions.
- **Machine Learning Powered:** Uses a pre-trained ML model for accurate spam detection.
- **User-friendly Interface:** Eye-catching dark-themed UI for an excellent user experience.
- **Secure Backend:** Django framework ensures robust backend operations.

---

## 🛠️ Tech Stack

### Frontend
- **HTML5** and **CSS3**
- **Bootstrap** for responsive design
- Custom **dark theme**

### Backend
- **Python** and **Django** framework
- **Joblib** for loading ML models
- **TF-IDF Vectorizer** for text preprocessing

### Machine Learning
- **Logistic Regression** (pre-trained on spam email datasets)
- **TF-IDF Vectorization**

---

## 📂 Project Structure

Email Spam/ 


├── Email_Spam/ 


│ ├── init.py 

│ ├── settings.py 

│ ├── urls.py 

│ ├── views.py 

│ ├── wsgi.py 

├── templates/ 

│ ├── index.html 

├── spam_classifier_model.joblib 

├── tfidf_vectorizer.joblib 

├── db.sqlite3 

├── manage.py


## 🧪 Usage
Enter the email content in the text box.
Click "Predict" to classify the email.
See whether the email is marked as Spam or Not Spam.


## 🔍 Model Details
Vectorizer: TF-IDF (Term Frequency - Inverse Document Frequency)
Algorithm: Logistic Regression
Dataset: Trained on a curated dataset of spam and non-spam emails.
