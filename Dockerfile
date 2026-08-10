FROM python:3.10.8-slim
LABEL maintainer="spmspi"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /media/images

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /media/images
RUN chmod -R 755 /media/images

USER my_user