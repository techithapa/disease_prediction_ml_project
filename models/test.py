# machine_learning_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
dataset = pd.read_csv('./data/dizs_sympt_data.csv')

# Preprocess data
# (Include steps like handling missing values, encoding categorical variables, etc.)a
columns = dataset.columns[1:]

# Perform one-hot encoding
df_encoded = pd.get_dummies(dataset, columns= columns, prefix=columns)
print(df_encoded)
X = df_encoded.drop('disease_types', axis=1)  # Features
y = df_encoded['disease_types']  # Target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier (or any suitable algorithm)
model = RandomForestClassifier(n_estimators=142, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

# Additional evaluation metrics
#print(classification_report(y_test, predictions))


