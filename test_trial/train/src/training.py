
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import logging
import argparse
import gcsfs
import json
import ast
import pickle

    
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser(description='Traiining the Model on data')
    parser.add_argument('--path', type=str, help='Local or GCS path to the training file')
    parser.add_argument('--target', type=str, help='Dependent varaible name.')
    parser.add_argument('--search_type', type=int, default=1, help='Type of hyper-parameter search: Grid ->1, Random->2')
    
    args = parser.parse_args()
    train=pd.read_csv(args.path+'outputs/train.csv')
    test=pd.read_csv(args.path+'outputs/test.csv')

    target=args.target

    # Feature Scaling
    sc = StandardScaler()
    X_train=train.drop(target,axis=1)
    y_train=np.ravel(train[[target]])

    X_test=test.drop(target,axis=1)

    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
        
    model = LogisticRegression(random_state = 0)
    model.fit(X_train, y_train)

    fs = gcsfs.GCSFileSystem()
    pickle.dump(model,fs.open((args.path+'models/model.pkl'),'wb'))