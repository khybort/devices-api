FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update && apt-get -y dist-upgrade
RUN apt install -y netcat-traditional

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./main.py /app/main.py

ADD ./start.sh /app/start.sh

ENV PYTHONUNBUFFERED=1

RUN ["chmod", "+x", "/app/start.sh"]

ENTRYPOINT ["./start.sh"]
