# -*- coding: utf-8 -*-


class Request(object):
    """Request is a wrapper for WSGI request data.
    """

    def __init__(self, env):
        self.__env = env

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError(key)
        key = key.replace("-", "_")
        if key in dir(self):
            return self.__getattribute__(key)
        key = key.upper()
        if key in self.__env:
            return self.__env[key]

    @property
    def path(self):
        url_path = self.__env.get('PATH_INFO')
        if len(url_path) > 1 and url_path[-1] == '/':
            url_path = url_path[:-1]
        return url_path

    @property
    def method(self):
        return self.__env.get('REQUEST_METHOD')

    @property
    def remote_addr(self):
        return self.__env.get('REMOTE_ADDR')

    @property
    def remote_port(self):
        return self.__env.get('REMOTE_PORT')

    @property
    def headers(self):
        return RequestHeaders(self.__env)


class RequestHeaders(object):
    """RequestHeaders is a wrapper for WSGI request headers.
    """

    def __init__(self, env):
        self.__env = env

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError(key)
        key = key.upper().replace("-", "_")
        if key in ("CONTENT_TYPE", "CONTENT_LENGTH"):
            return self.__env[key]
        return self.__env["HTTP_" + key]
