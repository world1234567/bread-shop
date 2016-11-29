#  -*- coding: utf-8 -*-
from flask import Flask

from app.database import db_session
from app.main import main
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.teardown_request
    def shutdown_session(exception=None):
        db_session.remove()

    app.register_blueprint(main)

    #生产环境处理未知的异常
    if not app.debug:
        import logging
        from logging.handlers import RotatingFileHandler
        file_handler = RotatingFileHandler('logs/error.log', 'a', 1 * 1024 * 1024, 10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        app.logger.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.info('web startup')

    return app