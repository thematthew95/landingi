FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code && pip3 install django==2.2.12
WORKDIR /code
COPY ./BackendN /code/
ENTRYPOINT ["python3", "./manage.py", "runserver", "0.0.0.0:8080"]
