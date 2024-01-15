function predictDisease() {
    // Collect selected symptoms
    const selectedSymptoms = document.querySelectorAll('input[name="symptoms"]:checked');
    const symptomsArray = Array.from(selectedSymptoms).map(symptom => symptom.value);

    // Send the input data to the server for prediction
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            symptoms: symptomsArray.join(','),
        }),
    })
    .then(response => response.text())
    .then(data => {
        // Display the prediction result
        document.getElementById('prediction-result').innerHTML = data;
    })
    .catch(error => console.error('Error:', error));
}
