# -*- coding: utf-8 -*-
from gevent import monkey, pywsgi

from .request import Request
from .response import Response

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

    def __str__(self):
        return "<class 'DopamineObeject'>"

    def __repr__(self):
        return 'DopamineObeject'

    def route(self, url, method_list):
        def decorator(f):
            # Check the url
            if isinstance(url, str) and len(url) > 0 and url[0] == '/':
                if len(url) > 1 and url[-1] == '/':
                    new_url = url[:-1]
                else:
                    new_url = url
            else:
                from .exceptions import RouterException
                raise RouterException(
                    "Illeage URL '{0}' for handler '{1}'"
                    .format(url, f.__name__))

            # Check the method list
            if isinstance(method_list, list):
                new_method_list = []
                unknown_method_list = []
                for method in method_list:
                    if isinstance(method, str) and \
                        method.upper() in {'GET', 'HEAD', 'POST', 'PUT',
                                           'DELETE', 'CONNECT', 'OPTIONS',
                                           'TRACE', 'PATCH'}:
                        new_method_list.append(method.upper())
                    else:
                        unknown_method_list.append(method)
            if not new_method_list:
                if not unknown_method_list:
                    new_method_list = ['GET']
                else:
                    from .exceptions import RouterException
                    raise RouterException(
                        "Unsupported HTTP method '{0}'"
                        .format(unknown_method_list[0]))

            self._router[new_url] = (new_method_list, f)
            return f

        return decorator

    def application(self, env, start_response):
        request = Request(env)
        response = Response(content_type='text/html')
        if request.path in self._router:
            if request.method in self._router[request.path][0]:
                response.body = self._router[request.path][1](
                    request, response)
                start_response(response.status, response.headers)
            else:
                from .exceptions import MethodNotAllowed
                response.status = MethodNotAllowed.status
                start_response(response.status, response.headers)
                response.body = MethodNotAllowed.description
        else:
            from .exceptions import NotFound
            response.status = NotFound.status
            response.body = NotFound.description
            start_response(response.status, response.headers)

        return [response.body]

    def run(self):
        self.serve_forever()
