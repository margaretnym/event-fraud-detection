from flask import Flask, request, render_template
from pymongo import MongoClient
import pandas as pd
import pickle
import json
from time import sleep
from sklearn.ensemble import GradientBoostingClassifier

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("login.html")

@app.route('/fraud')

def fraud():
    pandas_input = data_table.find({'fraud': 1}, {'name':1, '_id':0, 'venue_address':1})
    #{'name':1},{'venue_address':1}
    df = pd.DataFrame(list(pandas_input))
    # df = pd.concat([df.name, df.venue_address], axis=1)
    return df.to_html()


if __name__=="__main__":
    client = MongoClient()
    db = client['my_db']
    data_table = db['data']

    app.run(host='0.0.0.0', port = 5000, debug=True)
