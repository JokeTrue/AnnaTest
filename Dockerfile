FROM python:3

RUN mkdir /anna-server
WORKDIR /anna-server

ADD . /anna-server/
RUN pip install -r requirements.txt

CMD [ "python", "-u", "server.py" ]