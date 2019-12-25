# -*- coding: utf-8 -*-
from gevent.pywsgi import WSGIServer


class Dopamine(WSGIServer):
    """A simple and fast Python web framework which aims to help you build an
    app agilely.
    """
    def __init__(self, listener=None):
        self.listener = ('127.0.0.1', 2995) if listener is None else listener
        WSGIServer.__init__(self, listener=self.listener,
                            application=self.application)

    def application(self, env, start_response):
        header = [
            ('Content-Type', 'text/html')
        ]
        if env['PATH_INFO'] == '/':
            start_response('200 OK', header)
            return [b"<h1>Hello, dopamine!</h1>"]

        start_response('404 Not Found', header)
        return [b'<h1>Not Found</h1>']

    def run(self):
        self.serve_forever()
