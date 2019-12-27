# -*- coding: utf-8 -*-
from dopamine import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))


@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine!<br>'
    html += 'Your host is {0}:{1}<br>'.format(
        request.remote_addr, request.remote_port)
    html += 'Your user agent is: {0}'.format(
        request.headers['User-Agent'])
    return html


app.run()
