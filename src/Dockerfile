FROM python:3.8

ENV PYTHONBUFFERED=1
ENV WEBAPP_DIR=/src

RUN mkdir -p /var/log/gunicorn
RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR

COPY ./requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR