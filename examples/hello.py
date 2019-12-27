# -*- coding: utf-8 -*-
from dopamine import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))


@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine! Your host is {0}:{1}.'.format(
        request.remote_addr, request.remote_port)
    return html


app.run()
