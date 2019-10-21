# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# A program to generate confusion matrix data out of prediction results.
# Usage:
# python confusion_matrix.py  \
#   --predictions=gs://bradley-playground/sfpd/predictions/part-* \
#   --output=gs://bradley-playground/sfpd/cm/ \
#   --target=resolution \
#   --analysis=gs://bradley-playground/sfpd/analysis \


from sklearn.metrics import confusion_matrix, accuracy_score
import json
import pandas as pd
def main(argv=None):
    cm_file = "gs://social_network-kubeflow-on-mnist/sample_confusion_matrix.csv"
    data = {'fpr':[0.01,0.19,0.58],
            'tpr':[0.56,0.78,0.91],
            'thresholds':[5,7,9]
        }
    df_roc = pd.DataFrame(data) 
    with open('roc.csv', 'w') as f:
        df_roc.to_csv(f, columns=['fpr', 'tpr', 'thresholds'], header=False, index=False)
    f = open('roc.csv', "r")
    print(f.read())
    metadata = {
        'outputs': [
            {
              'type': 'web-app',
              'storage': 'gcs',
              'source': 'gs://social_network-kubeflow-on-mnist/sample_HTML.html',
            },
            {
                'storage': 'inline',
                'source': '# Inline Markdown\n[A link](https://www.kubeflow.org/)',
                'type': 'markdown',
            },
            {
                'type': 'confusion_matrix',
                'format': 'csv',
                'schema': [
                            {'name': 'target', 'type': 'NUMBER'},
                            {'name': 'predicted', 'type': 'NUMBER'},
                            {'name': 'count', 'type': 'NUMBER'},
                          ],
                "labels": "vocab",
                "source": cm_file
             }
        ]
     }
 
    with open('/mlpipeline-ui-metadata.json', 'w') as f:
        json.dump(metadata, f)
    f = open("/mlpipeline-ui-metadata.json", "r")
    print(f.read())
   
    
if __name__== "__main__":
        main()
