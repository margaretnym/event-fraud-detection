# Event Fraud Detection Case Study

A machine learning web application to predict fraud events on realtime data streams. Compared the performance of Logistic Regression, Random Forest and GradientBoasting Classifier Algorithms by fine tuning the model to have the highest score accuracy. GradientBoasting Classifier made up the final model with score 93% and precision 

Due to confidentiality, the training data is not made public. The python code is made available in the src file. The model is also available as a pickle file.

Team:+1::+1::+1:: Alexandra Magana Noronha, Margaret Ng, Christopher Sankat

## Files Desciption
model_building.py - Set up training data and compares the performance of models and stores the best model in pickle format
predit.py


## Library Used
Numpy
Pandas
Sklearn
Flask
Jinja
cPickle


## Feature Picked up & its importance

Features Picked | Feature Importance
------------ | -------------
body_length|                  |0.382260768935
have_previous_payouts||0.212499442992
payout_type_|NAN for payout_type|0.0808801964102
maindomain_email|If the email domain from 'hotmail.com', 'gmail.com', or'yahoo.com'            |0.0601378041721
Facebook_presence|            |0.049203266724
show_map|                     |0.0453565490356
US/N|if the country is US or not|0.0374902063586
Twitter_presence|             |0.0358097072891
sensible_age|user age within range 15-80                 |0.0329840909997
payout_type_CHECK|Check for payout_type             |0.0239138354847
cap_name|If name is all in captial case                     |0.0200757693587
payout_type_ACH|              |0.0193883622403
