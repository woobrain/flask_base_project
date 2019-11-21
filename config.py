import redis


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@192.168.179.131:3306/test_01'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = '192.168.179.131'
    REDIS_PORT = '6379'

    SECRET_KEY = 'woobrainaiyaoyaohahayibeizi'
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400

    DEBUG = True

class DevelopementConfig(Config):
    """开发模式下的配置"""
    DEBUG = True


class ProductionConfig(Config):
    """生产模式下的配置"""
    pass


config = {
    'config':Config,
    "development": DevelopementConfig,
    "production": ProductionConfig
}