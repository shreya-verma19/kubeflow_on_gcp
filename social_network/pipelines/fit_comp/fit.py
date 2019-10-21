# Splitting the dataset into the Training set and Test set
import sys
import numpy as np
import json
import pandas as pd
print("arguments",sys.argv)

data = {'fpr':[0.01,0.19,0.58],
        'tpr':[0.56,0.78,0.91],
        'thresholds':[5,7,9]
        }
df_roc = pd.DataFrame(data)
with open('roc.csv', 'w') as f:
    df_roc.to_csv(f, columns=['fpr', 'tpr', 'thresholds'], header=False, index=False)

metadata = {
    'outputs': [{
      'type': 'roc',
      'format': 'csv',
      'schema': [
        {'name': 'fpr', 'type': 'NUMBER'},
        {'name': 'tpr', 'type': 'NUMBER'},
        {'name': 'thresholds', 'type': 'NUMBER'},
      ],
      'source': 'roc.csv'
    }]
  }
with open('/mlpipeline-ui-metadata.json', 'w') as f:
    json.dump(metadata, f)
