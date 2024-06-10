from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the pre-trained machine learning model
model = joblib.load('model.pkl')

# Define a dictionary mapping numeric predictions to textual labels
prediction_labels = {
    0: 'Not Safe for drinking',
    1: 'Safe for drinking',
    2: 'Good'
}

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for predicting water quality
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request form
    ph = float(request.form['ph'])
    hardness = float(request.form['hardness'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])

    # Perform prediction using the loaded model
    prediction = model.predict([[ph, hardness, conductivity, organic_carbon, trihalomethanes, turbidity]])[0]

    # Convert numpy.int64 to Python int
    prediction = int(prediction)

    # Get the textual label corresponding to the prediction
    prediction_text = prediction_labels.get(prediction, 'Unknown')

    # Return prediction and prediction text as JSON response
    return jsonify({'prediction': prediction, 'prediction_text': prediction_text})

if __name__ == '__main__':
    app.run(debug=True)
