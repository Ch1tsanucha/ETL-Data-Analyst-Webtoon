FROM python:3.10
WORKDIR /app
COPY extract.py /app
COPY transform.py /app
COPY load.py /app
COPY test_delete.py /app
COPY concat.py /app
COPY requirements.txt /requirements.txt
COPY .env /app

RUN pip install --upgrade pip --trusted-host pypi.python.org -r /requirements.txt 

RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb &&\
    rm google-chrome-stable_current_amd64.deb &&\
    apt-get clean

RUN apt-get install -y vim