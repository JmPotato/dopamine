# -*- coding: utf-8 -*-
import io
import re

from setuptools import setup

with io.open("dopamine/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name='dopamine',
    version=version,
    keywords=['web', 'framework', 'wsgi', 'http', 'gevent'],
    description='A simple and fast Python web framework which aims to help you build an app agilely',
    author='JmPotato',
    author_email='ghzpotato@gmail.com',
    license='Apache',
    url='https://ipotato.me',
    packages=['dopamine'],
    install_requires=[
        'gevent'
    ],
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        'Topic :: Software Development :: Build Tools',
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ]
)
