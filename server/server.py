from flask import Flask,request,jsonify,render_template
import util
#from flask_cors import CORS
#from flask_restful import Resource, Api
import joblib
import numpy as np
import os
import json

# CONSTANTS
STATES = ['TX', 'CA', 'VA', 'NC', 'CO', 'FL', 'MA', 'MD']
MODEL_PATH = 'Objects/Models/'
CITYNAME_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/cityname/'
PETS_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/pets/'


# Create a flask app
app = Flask(__name__)

# create the home endpoint note: @app.route exposes http endpoint


# create an endpoint to predict
@app.route('/Predict', methods=['GET', 'POST'])

# fetch the inputs from the form
def predict_rent():
    if request.method == 'POST':
            state = request.form['state']
            if state == 'Texas':
                    state = 'TX'
            elif state == 'California':
                    state = 'CA'
            elif state == 'Virginia':
                    state = 'VA'
            elif state == 'North Carolina':
                    state = 'NC'
            elif state == 'Colorado':
                    state = 'CO'
            elif state == 'Florida':
                    state = 'FL'
            elif state == 'Massachusetts':
                    state = 'MA'
            elif state == 'Maryland':
                    state = 'MD'
            category = request.form['category']
            bathrooms = int(request.form['bathrooms'])
            bedrooms = int(request.form['bedrooms'])
            fee = request.form['fee']
            pets_allowed = request.form['pets_allowed']
            square_feet = float(request.form['square_feet'])
            cityname = request.form['cityname']
            with_storage = request.form['with_storage']
            with_parking = request.form['with_parking']
            with_gym = request.form['with_gym']
            with_pool = request.form['with_pool']
            with_woodfloors = request.form['with_woodfloors']
            with_patio = request.form['with_patio']
            with_clubhouse = request.form['with_clubhouse']
            with_internet = request.form['with_internet']
            with_gated = request.form['with_gated']


    response = jsonify({
                     'estimated_rent': util.get_estimated_rent(state,category, bathrooms, bedrooms, fee, pets_allowed, square_feet, cityname, with_storage, with_parking, with_gym, with_pool, with_woodfloors, with_patio, with_clubhouse, with_internet, with_gated)
            })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

    
if __name__ == "__main__":
    print("Starting Python Flask Server For Rent Prediction...")
    #util.load_saved_artifacts()

    app.run(debug=True)
         
