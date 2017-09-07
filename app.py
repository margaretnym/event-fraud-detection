from flask import Flask, render_template, request, jsonify
import pickle
from build_model import TextClassifier
from pymongo import MongoClient
from predict import

app = Flask(__name__)

##all of Chris's code would go here

if __name__ == '__main__':
    with open('data/model.pkl') as f:
        model = pickle.load(f)
    client = MongoClient()
    db = clinet['my_db']
    app.run(host='0.0.0.0', debug=True)
