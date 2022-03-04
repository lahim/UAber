# Code4Ukraine:UAber app

## Pre-installed

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Install

Below you can find a simple guide how to install all required python dependencies:

### Create & activate virtualenv

```bash
python3 -m venv venv
. venv/bin/active
```

### Install Python dependencies

```bash
pip install -U pip wheel pip-tools
pip install -r requirements.txt
```

### Run MongoDB

```bash
mkdir -p bin/data/db
docker-compose up mongodb
```

### Run UAber API

```bash
cd uaber-api
uvicorn main:app --reload
```

### Run UAber API & MongoDB from Docker

```bash
docker-compose up --build
```
