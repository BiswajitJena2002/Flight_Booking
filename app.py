from flask import Flask, request, render_template
import numpy as np
import joblib
import pandas as pd
from datetime import datetime, timedelta

# Flask app
app = Flask(__name__)

# Load the pre-trained model and the fitted scaler
loaded_model = joblib.load('FlightPrice_GBR.joblib')
scaler = joblib.load('FlightPrice_scaler.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input values from the form
        airline = float(request.form['airline'])
        date_of_journey = request.form['departure-date']
        source = float(request.form['from'])
        destination = float(request.form['to'])
        total_stops = float(request.form['stops'])
        additional_info = float(request.form['additional-info'])
        dep_time = request.form['departure-time']
        arrival_time = request.form['arrival-time']
        travellers = float(request.form['travellers'])

        # Converting Date_of_Journey to datetime format and then to UNIX timestamp
        date_of_journey = pd.to_datetime(date_of_journey, format='%Y-%m-%d')
        date_of_journey_unix = int(date_of_journey.timestamp())

        # Extracting journey day and month
        journey_day = date_of_journey.day
        journey_month = date_of_journey.month

        # Extracting departure and arrival hour and minute
        dep_hour, dep_minute = map(int, dep_time.split(':'))
        arrival_hour, arrival_minute = map(int, arrival_time.split(':'))

        # Calculating duration in minutes
        dep_datetime = datetime.strptime(dep_time, '%H:%M')
        arrival_datetime = datetime.strptime(arrival_time, '%H:%M')
        duration_minutes = (arrival_datetime - dep_datetime).seconds // 60

        # Organize the input features as a numpy array
        features = np.array([[airline, date_of_journey_unix, source, destination, total_stops, additional_info, journey_day, journey_month, dep_hour, dep_minute, arrival_hour, arrival_minute, duration_minutes]])

        # Scale the input data using the fitted scaler
        scaled_test_data = scaler.transform(features)


        # Check if date_of_journey is before today
        if date_of_journey < datetime.now():
            return render_template('index.html', error="Cannot choose a date before today.")

        # Calculate total price based on options
        trip_type = request.form.get('trip-type')
        base_price = loaded_model.predict(scaled_test_data)

        if trip_type == 'Round-trip':
            base_price *= 2

        # Apply discounts
        discount = 0
        if 'student' in request.form:
            discount = 0.1
        elif 'senior-citizen' in request.form:
            discount = 0.06
        elif 'armed-forces' in request.form:
            discount = 0.5
        elif 'doctor-nurse' in request.form:
            discount = 0.25

        total_price = base_price * (1 - discount) * travellers

        # Round off to upper integer rupee
        total_price = np.ceil(total_price)

        return render_template('index.html', prediction=int(total_price))

#if __name__ == "__main__":
#  app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
