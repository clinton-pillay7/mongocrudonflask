FROM python:3.10.6

WORKDIR /app

COPY . . 

RUN pip3 install -r requirements.txt

cmd gunicorn --bind 0.0.0.0:5000 wsgi:app 
