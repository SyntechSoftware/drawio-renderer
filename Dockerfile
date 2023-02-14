FROM python:3.11-slim-bullseye

ENV DISPLAY :0

WORKDIR /app

RUN apt update && apt install -y wget libsecret-1-0 libatspi2.0-0 xdg-utils libxss1 libnss3 libnotify4 libgtk-3-0 libgbm-dev libasound2 xvfb

RUN wget https://github.com/jgraph/drawio-desktop/releases/download/v20.8.16/drawio-amd64-20.8.16.deb -O /tmp/drawio.deb
RUN dpkg -i /tmp/drawio.deb

COPY requirements.txt .
RUN pip install -r requirements.txt
