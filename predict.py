import pandas as pd
import numpy as np
import requests

def prepare_data(new_data):
    clean_data = {}
    X_col = ['US/N', 'body_length', 'Twitter_presence','Facebook_presence', 'payout_type_',
             'payout_type_ACH', 'payout_type_CHECK', 'have_previous_payouts', \
            'show_map','sensible_age','cap_name', 'maindomain_email']
    clean_data['body_length'] = new_data['body_length']
    clean_data['show_map'] = new_data['show_map']
    clean_data['payout_type_'] = 1 if new_data['payout_type']  == '' else 0
    clean_data['payout_type_ACH'] = 1 if new_data['payout_type']  == 'ACH' else 0
    clean_data['payout_type_CHECK'] = 1 if new_data['payout_type']  == 'CHECK' else 0
    clean_data['US/N'] = 1 if new_data['country'] == "US" else 0
    clean_data['Twitter_presence'] = 1 if new_data['org_twitter'] > 0 else 0
    clean_data['Facebook_presence'] = 1 if new_data['org_facebook'] > 0 else 0
    clean_data['have_previous_payouts'] = 1 if len(new_data['previous_payouts']) != 0 else 0
    clean_data['cap_name'] = 1 if new_data['name'].isupper() == True else 0
    clean_data['sensible_age'] = 1 if (new_data['user_age'] >= 15) and (new_data['user_age']<= 80) else 0
    clean_data['maindomain_email'] = 1 if ('hotmail.com' in new_data['email_domain']) or ('gmail.com' in new_data['email_domain']) or ('yahoo.com' in new_data['email_domain']) else 0
    X = np.array([])
    for col in X_col:
        X = np.append(X, clean_data[col])
    return X

def predict_fraud(new_data, model):
    X = prepare_data(new_data)
    return model.predict(X)


def request_data_point():
    """GET request to herokuapp that supplies a new
    unscored datapoint, parses as json"""
    return requests.get('http://galvanize-case-study-on-fraud.herokuapp.com/data_point').content


def check_duplicate(data, key, table):
    """Query the database to see if the observation
    has alreayd been seen and scored"""
    return table.find({key : data}).count() > 0
