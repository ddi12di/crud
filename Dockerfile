FROM python:3.13


WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

#CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5659" ]

