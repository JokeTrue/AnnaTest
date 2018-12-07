FROM python:3

COPY server.py /
COPY routes.py /
COPY views.py /
COPY requirements.txt /
COPY static /
COPY templates /

RUN pip install -r requirements.txt

CMD [ "python", "-u", "server.py" ]