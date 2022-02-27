import os # os is used for interacting with operating system
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))
#above code gives the basdir

class Config:
    #os.getenv method in Python returns the value of the environment variable key if it exists otherwise returns the default value.
    # default value is my_precious_secret_key
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    
    # environment will have different set up 
    # please see it more

    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost:5432/rbac_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig)
    #test=TestingConfig,
    #prod=ProductionConfig)

# as an when we need differnent system we can chnage it

key = Config.SECRET_KEY






