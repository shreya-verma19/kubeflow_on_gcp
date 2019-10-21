FROM google/cloud-sdk:latest

WORKDIR /home/s_verma1904/test_trial/deploy 

COPY deploy-social.json /home/s_verma1904/test_trial/deploy

COPY . .

ENTRYPOINT ["bash","src/deployment.sh"]
