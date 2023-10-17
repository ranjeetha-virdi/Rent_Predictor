import joblib
import numpy as np
import os
import json
__states = None
__model = None
# CONSTANTS

MODEL_PATH = 'Objects/Models/'
CITYNAME_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/cityname/'
PETS_ENCODER_PATH = 'Objects/Encoders/LabelEncoder/pets/'
__states = ['Texas', 'California', 'Virginia', 'North Carolina', 'Colorado', 'Florida', 'Massachusetts', 'Maryland']
'''
def load_saved_artifacts():
    global __model
    global __states
    print("loading saved artifacts...start")
    __states = ['TX', 'CA', 'VA', 'NC', 'CO', 'FL', 'MA', 'MD']
    for state in __states:

        if __model is None:
            __model = joblib.load(os.path.join(MODEL_PATH, f'{state}_model.pkl'))
    print("loading saved artifacts....done")
'''
def get_estimated_rent(state:str,category:str, bathrooms:int, bedrooms:int, fee:str, pets_allowed:str,square_feet:float, cityname:str,with_storage:bool, with_parking:bool,with_gym:bool, with_pool:bool, with_woodfloors:bool,with_patio:bool,with_clubhouse:bool,with_internet:bool, with_gated:bool):
                global __states
                '''
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
                print(state)
                '''
                x = np.zeros(27) #length X_Train
                model = joblib.load(os.path.join(MODEL_PATH, f'{state}_model.pkl'))
                city_encoder = joblib.load(os.path.join(CITYNAME_ENCODER_PATH, f'{state}_cityname_encoder.pkl'))
                pets_encoder = joblib.load(os.path.join(PETS_ENCODER_PATH, f'{state}_pets_encoder.pkl'))


                x[8] = city_encoder.transform([cityname])
                x[6] = pets_encoder.transform([pets_allowed])

                if category == True:
                    x[0] = 1

                else:

                    x[1] = 1

               # numerical data
                x[2] = bathrooms
                x[3] = bedrooms
                x[7] = square_feet

                if fee == 'Yes':
                    x[4] = 1

                else:
                    x[5] = 1


                if with_storage == True:
                    x[9] = 1

                else:

                    x[10] = 1



                if with_parking == True:
                    x[11] = 1

                else:

                    x[12] = 1



                if with_gym == True:
                    x[13] = 1

                else:

                    x[14] = 1



                if with_pool == True:
                    x[15] = 1

                else:

                    x[16] = 1



                if with_woodfloors == True:
                    x[17] = 1

                else:

                    x[18] = 1


                if with_patio == True:
                        x[19] = 1

                else:

                    x[20] = 1


                if with_clubhouse == True:
                    x[21] = 1

                else:

                    x[22] = 1


                if with_internet == True:
                    x[23] = 1

                else:

                    x[24] = 1


                if with_gated == True:
                    x[25] = 1

                else:

                    x[26] = 1

                  # make the prediction
                preds = model.predict((x).reshape(-1, 1).T)
                preds = preds[0]
                preds = np.round(preds)
                preds = preds.tolist()
                return preds


if __name__ == '__main__':
    #load_saved_artifacts()
    print("Starting Python Flask Server For Rent Prediction...")

    print(get_estimated_rent('CA','home', 1, 3, 'No', 'no pets'
                , 1000, 'Los Angeles', 'True', 'True'
                , 'True', 'False', 'False', 'True', 'False', 'True', 'False'))
    print(get_estimated_rent('MA','home', 1, 3, 'No', 'no pets'
                , 1000, 'Amherst', 'True', 'True'
                , 'True', 'False', 'False', 'True', 'False', 'True', 'False'))

