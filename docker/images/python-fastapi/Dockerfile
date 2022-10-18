FROM python:3.9

EXPOSE 8080

RUN pip install fastapi uvicorn[standard] sqlmodel mysqlclient passlib PyJWT

WORKDIR /home/fastapi

ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 8080
