FROM python:3.6-alpine

MAINTAINER gregkoul@gmail.com

RUN pip install flask

COPY . /opt/

EXPOSE 8000

WORKDIR /opt

ENTRYPOINT ["python"]

CMD ["app.py"]
