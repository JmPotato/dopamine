# -*- coding: utf-8 -*-


class Response(object):
    """Response is a wrapper for WSGI response data.
    """
    default_charset = 'utf-8'
    default_status = '200 OK'
    default_content_type = 'text/plain'

    def __init__(self, headers=None, body=None, status=None, content_type=None):
        self.charset = self.default_charset
        # Init headers
        if isinstance(headers, ResponseHeaders):
            self.headers = headers
        elif headers is None:
            self.headers = ResponseHeaders()
        else:
            self.headers = ResponseHeaders(headers)
        # Init response body
        if isinstance(body, (str, bytes, bytearray)):
            self.set_body(body)
        # Init status des & code
        self.status = '200 OK' if status is None else status
        # Init Content-Type
        if content_type is None and "Content-Type" not in self.headers:
            content_type = self.default_content_type
        if content_type is not None:
            self.headers["Content-Type"] = content_type

    def set_body(self, body_data):
        if isinstance(body_data, str):
            body = body_data.encode(self.charset)
        else:
            body = bytes(body_data, self.charset)
        self._body = [body]
        self.headers["Content-Length"] = str(len(body))

    def get_body(self, need_bytes=True):
        body_data = self._body[0]
        if isinstance(body_data, bytes) and not need_bytes:
            body_data = body_data.decode(self.charset)
        return body_data

    body = property(get_body, set_body)


class ResponseHeaders(object):
    """Response is a wrapper for WSGI response headers.
    """

    def __init__(self, defaults=None):
        self.__list = []
        if defaults is not None and isinstance(
                defaults, (list, ResponseHeaders)):
            self.__list.extend(defaults)
        else:
            self.extend(defaults)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__list[key]
        elif isinstance(key, slice):
            return self.__class__(self.__list[key])
        key = key.lower()
        for k, v in self.__list:
            if k.lower() == key:
                return v

    def __setitem__(self, key, value):
        if not self.__list:
            self.__list.append((key, value))
            return
        listiter = iter(self.__list)
        key = key.lower()
        for index, (old_key, old_value) in enumerate(listiter):
            if old_key.lower() == key:
                self.__list[index] = (key, value)
                break
        else:
            self.__list.append((key, value))
            return
        self.__list[index + 1:] = [t for t in listiter if t[0].lower() != key]

    def extend(self, *args, **kwargs):
        if len(args) <= 1 and args:
            pass

    def get_list(self):
        return self.__list
