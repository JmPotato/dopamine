# -*- coding: utf-8 -*-
import sys
sys.path.append('../..')

from dopamine import app

if __name__ == '__main__':
    dopamine_app = app.Dopamine(listener=('127.0.0.1', 5299))
    dopamine_app.run()
