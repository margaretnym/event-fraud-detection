from flask import Flask, request, render_template
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)


@app.route('/')

def index():
    return render_template("login.html")

@app.route('/fraud')

def fraud():
    #template we need to update
    connection = MongoClient()
    db = connection['test']
    collection = db['baseball']
    pandas_input = collection.find({'earned_run_avg': {'$exists': True}})
    df = pd.DataFrame(list(pandas_input))

    return df.to_html()


if __name__=="__main__":
    # all this says is start this app
    app.run(host='0.0.0.0', port = 5000, debug=True)
