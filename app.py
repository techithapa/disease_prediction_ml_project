from collections import Counter
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from joblib import load
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the pre-trained models and other necessary preprocessing objects
rf_model = load('rf_model.pkl')  # Update the path
nb_model = load('nb_model.pkl')
svm_model = load('svm_model.pkl')

# Load the dataset
raw_data = pd.read_csv('data/dataset.csv')

# Data preprocessing
data = raw_data.drop(columns=['Unnamed: 133']).drop_duplicates()
encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

# Separate features and target variable
X = data.drop('prognosis', axis=1)

# Create a dictionary to encode symptoms into numerical values
symptoms = X.columns.values
symptom_index = {f"{' '.join([i.capitalize() for i in value.split('_')])}": index for index, value in enumerate(symptoms)}

# Store information for later use
data_dict = {
    "symptom_index": symptom_index,
    "predictions_classes": encoder.classes_
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get selected symptoms from the form
        selected_symptoms_str = request.form.get('symptoms')
        symptoms = selected_symptoms_str.split(',')

        # Input data for model
        input_data = [0] * len(data_dict["symptom_index"])
        for symptom in symptoms:
            index = data_dict["symptom_index"].get(symptom)
            if index is not None:
                input_data[index] = 1

        # Check the number of features in the input data
        if len(input_data) != len(data_dict["symptom_index"]):
            raise ValueError(f"Input data has {len(input_data)} features, "
                             f"but the model expects {len(data_dict['symptom_index'])} features.")

        # Convert input data into a suitable format
        input_data = np.array(input_data).reshape(1, -1)

        # Make predictions using the pre-trained models
        rf_prediction = data_dict["predictions_classes"][rf_model.predict(input_data)[0]]
        nb_prediction = data_dict["predictions_classes"][nb_model.predict(input_data)[0]]
        svm_prediction = data_dict["predictions_classes"][svm_model.predict(input_data)[0]]

        # Use Counter to find the most common prediction
        final_prediction = Counter([rf_prediction, nb_prediction, svm_prediction]).most_common(1)[0][0]

        # Display predictions in a tabular format
        predictions_table = pd.DataFrame({
            'Model': ['Random Forest', 'Naive Bayes', 'SVM', 'Final Prediction'],
            'Prediction': [rf_prediction, nb_prediction, svm_prediction, final_prediction]
        })

        # Convert DataFrame to HTML
        table_html = predictions_table.to_html(classes='table table-striped', index=False)

        # Render the template with the predictions
        return render_template('index.html', symptoms=data.columns[:-1], prediction=table_html)

    # Render the template with the symptoms
    return render_template('index.html', symptoms=data.columns[:-1])

if __name__ == '__main__':
    app.run(debug=True)
