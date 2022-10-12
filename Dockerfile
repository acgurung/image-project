# syntax=docker/dockerfile:1
# points to latest release of version 1 syntax

FROM python:3.10.7-slim-buster

WORKDIR /docker-app

# copy our requirements.txt into the image
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 

# copy source code into the image
COPY . . 

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]