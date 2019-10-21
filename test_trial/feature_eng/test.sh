#IMAGE NAME WITH TAG TO BE RUN
IMAGE_NAME_WITH_TAG=us.gcr.io/kubeflow-on-mnist/feature_eng
#PARAMETERS TO RUN THE IMAGE
#path
P=gs://social_network-kubeflow-on-mnist/Social_Network_Ads.csv
#Filename
F=''
#Test Size
T=0.3

docker run -t ${IMAGE_NAME_WITH_TAG}  --path ${P} --filename ${F} --t_size ${T} 
