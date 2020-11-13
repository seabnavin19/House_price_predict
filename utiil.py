import json
import numpy as np
import pickle
__location=None
__re_location=None
__model=None
def save_data():
    global __location
    global __model
    global __re_location
    with open("./artifacts/col.json",'r') as f:
        __location=json.load(f)["data_columns"]
        __re_location=__location[3:]
    with open("./artifacts/models.pickle",'rb') as f:
         __model= pickle.load(f)


def location():
    return __re_location

def predict_price(location,size,total_sqft,bath):
    try:
        k = __location.index(location.lower())
    except:
        k = -1
    X = np.zeros(len(__location))
    X[0] = size
    X[1] = total_sqft
    X[2] = bath
    if k >= 0:
        X[k] = 1
    return __model.predict([X])[0]


if __name__=='utiil':
    save_data()


