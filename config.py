import os
class Config(object):
    DEBUG = True
    SECRET_KEY = "YTGLBygn6C"
    WTF_CSRF_SECRET_KEY = "I7dz4PD7T6"
    STATIC_FOLDER = 'machine_learning_hkbu/app/static'
    # database URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:GBuOMcYaq54xU-rofwY,hOFwg-v528@auroradb-auroracluster23d869c0-12k8tb50v0a6i.cluster-cbh4kufcvqer.us-east-1.rds.amazonaws.com/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
