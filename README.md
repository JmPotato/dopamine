![Dopamine](https://github.com/JmPotato/dopamine/blob/master/docs/imgs/1920px-dopamine.png)

# Dopamine

A simple and fast Python web framework which aims to help you build an app agilely.

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
