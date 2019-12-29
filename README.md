![Dopamine](./docs/imgs/1920px-dopamine.png)

# Dopamine

Dopamine is a simple and fast Python web framework which aims to help you build an app agilely. It's based on gevent's `pywsgi`, a pure-Python, gevent-friendly WSGI server. Benefiting from a high-level synchronous API on top of the `libev` or `libuv` event loop, dopamine could be fast to respond every HTTP request without the user to do any extra work. Also, dopamine will stay in both easy-using and powerfuly to help you build some simple apps agilely.

## Feature

Dopamine hopes you can use it to build your app without any burden. Here are some features dopamine already has or soon will be supported.

* Simple router function
* JSON friendly
* Easy to handle HTTP requests
* Template framework support
* ...

## Example

```python
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
```

## LICENSE
Copyright © 2019 by JmPotato

Under [Apache License 2.0](http://www.apache.org/licenses/)
