FROM python:3.7

ENV PORT 8081

ENV PORT_CS 11211

COPY ./requirements.txt /app/requirements.txt

COPY ./app/app.py /app/app.py

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]