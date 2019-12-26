![A pic of dopamine](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Dopamine2.svg/1920px-Dopamine2.svg.png)

# Dopamine

A simple and fast Python web framework which aims to help you build an app agilely.

# Example

```python
from dopamine import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))

@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine! Your address is {0}:{1}'.format(
        request['REMOTE_ADDR'], request['REMOTE_PORT'])
    return html

app.run()
```

# LICENSE
Copyright © 2019 by JmPotato

Under [Apache License 2.0](http://www.apache.org/licenses/)
