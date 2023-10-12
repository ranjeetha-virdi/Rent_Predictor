
from flask import Flask, render_template,request,jsonify
import joblib
import numpy as np
import os
import json

# CONSTANTS
STATES = ['TX', 'CA', 'VA', 'NC', 'CO', 'FL', 'MA', 'MD']
MODEL_PATH = 'Objects/Models/'
CITYNAME_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/cityname/'
PETS_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/pets/'
CATEGORY_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/category/'
FEE_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/fee/'
STORAGE_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/storage/'
PARKING_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/parking/'
GYM_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/gym/'
POOL_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/pool/'
WOODFLOORS_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/woodfloors/'
PATIO_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/patio/'
CLUBHOUSE_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/clubhouse/'
INTERNET_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/internet/'
GATED_ENCODER_PATH = 'Objects/Encoders/BinaryEncoder/gated/'

# Create a flask app
app = Flask(__name__)


# create the home endpoint note: @app.route exposes http endpoint
@app.route('/')
def home():
    return render_template('home.html')


# create an endpoint to predict
@app.route('/Predict', methods=['GET', 'POST'])
# fetch the inputs from the form


    state = request.form['state'].strip()
    city = request.form['city'].lower()
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    category = request.form['category']
    fee = request.form['fee']
    pets = request.form['pets']
    storage = request.form['storage']
    parking = request.form['parking']
    gym = request.form['gym']
    pool = request.form['pool']
    wood_floors = request.form['wood_floors']
    patio = request.form['patio']
    clubhouse = request.form['clubhouse']
    internet = request.form['internet']
    gated = request.form['gated']

if __name__ == "__main__":
    print("Starting Python Flask Server For Rent Prediction...")
    predict(['apartment',2,1,'No','no pets'
            ,'1000','Dallas','True','True'
            ,'True','False','False','True','False','True','False'])
    predict(['home', 3, 1, 'No', 'no pets'
            , '1000', 'Dallas', 'True', 'True'
            , 'True', 'False', 'False', 'True', 'False', 'True', 'False'])
    app.run()
         
