# Phishing Email Detection Model

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    'email': [
        'Congratulations! You won a free iPhone click here',
        'Your bank account has been suspended login immediately',
        'Meeting scheduled for tomorrow at 10 AM',
        'Please find the project report attached',
        'Claim your lottery prize now',
        'Team meeting has been postponed'
    ],
    
    'label': [
        'Phishing',
        'Phishing',
        'Safe',
        'Safe',
        'Phishing',
        'Safe'
    ]
}

df = pd.DataFrame(data)

X = df['email']
y = df['label']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.3,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


print("\nClassification Report:")
print(classification_report(y_test, y_pred))


new_email = ["Click here to claim your free reward now"]

new_email_vector = vectorizer.transform(new_email)


prediction = model.predict(new_email_vector)

print("\nNew Email Prediction:", prediction[0])
