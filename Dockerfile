FROM alpine:latest

MAINTAINER Sion Smith (https://github.com/sionsmith)

RUN apk add --update python3 py3-pip

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip3 install py3dns validate-email

ENTRYPOINT ["python3", "knock.py"]

CMD ["--help"]