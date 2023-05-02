import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv('tweets.csv')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model using Naive Bayes algorithm
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Evaluate model on testing set
y_pred = clf.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Make predictions on new data
new_tweets = ['This movie is amazing!', 'I hate waiting in line', 'The weather is perfect today']
new_tweets_vec = vectorizer.transform(new_tweets)
predictions = clf.predict(new_tweets_vec)
print('Predictions: ', predictions)