#IMAGE NAME WITH TAG TO BE RUN
IMAGE_NAME_WITH_TAG=us.gcr.io/kubeflow-on-mnist/test:latest
#PARAMETERS TO RUN THE IMAGE
#path
P=gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csv
#Target Varaible Name
T=Purchased

docker run -t ${IMAGE_NAME_WITH_TAG}  --path ${P} --target ${T}  
