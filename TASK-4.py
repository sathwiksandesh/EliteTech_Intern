import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load dataset from your path
df = pd.read_csv(r'C:/Users/lenovo/Downloads/email.csv', encoding='latin-1')

# Keep only relevant columns
df = df[['Category', 'Message']]

# Drop missing values
df = df.dropna(subset=['Category', 'Message'])

# Check unique labels
print("Unique categories:", df['Category'].unique())

# Map 'ham' to 0 and 'spam' to 1
df['label_num'] = df['Category'].map({'ham': 0, 'spam': 1})

# Drop rows where mapping produced NaN (if any)
df = df.dropna(subset=['label_num'])

# Convert labels to int
df['label_num'] = df['label_num'].astype(int)

# Check no NaNs remain
print("NaNs in target after mapping:", df['label_num'].isna().sum())

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['Message'], df['label_num'], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict on test
y_pred = model.predict(X_test_vec)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Sample predictions
samples = [
    "Free entry in 2 a weekly competition to win FA Cup final tickets!",
    "Hi, are you coming to the party tonight?"
]

sample_vec = vectorizer.transform(samples)
preds = model.predict(sample_vec)

for msg, pred in zip(samples, preds):
    print(f"\nMessage: {msg}\nPrediction: {'Spam' if pred == 1 else 'Ham'}")
