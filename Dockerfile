FROM alpine

RUN apk --update add nano supervisor python3 redis

ADD /django_app /src/django_app

ADD /supervisor /src/supervisor

RUN pip3 install -r /src/django_app/requirements.txt

EXPOSE 8000

WORKDIR /src/django_app

CMD ["supervisord","-c","/src/supervisor/service_script.conf"]