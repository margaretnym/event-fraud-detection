# Event Fraud Detection Case Study

A machine learning web application to predict fraud events on realtime data streams. Compared the performance of Logistic Regression, Random Forest and GradientBoasting Classifier Algorithms by fine tuning the model to have the highest score accuracy. GradientBoasting Classifier made up the final model with score 93% and precision 

Due to confidentiality, the training data is not made public. The python code is made available in the src file. The model is also available as a pickle file.

Team: Alexandra Magana Noronha, Margaret Ng, Christopher Sankat

## Files Desciption
model_building.py - Set up training data and compares the performance of models and stores the best model in pickle format
predit.py


## Library Used
numpy
pandas
skilearn
Flask

## Feature Picked up & its importance

- body_length                  0.382260768935
- have_previous_payouts        0.212499442992
- payout_type_                 0.0808801964102
- maindomain_email             0.0601378041721
- Facebook_presence            0.049203266724
- show_map                     0.0453565490356
- US/N                         0.0374902063586
- Twitter_presence             0.0358097072891
- sensible_age                 0.0329840909997
- payout_type_CHECK            0.0239138354847
- cap_name                     0.0200757693587
- payout_type_ACH              0.0193883622403
