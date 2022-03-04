FROM python:3-alpine3.10 as builder

WORKDIR /app/service/
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM builder

WORKDIR /app/service/
COPY . .
VOLUME /app/service/

EXPOSE 8000
