# -*- coding: utf-8 -*-
from gevent import monkey, pywsgi

from .error import RouterException

monkey.patch_all()


class Dopamine(pywsgi.WSGIServer):
    """A simple and fast Python web framework which aims to help you build an
    app agilely.
    """

    def __init__(self, listener=None):
        self._router = {}
        self.listener = ('127.0.0.1', 2995) if listener is None else listener
        pywsgi.WSGIServer.__init__(self, listener=self.listener,
                                   application=self.application)

    def route(self, url, method_list):
        def decorator(f):
            # Check the url
            if isinstance(url, str) and len(url) > 0 and url[0] == '/':
                if len(url) > 1 and url[-1] == '/':
                    new_url = url[:-1]
                else:
                    new_url = url
            else:
                raise RouterException

            # Check the method list
            if isinstance(method_list, list):
                new_method_list = []
                for method in method_list:
                    if method in {'GET', 'HEAD', 'POST', 'PUT', 'DELETE',
                                  'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'}:
                        new_method_list.append(method)
            if not new_method_list:
                raise RouterException

            self._router[new_url] = (new_method_list, f)
            return f

        return decorator

    def application(self, env, start_response):
        header = [
            ('Content-Type', 'text/html')
        ]
        url_path = env['PATH_INFO']
        if len(url_path) > 1 and url_path[-1] == '/':
            url_path = url_path[:-1]
        if url_path in self._router:
            if env['REQUEST_METHOD'] in self._router[url_path][0]:
                start_response('200 OK', header)
                html = self._router[url_path][1](env)
            else:
                start_response('405 Method Not Allowed', header)
                html = b'Method Not Allowed'
        else:
            start_response('404 Not Found', header)
            html = b'Not Found'

        return [html]

    def run(self):
        self.serve_forever()
