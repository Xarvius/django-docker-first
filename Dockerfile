FROM python:3

ADD requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install psycopg2
ADD . /app/

CMD python mysite/manage.py migrate && python mysite/manage.py runserver 0.0.0.0:8000

