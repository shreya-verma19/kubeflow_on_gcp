# Splitting the dataset into the Training set and Test set
import numpy as np
import argparse
if __name__ == '__main__':
  try:
    print("An exception occurred")  
    parser = argparse.ArgumentParser()
    parser.add_argument('--X',
                      type=str,
                      required=True,
                      help='The GCP project to run the dataflow job.')
    parser.add_argument('--y',
                      type=str,
                      required=True,
                      help='Bucket to store outputs.')
    args = parser.parse_args()
  except Exception as detail:
    print('Handling run-time error:', detail)
"""      
from sklearn.model_selection import train_test_split
X_args=args.X.strip()
print(args.X)
print(args.y)

with open("output.txt", "w") as output_file:
    output_file.write(X_args)
    print("Done X args!")

X_train, X_test, y_train, y_test = train_test_split(np.fromstring(args.X.strip()), np.fromstring(args.y.strip()), test_size = 0.25, random_state = 0)
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
"""