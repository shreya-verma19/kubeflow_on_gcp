IMAGE_PATH=us.gcr.io/kubeflow-on-mnist/cm
docker build -t $IMAGE_PATH -f Dockerfile .
