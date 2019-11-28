class Config():
    # STATIC_ID = 'http://129.28.206.139:80/static/'
    STATIC_ID = 'http://127.0.0.1:5000/static/'
    IGNORE_URLS = ['/api/v1/member/login',
                   '/api/v1/member/cklogin',
                   '/api/v1/food/search',
                   '/api/v1/food/all',
                   '/api/v1/food/info']

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

    SECRET_KEY = 'gebidetaishang'
    # 设置连接数据库的URL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/db_1811_flask'

    # 数据库和模型类同步修改
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    APP_ID = 'wx8b77e719e6fbd899'
    APPSECRET ='1db1022c1f80bb9f0d8b3835197504de'
    MCH_ID ='131452010386'#商户号id
    PAYKEY = 'dgjagrg23435'#商户秘钥

    DOMAIN = 'http://127.0.0.1:5000'
    # DOMAIN = 'http://129.28.206.139:80'


# 线上环境
class ProductingConfig(Config):
    DEBUG = False

# 生产环境
class DevelopmentConfig(Config):
    DEBUG = True

mapping_config = {
    'pro': ProductingConfig,
    'dev': DevelopmentConfig,
}
