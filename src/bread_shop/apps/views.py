#  -*- coding: utf-8 -*-
from framework import app


@app.route('/')
def hello_world():
    return 'Hello World!'