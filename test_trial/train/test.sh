#IMAGE NAME WITH TAG TO BE RUN
IMAGE_NAME_WITH_TAG=us.gcr.io/kubeflow-on-mnist/train:latest
#PARAMETERS TO RUN THE IMAGE
#path
P=gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csv
#Target Varaible Name
T=Purchased
#Hyper-parameters
#H=json.dumps({'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000],'max_features': ['auto', 'sqrt'],'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None],'min_samples_split': [2, 5, 10],'min_samples_leaf': [1, 2, 4],'bootstrap': [True, False]})
#Hyper Parameter Search Type
S=1

docker run -t ${IMAGE_NAME_WITH_TAG}  --path ${P} --target ${T} --search_type ${S} 
