FROM ubuntu:16.04

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

RUN apt-get -y install redis-server

RUN pip install redis

ADD requirements.txt /

ADD templates /templates

ADD index.py /

ADD docker-compose.yml /

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python"]

CMD ["index.py"]
