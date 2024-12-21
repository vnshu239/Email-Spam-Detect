from django.shortcuts import render
import joblib

# Load your model and vectorizer
model = joblib.load('spam_classifier_model.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def predict(request):
    result = None  # Initialize result to None
    if request.method == 'POST':
        input_data = request.POST.get('input_data', '').strip()
        if input_data:  # Ensure input_data is not empty
            input_data_features = vectorizer.transform([input_data])
            prediction = model.predict(input_data_features)
            result = 'Not Spam Mail' if prediction[0] == 1 else 'Spam Mail'
    return render(request, 'index.html', {'result': result})
