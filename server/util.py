import joblib
import numpy as np
import os
import json
__state = None
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

def get_estimated_price(state,category, bathrooms, bedrooms, fee, pets_allowed,square_feet, cityname,with_storage, with_parking,with_gym, with_pool, with_woodfloors,with_patio,with_clubhouse,with_internet, with_gated):
    
    for state in STATES:  
       
        
            # loading the encoder for that particular city
            city_encoder = joblib.load(os.path.join(CITYNAME_ENCODER_PATH, f'{state}_cityname_encoder.pkl'))
            pets_encoder = joblib.load(os.path.join(PETS_ENCODER_PATH, f'{state}_pets_encoder.pkl'))
            category_encoder = joblib.load(os.path.join(CATEGORY_ENCODER_PATH, f'{state}_category_encoder.pkl'))
            fee_encoder = joblib.load(os.path.join(FEE_ENCODER_PATH, f'{state}_fee_encoder.pkl'))
            storage_encoder = joblib.load(os.path.join(STORAGE_ENCODER_PATH, f'{state}_storage_encoder.pkl'))
            parking_encoder = joblib.load(os.path.join(PARKING_ENCODER_PATH, f'{state}_parking_encoder.pkl'))
            gym_encoder = joblib.load(os.path.join(GYM_ENCODER_PATH, f'{state}_gym_encoder.pkl'))
            pool_encoder = joblib.load(os.path.join(POOL_ENCODER_PATH, f'{state}_pool_encoder.pkl'))
            woodfloors_encoder = joblib.load(os.path.join(WOODFLOORS_ENCODER_PATH, f'{state}_woodfloors_encoder.pkl'))
            patio_encoder = joblib.load(os.path.join(POOL_ENCODER_PATH, f'{state}_pool_encoder.pkl'))
            clubhouse_encoder = joblib.load(os.path.join(PATIO_ENCODER_PATH, f'{state}_patio_encoder.pkl'))
            internet_encoder = joblib.load(os.path.join(INTERNET_ENCODER_PATH, f'{state}_internet_encoder.pkl'))
            gated_encoder = joblib.load(os.path.join(GATED_ENCODER_PATH, f'{state}_gated_encoder.pkl'))

            model = joblib.load(os.path.join(MODEL_PATH, f'{state}_model.pkl'))  # select the model

            # make inputs compatible with our machine learning model
            city = city_encoder.transform([cityname])
            pets = pets_encoder.transform([[pets_allowed]])
            category = category_encoder.transform([[category]])
            fee = fee_encoder.transform([[fee]])
            storage = storage_encoder.transform([[with_storage]])
            parking = parking_encoder.transform([[with_parking]])
            gym = gym_encoder.transform([[with_gym]])
            pool = pool_encoder.transform([[with_pool]])
            wood_floors = woodfloors_encoder.transform([[with_woodfloors]])
            patio = patio_encoder.transform([[with_patio]])
            clubhouse = clubhouse_encoder.transform([[with_clubhouse]])
            internet = internet_encoder.transform([[with_internet]])
            gated = gated_encoder.transform([[with_gated]])

        # make the prediction
            preds = model.predict(np.array([
                category,
                bathrooms,
                bedrooms,
                fee,
                pets,
                square_feet,
                city,
                storage,
                parking,
                gym,
                pool,
                wood_floors,
                patio,
                clubhouse,
                internet,
                gated
            ], dtype='object').reshape(-1, 1).T)
            preds = preds[0]
            preds = np.round(preds)

            return preds



if __name__ == '__main__':

    print("Starting Python Flask Server For Rent Prediction...")
    params = ['TX','apartment', 1, 2, 'No', 'no pets'
                , 1000, 'Dallas', 'True', 'True'
                , 'True', 'False', 'False', 'True', 'False', 'True', 'False']
    get_estimated_price(params)
    get_estimated_price('home', 1, 3, 'No', 'no pets'
                , 1000, 'Dallas', 'True', 'True'
                , 'True', 'False', 'False', 'True', 'False', 'True', 'False')
    app.run()
