#IMAGE NAME WITH TAG TO BE RUN
IMAGE_NAME_WITH_TAG=us.gcr.io/kubeflow-on-mnist/deploy:latest
#PARAMETERS TO RUN THE IMAGE
#BUCKET NAME
B=social_network-deploy
#PROJECT NAME
P=kubeflow-on-mnist
#REGION OF MODEL DEPLOYMENT
R=us-central1-a
#URI OF PKL FILE
U=gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csvmodels/model.pkl
#FRAMEWORK
F=''
#VERSION BEGINING WORDS
V=''
#MODEL NAME
M=social_network

docker run -t ${IMAGE_NAME_WITH_TAG} ${B} ${P} ${R} ${U} ${F} ${V} ${M}  
