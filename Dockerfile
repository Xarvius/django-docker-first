FROM python:3

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install psycopg2
#RUN
#RUN
#RUN

CMD python mysite/manage.py runserver 0.0.0.0:8000
