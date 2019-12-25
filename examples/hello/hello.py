# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from dopamine.app import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))


@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine! Your address is {0}:{1}'.format(
        request['REMOTE_ADDR'], request['REMOTE_PORT'])
    return bytes(html, 'utf-8')


app.run()
