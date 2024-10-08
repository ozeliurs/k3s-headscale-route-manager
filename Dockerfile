FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py /app/main.py

ENTRYPOINT [ "python", "main.py"]
