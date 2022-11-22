from flask import Flask
from werkzeug.serving import make_server

import settings

app = Flask(__name__)
app.config.from_object(settings)


if __name__ == '__main__':
    server = make_server('0.0.0.0', 9090, app)
    server.serve_forever()
    app.run()