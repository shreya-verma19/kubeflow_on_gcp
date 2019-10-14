import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

with open("X.txt", "w") as output_file:
    output_file.write(np.array2string(X))
    print("Done X!")
with open("y.txt", "w") as output_file:
    output_file.write(np.array2string(y))
    print("Done y!")
 
