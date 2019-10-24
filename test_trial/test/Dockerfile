FROM python:3.7.3-slim

WORKDIR /home/s_verma/test_trial/Testing/

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python","src/test.py"]
