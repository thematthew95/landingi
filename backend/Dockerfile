FROM python:3.9-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./backend.py /code/
ENTRYPOINT ["python3", "backend.py"]
