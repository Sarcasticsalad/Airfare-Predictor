import uvicorn
from fastapi import FastAPI
import pickle
import os
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse

# App object
app = FastAPI()

# Load Machine Learning Model
pickle_in = open("../machine_learning/flight_price_rf_v2.pkl", "rb")
rf_reg_model = pickle.load(pickle_in)

# List of airlines
Airline_names = [
    'Air Arabia', 'Air Canada', 'Air China', 'Air France', 'Air India',
    'American Airlines', 'Austrian', 'British Airways', 'Brusseis',
    'Cathay Pacific', 'China Eastern', 'China Southern', 'Delta',
    'Easy Jet', 'Emirates', 'Etihad', 'IndiGo', 'Korean Air',
    'Lufthansa', 'Luxiar', 'Malaysia Airlines', 'Malindo Air',
    'Nepal Airlines', 'Qantas', 'Qatar Airways', 'SWISS',
    'Singapore Airlines', 'SriLankan Airlines', 'THAI',
    'Turkish Airlines', 'United Airlines', 'Virgin Atlantic',
    'Vueling', 'flydubai']

# List of departure locations
Departure_locations = ['Beijing', 'Berlin', 'Chicago',
                       'Delhi', 'Dubai', 'Kathmandu', 'London', 'New Delhi', 'New York',
                       'Paris', 'Sydney']

# List of destination locations
Destination_locations = ['Beijing', 'Berlin', 'Chicago', 'Dubai',
                          'Kathmandu', 'London', 'New Delhi',
                          'New York', 'Singapore', 'Sydney']

# List of flight class types
Flight_Class_type = ['Business', 'Economy', 'First']

# Function to preprocess the input
def preprocess_data(Airline, Departure, Destination, Departure_date, Arrival_date, Stops, Travel_time, Flight_Class):
    # Extracting month and date from departure and arrival dates
    departure_month = pd.to_datetime(Departure_date).month
    departure_day = pd.to_datetime(Departure_date).day
    arrival_month = pd.to_datetime(Arrival_date).month
    arrival_day = pd.to_datetime(Arrival_date).day

    # Convert date of the day to week day and one-hot encode it
    departure_weekday = pd.to_datetime(Departure_date).strftime('%A')
    weekdays = ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    departure_weekday_encoded = [int(departure_weekday == day) for day in weekdays]

    # Encoding code 2.0
    Airline_encoded = [int(Airline == name) for name in Airline_names]
    Departure_encoded = [int(Departure == loc) for loc in Departure_locations]
    Destination_encoded = [int(Destination == loc) for loc in Destination_locations]
    #Flight_Class_encoded = [int(Flight_Class == fc) for fc in Flight_Class]
    Flight_Class_encoded = [int(Flight_Class == fc_type) for fc_type in Flight_Class_type]


    #  # Print lengths for debugging
    # print("Lengths of encoded features:")
    # print("Airline_encoded:", len(Airline_encoded))
    # print("Departure_encoded:", len(Departure_encoded))
    # print("Destination_encoded:", len(Destination_encoded))
    # print("Flight_Class_encoded:", len(Flight_Class_encoded))

    # Create a 1D array with all the features
    features = np.array([[Stops, Travel_time, departure_month, departure_day, arrival_month, arrival_day]
                         + Airline_encoded + Departure_encoded + Destination_encoded
                         + departure_weekday_encoded + Flight_Class_encoded])

    return features

# Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict")
async def predict(
        departure_date: str,
        departure: str,
        arrival_date: str,
        destination: str,
        airline: str,
        flight_class: str,
        stops: int,
        travel_time: int):

    features = preprocess_data(airline, departure, destination, departure_date, arrival_date, stops, travel_time, flight_class)

    # print(features)

    
    # Predicting
    predict_price = rf_reg_model.predict(features)

    predict_price = str(predict_price[0])
    

    return JSONResponse({"price":predict_price})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

    