import pandas as pd
import random

# Generate a list of Diseases related variables 
disease_var = ["disease_types", "age", "gender", "blood_pressure", "cholesterol"]

# Generate a dictionary of 42 diseases and their symptoms (replace with actual symptoms)
disease_symptoms = {
    "Flu": ["fever", "cough", "fatigue", "headache", "body aches", "chills"],
    "Diabetes": ["increased thirst", "frequent urination", "fatigue", "unexplained weight loss", "blurred vision"],
    "Asthma": ["shortness of breath", "wheezing", "coughing", "chest tightness"],
    "Heart Disease": ["chest pain", "shortness of breath", "fatigue", "dizziness", "irregular heartbeat"],
    "Hypertension": ["headache", "fatigue", "dizziness", "blurred vision"],
    "Arthritis": ["joint pain", "joint swelling", "morning stiffness", "decreased range of motion"],
    "Alzheimer's Disease": ["memory loss", "confusion", "difficulty in problem-solving", "language problems"],
    "Parkinson's Disease": ["tremors", "rigidity", "bradykinesia", "postural instability"],
    "Cancer": ["unexplained weight loss", "fatigue", "pain", "skin changes", "changes in bowel habits"],
    "COPD": ["shortness of breath", "chronic cough", "sputum production", "wheezing"],
    "Kidney Disease": ["fatigue", "swelling", "changes in urine output", "blood in urine"],
    "Liver Disease": ["jaundice", "abdominal pain", "swelling", "fatigue"],
    "Osteoporosis": ["back pain", "loss of height", "stooped posture", "fractures"],
    "Depression": ["persistent sadness", "loss of interest or pleasure", "changes in appetite", "sleep disturbances"],
    "Anxiety": ["excessive worrying", "restlessness", "fatigue", "difficulty concentrating"],
    "Migraine": ["severe headache", "nausea", "sensitivity to light and sound", "aura"],
    "Rheumatoid Arthritis": ["joint pain", "joint swelling", "morning stiffness", "fatigue"],
    "Lupus": ["joint pain", "skin rash", "fatigue", "fever", "kidney problems"],
    "Multiple Sclerosis": ["fatigue", "numbness or tingling", "muscle weakness", "balance problems"],
    "Crohn's Disease": ["abdominal pain", "diarrhea", "fatigue", "weight loss"],
    "Ulcerative Colitis": ["abdominal pain", "bloody stools", "diarrhea", "fatigue"],
    "Schizophrenia": ["hallucinations", "delusions", "disorganized thinking", "social withdrawal"],
    "Bipolar Disorder": ["mood swings", "energy changes", "impulsivity", "sleep disturbances"],
    "Endometriosis": ["pelvic pain", "painful periods", "pain during intercourse", "infertility"],
    "PCOS": ["irregular periods", "excessive hair growth", "acne", "weight gain"],
    "Fibromyalgia": ["widespread pain", "fatigue", "sleep disturbances", "cognitive difficulties"],
    "Chronic Fatigue Syndrome": ["profound fatigue", "sleep disturbances", "cognitive difficulties", "muscle pain"],
    "Psoriasis": ["skin redness", "itching", "scaling", "joint pain"],
    "Eczema": ["itching", "redness", "dry skin", "rashes"],
    "Celiac Disease": ["abdominal pain", "bloating", "diarrhea", "fatigue"],
    "Anemia": ["fatigue", "pale skin", "weakness", "shortness of breath"],
    "Hypothyroidism": ["fatigue", "weight gain", "cold intolerance", "dry skin"],
    "Hyperthyroidism": ["weight loss", "increased appetite", "anxiety", "tremors"],
    "GERD": ["heartburn", "acid regurgitation", "chest pain", "difficulty swallowing"],
    "Sleep Apnea": ["loud snoring", "episodes of stopped breathing during sleep", "excessive daytime sleepiness"],
    "Chronic Kidney Disease": ["fatigue", "swelling", "changes in urine output", "blood in urine"],
    "Pancreatitis": ["abdominal pain", "nausea", "vomiting", "fever"],
    "Gallstones": ["abdominal pain", "nausea", "vomiting", "jaundice"],
    "Hemorrhoids": ["rectal bleeding", "anal itching", "pain during bowel movements", "swelling"],
    "Diverticulitis": ["abdominal pain", "fever", "changes in bowel habits", "nausea"],
    "Ovarian Cancer": ["abdominal bloating", "pelvic pain", "changes in appetite", "fatigue"],
    "Testicular Cancer": ["lump in the testicle", "testicular pain", "enlarged testicle", "back pain"]
}

# Create a list to store all sorted and unique symptoms
all_sorted_symptoms = []

# Iterate over the dictionary
for symptoms_list in disease_symptoms.values():
    # Sort the symptoms and remove duplicates
    sorted_unique_symptoms = sorted(set(symptoms_list))
    
    # Extend the list with sorted and unique symptoms
    all_sorted_symptoms.extend(sorted_unique_symptoms)

# Remove duplicates from the combined list
Symptoms = sorted(set(all_sorted_symptoms))

# print(Symptoms)

# Combine all variables into a single list
DatasetColumns = disease_var + Symptoms

# Create an empty DataFrame
df = pd.DataFrame(columns=DatasetColumns)
# Populate the DataFrame with random data
df["disease_types"] = disease_symptoms.keys()
for index, row in df.iterrows():
    for column in df.columns:
        df.at[index, 'age'] = random.randint(18, 80)
        df.at[index, 'gender'] = random.choice(["M", "F"])
        df.at[index, 'blood_pressure'] = random.choice(["Normal", "High"])
        df.at[index, 'cholesterol'] = random.choice(["Normal", "High"])

# Update DataFrame based on conditions
for key, value in disease_symptoms.items():
    
    for column_to_check in value:
        # Get the row index where the value in the 'ID' column matches the key
        diseaseT_index = df.index[df['disease_types'] == key].tolist()[0]
                
        # Check if the column name matches the value in the list
        if column_to_check in df.columns:
            df.at[diseaseT_index, column_to_check] = 'Yes'
# Save the dataset to CSV
df.to_csv('./data/dizs_sympt_data.csv', index=False)