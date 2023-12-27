from flask import Flask, render_template, request
import pandas as pd
from sklearn.externals import joblib  # Use joblib for loading the pre-trained model

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('dizs_pred_mlmodel.joblib')  # Replace with the actual filename

# Load the data
data = pd.read_csv('data/dizs_sympt_data.csv')  # Replace with the actual filename

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get selected symptoms from the form
        selected_symptoms = request.form.getlist('symptoms')

        # Create a dictionary to store user-selected symptoms and their information
        user_data = {column: [] for column in data.columns[1:]}
        for symptom in selected_symptoms:
            user_data[symptom] = 'Yes'

        # Create a DataFrame with user-selected symptoms
        user_df = pd.DataFrame([user_data])

        # Make a prediction using the pre-trained model
        prediction = model.predict(user_df)[0]

        # Get the disease type based on the prediction
        disease_type = data.loc[data['disease_types'] == prediction].iloc[0]['disease_types']

        return render_template('index.html', prediction=disease_type)
    
    return render_template('index.html', symptoms=data.columns[1:])

if __name__ == '__main__':
    app.run(debug=True)

