# -*- coding: utf-8 -*-
from dopamine import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))


@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine! Your address is {0}:{1}'.format(
        request['REMOTE_ADDR'], request['REMOTE_PORT'])
    return html


app.run()
