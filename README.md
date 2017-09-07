# Event Fraud Detection Case Study

A machine learning web application :rainbow: to predict fraud events on realtime data streams. Compared the performance of Logistic Regression, Random Forest and GradientBoasting Classifier Algorithms by fine tuning the model to have the highest score accuracy. GradientBoasting Classifier made up the final model with a score .93 and precision .56.

Due to confidentiality, the training data is not made public. The python code is made available in the src file. The model is also available as a pickle file.

Team:+1::+1::+1:: Alexandra Magana Noronha:cake:, Margaret Ng:icecream:, Christopher Sankat:pizza:


## Main Infrastructure
- MongoDB
- Flask
- AWS

## Library Used
- Numpy
- Pandas
- Sklearn
- Jinja
- cPickle
- pymongo
- flask

## Diagram of all pieces + connections
![App Architecture](https://github.com/margaretnym/event-fraud-detection/blob/master/images/fraud_detection.png)

## Feature Picked up & its importance

Features Picked | Description |Feature Importance
------------ | ------------- | -------------
body_length|                  |0.38
have_previous_payouts||0.21
payout_type_|NAN for payout_type|0.08
maindomain_email|If the email domain from 'hotmail.com', 'gmail.com', or 'yahoo.com'|0.06
Facebook_presence|            |0.05
show_map|                     |0.05
US/N|If the country is US or not|0.04
Twitter_presence|             |0.04
sensible_age|User age is within the range 15-80                 |0.03
payout_type_CHECK|Check for payout_type             |0.02
cap_name|If name is all in captial case                     |0.02
payout_type_ACH|ACH for payout_type              |0.02


## Model picked
```python
GradientBoostingClassifier(criterion='friedman_mse', init=None,
               learning_rate=0.1, loss='deviance', max_depth=4,
               max_features='log2', max_leaf_nodes=None,
               min_impurity_split=1e-07, min_samples_leaf=1,
               min_samples_split=2, min_weight_fraction_leaf=0.0,
               n_estimators=100, presort='auto', random_state=None,
               subsample=1.0, verbose=0, warm_start=False)
```
## Web-Application Instructions

1. Enter http://52.89.86.85:5000/ into your web browser. You will be prompted to the screen below. 

![App Architecture](https://github.com/margaretnym/event-fraud-detection/blob/master/images/Screen%20Shot%202017-09-07%20at%204.17.48%20PM.png)

2. Enter username and password to access the Fraud Application. 

3. Conduct Investigation. 

![App Architecture](https://github.com/margaretnym/event-fraud-detection/blob/master/images/Screen%20Shot%202017-09-07%20at%204.10.02%20PM.png)

## Special Thanks

This project would not be possible without the efforts of Chris Wirgler and Dan Rupp.
