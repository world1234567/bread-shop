#  -*- coding: utf-8 -*-
from framework import app
from views import *


if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', port=8088, debug=True)
    app.run()