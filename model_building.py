
import pandas as pd
import numpy as np
import cPickle as pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
# from sklearn.svm import SVC
# from sklearn.neighbors import KNeighborsClassifier

from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import cross_val_score
#from sklearn.metrics import confusion_matrix, recall_score, make_scorer, precision_score, f1_score, accuracy_score
from sklearn.model_selection import cross_val_score
#from sklearn.pipeline import Pipeline



def feature_engineering(file):
    
    df = pd.read_json(file)


    '''
    Index([u'acct_type', u'approx_payout_date', u'body_length', u'channels',
       u'country', u'currency', u'delivery_method', u'description',
       u'email_domain', u'event_created', u'event_end', u'event_published',
       u'event_start', u'fb_published', u'gts', u'has_analytics',
       u'has_header', u'has_logo', u'listed', u'name', u'name_length',
       u'num_order', u'num_payouts', u'object_id', u'org_desc',
       u'org_facebook', u'org_name', u'org_twitter', u'payee_name',
       u'payout_type', u'previous_payouts', u'sale_duration',
       u'sale_duration2', u'show_map', u'ticket_types', u'user_age',
       u'user_created', u'user_type', u'venue_address', u'venue_country',
       u'venue_latitude', u'venue_longitude', u'venue_name', u'venue_state'],
      dtype='object')
    '''

    df['fraud'] = df.acct_type.apply(lambda x: 0 if x =="premium" else 1)
    df['US/N'] = df.country.apply(lambda x: 1 if x =="US" else 0)
    df= pd.get_dummies(df , columns=['payout_type'])
    df['Twitter_presence'] = df.org_twitter.apply(lambda x: 1 if x > 0 else 0)
    df['Facebook_presence'] = df.org_facebook.apply(lambda x: 1 if x > 0 else 0)
    df['have_previous_payouts'] = df['previous_payouts'].apply(lambda x: 1 if len(x) != 0 else 0)
    df['cap_name'] = df['name'].apply(lambda x: 1 if x.isupper() == True else 0)
    df['sensible_age'] = df['user_age'].apply(lambda x: 1 if (x >= 15) and (x<= 80) else 0)
    df['maindomain_email'] = df['email_domain'].apply(lambda x: 1 if ('hotmail.com' in x) or ('gmail.com' in x) or ('yahoo.com' in x) else 0)

    X_col = df[['US/N', 'body_length', 'Twitter_presence','Facebook_presence', 'payout_type_',
             'payout_type_ACH', 'payout_type_CHECK', 'have_previous_payouts', \
            'show_map','sensible_age','cap_name', 'maindomain_email']]
    y_col = df['fraud']

    X = np.array(X_col)
    y = np.array(y_col)

    return X, y


def score_best_models(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)

    best_model = parameter_tuning(X,y)
    #methods =[LogisticRegression(), GradientBoostingClassifier(), RandomForestClassifier()] #SVC(), 
    model = best_model.fit(X_train, y_train)
    score = np.mean(cross_val_score(model, X, y ,cv=5))
    print best_model 
    print 'score: {}' .format(score)
    recall = np.mean(cross_val_score(model, X, y,cv=5, scoring='recall'))
    print 'recall: {}' .format(recall)
    precision = np.mean(cross_val_score(model, X, y,cv=5, scoring='precision'))
    print 'precision: {}' .format(recall)
    return best_model, score, recall, precision


def parameter_tuning(X,y):   
    param_grid = {'n_estimators':[10, 100, 1000],
                  'max_depth': [4, 6], 
                  'max_features': ['auto', 'sqrt', 'log2']}
    
    gb_model = GradientBoostingClassifier()
    gb_cv = GridSearchCV(gb_model, param_grid, n_jobs=-1,verbose=True, cv=3).fit(X,y)  
    
    rf_model = RandomForestClassifier()
    rf_cv = GridSearchCV(rf_model, param_grid, n_jobs=-1,verbose=True, cv=3).fit(X,y)  
    
    param_grid2 = {'penalty':['l1', 'l2']}
    
    log_model = LogisticRegression()
    log_cv = GridSearchCV(log_model, param_grid2, n_jobs=-1,verbose=True, cv=3).fit(X,y)  
               
               
    if (gb_cv.best_score_ > rf_cv.best_score_) and (gb_cv.best_score_ > log_cv.best_score_):
        return gb_cv.best_estimator_
    elif (rf_cv.best_estimator_ > gb_cv.best_score_) and (rf_cv.best_estimator_ > log_cv.best_score_):
        return rf_cv.best_estimator_
    else:
        return log_cv.best_estimator_

if __name__ == '__main__':

    file = 'files/data.json'
    X,y = feature_engineering(file)
    best_model, score, recall, precision = score_best_models(X,y)
    with open('files/model.pkl', 'wb') as f:
        pickle.dump(best_model, f)



