# -*- coding: utf-8 -*-


class Request(object):
    """Request is a wrapper for WSGI request data.
    """

    def __init__(self, env):
        self.env = env

    @property
    def path(self):
        url_path = self.env.get('PATH_INFO')
        if len(url_path) > 1 and url_path[-1] == '/':
            url_path = url_path[:-1]
        return url_path

    @property
    def method(self):
        return self.env.get('REQUEST_METHOD')

    @property
    def remote_addr(self):
        return self.env.get('REMOTE_ADDR')

    @property
    def remote_port(self):
        return self.env.get('REMOTE_PORT')

    @property
    def headers(self):
        return RequestHeaders(self.env)


class RequestHeaders(object):
    """RequestHeaders is a wrapper for WSGI request headers.
    """

    def __init__(self, env):
        self.env = env

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError(key)
        key = key.upper().replace("-", "_")
        if key in ("CONTENT_TYPE", "CONTENT_LENGTH"):
            return self.env[key]
        return self.env["HTTP_" + key]
