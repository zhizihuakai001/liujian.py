from gevent import pywsgi

from liujian import app

if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0',9090), app)
    server.serve_forever()