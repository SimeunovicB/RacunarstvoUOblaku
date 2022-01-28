FROM python:3.8

WORKDIR /usr/src

RUN pip install --upgrade pip 
RUN apt update
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY /cloud_computing /usr/src/cloud_computing

CMD bash -c "cd cloud_computing &&  python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
