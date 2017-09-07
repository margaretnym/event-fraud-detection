from flask import Flask, render_template, request, jsonify
import pickle
import sleep
from build_model import TextClassifier
from pymongo import MongoClient
from sklearn.ensemble import GradientBoostingClassifier
from predict import prepare_data, predict_fraud, request_data_point, check_duplicate, generate_hash

app = Flask(__name__)

##all of Chris's code would go here

if __name__ == '__main__':
    with open('data/model.pkl') as f:
        model = pickle.load(f)

    client = MongoClient()
    db = client['my_db']
    hash_table = db['hashes']
    data_table = db['data']

    while True:
        sleep(10)
        new_data = request_data_point()
        data_hash = generate_hash(new_data)
        if check_duplicate(data_hash, 'data_hash' hash_table) == False:
            hash_table.insert_one({'data_hash' : data_hash})
            new_data = json.loads(new_data)
            prediction = predict_fraud(X)
            new_data['fraud'] = prediction
            data_table.insert_one(new_data)
            
    app.run(host='0.0.0.0', debug=True)
