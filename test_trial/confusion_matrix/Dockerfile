FROM python:3.7.3-slim

WORKDIR /home/s_verma1904/test_trial/cm/

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python","src/confusion_matrix.py"]