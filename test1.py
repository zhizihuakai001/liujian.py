from wsgiref.simple_server import make_server

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 9090, app)
    server.serve_forever()