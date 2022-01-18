FROM python:3.8

WORKDIR /usr/src/app

RUN pip install --upgrade pip 
RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY cloud_computing/ .

CMD python manage.py migrate & python manage.py runserver 0.0.0.0:8000
