![Dopamine](https://github.com/JmPotato/dopamine/blob/master/docs/imgs/1920px-dopamine.png)

# Dopamine

A simple and fast Python web framework which aims to help you build an app agilely.

## Example

```python
# -*- coding: utf-8 -*-
from dopamine import Dopamine

app = Dopamine(listener=('127.0.0.1', 5299))

@app.route('/', ['GET'])
def hello(request):
    html = 'Hello, dopamine! Your host is {0}:{1}.'.format(
        request.remote_addr, request.remote_port)
    return html

app.run()
```

## LICENSE
Copyright © 2019 by JmPotato

Under [Apache License 2.0](http://www.apache.org/licenses/)
