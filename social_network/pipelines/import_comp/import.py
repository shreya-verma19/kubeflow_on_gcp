import numpy as np
import pandas as pd
import json
# Importing the dataset
dataset = pd.read_csv('gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

with open("X.txt", "w") as output_file:
    output_file.write("Print X")
    print("Done X!")
with open("y.txt", "w") as output_file:
    output_file.write("Print y")
    print("Done y!")
metadata = {
    'outputs' : [
    # Markdown that is hardcoded inline
    {
      'storage': 'inline',
      'source': '# Inline Markdown\n[A link](https://www.kubeflow.org/)',
      'type': 'markdown',
    }]}
with open('mlpipeline-ui-metadata.json', 'w') as f:
    json.dump(metadata, f)