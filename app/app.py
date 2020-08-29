import os
from flask import Flask
from pymemcache.client.base import Client

app = Flask(__name__)
host = '0.0.0.0'
port = int(os.environ.get("PORT", 8081))


def json_serializer(key, value):
    if type(value) == str:
        return value, 1
    return json.dumps(value), 2

def json_deserializer(key, value, flags):
   if flags == 1:
       return value.decode("utf-8")
   if flags == 2:
       return json.loads(value.decode("utf-8"))

def get_fibo(number):
    if (number == 0) or (number == 1):
        return number
    return get_fibo(number - 1) + get_fibo(number - 2)

client = Client(('memcached', 11211), serializer=json_serializer, deserializer=json_deserializer)


@app.route("/<int:param_fi>/")
def get_fibonacci(param_fi):
    return str(get_fibo(param_fi))


if __name__ == '__main__':
    app.run(debug=False, host=host, port=port)

