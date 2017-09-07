import os
from predict import prepare_data, predict_fraud, request_data_point, check_duplicate
from pymongo import MongoClient
import pandas as pd
import pickle
import json
from time import sleep
from sklearn.ensemble import GradientBoostingClassifier

def run_all():
    with open('model.pkl') as f:
        model = pickle.load(f)

    client = MongoClient()
    db = client['my_db']
    hash_table = db['hashes']
    data_table = db['data']

    while True:
        sleep(10)
        new_data = request_data_point()
        data_hash = hash(new_data)
        is_duplicate = check_duplicate(data_hash, 'data_hash', hash_table)
        if is_duplicate == False:
            hash_table.insert_one({'data_hash' : data_hash})
            new_data = json.loads(new_data)
            prediction = predict_fraud(new_data, model)
            new_data['fraud'] = prediction[0]
            print new_data
            data_table.insert_one(new_data)


if __name__ == "__main__":
    os.system('python fraud_flask.py &')
    run_all()
