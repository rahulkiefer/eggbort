FROM ubuntu:latest

RUN apt update && \
    apt upgrade -y && \
    apt install -y git && \
    apt install -y python3-pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install --no-cache-dir -U git+https://github.com/Rapptz/discord-ext-menus.git

COPY . .

CMD [ "python3", "./launcher.py" ]