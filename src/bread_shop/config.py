import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'abcd0123'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    __SQL_PARAMS = {
        'passwd': 'a123456',
        'host': '127.0.0.1',
        'db': 'mytest',
        'port': 3306,
        'user': 'root',
    }
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s:%s/%s" % ( __SQL_PARAMS['user'], __SQL_PARAMS['passwd'], __SQL_PARAMS['host'], __SQL_PARAMS['port'], __SQL_PARAMS['db'])

    DEBUG = True


class TestingConfig(Config):
    TESTING=True
    pass

class ProductionConfig(Config):
    
    pass


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
