IMAGE_PATH=us.gcr.io/kubeflow-on-mnist/feature_eng
docker build -t $IMAGE_PATH -f Dockerfile .
docker push $IMAGE_PATH


