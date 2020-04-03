# pull official base image
FROM python:3.8.0-alpine

# pull official base image

COPY . /app

RUN PATH="$PATH"

WORKDIR /app
# set work directory
RUN pip3 install --upgrade pip
 
RUN pip3 install -r requirements.txt


CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]


