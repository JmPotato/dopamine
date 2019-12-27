# -*- coding: utf-8 -*-
class DopamineException(Exception):
    def __init__(self, *args, **kwargs):
        super(DopamineException, self).__init__()


class RouterException(DopamineException):
    def __init__(self, *args, **kwargs):
        super(DopamineException, self).__init__()


class HTTPException(Exception):
    """For HTTP exceptions.
    """

    code = None
    status = None
    description = None

    def __init__(self, description=None, response=None):
        super(HTTPException, self).__init__()
        if description is not None:
            self.description = description
        self.response = response


class NotFound(HTTPException):
    """*404* `Not Found`
    Raise if a resource does not exist and never existed.
    """

    code = 404
    status = '404 Not Found'
    description = (
        "The requested URL was not found on the server. If you entered"
        " the URL manually please check your spelling and try again."
    )


class MethodNotAllowed(HTTPException):
    """*405* `Method Not Allowed`
    Raise if the server used a method the resource does not handle.  For
    example `POST` if the resource is view only.  Especially useful for REST.
    The first argument for this exception should be a list of allowed methods.
    Strictly speaking the response would be invalid if you don't provide valid
    methods in the header which you can do with that list.
    """

    code = 405
    status = '405 Method Not Allowed'
    description = "The method is not allowed for the requested URL."
