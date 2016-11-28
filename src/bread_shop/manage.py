#  -*- coding: utf-8 -*-
import os
from app import create_app


if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
    app.run()