import os


class Config(object):
    DEBUG = True
    SECRET_KEY = "YTGLBygn6C"
    WTF_CSRF_SECRET_KEY = "I7dz4PD7T6"
    STATIC_FOLDER = 'machine_learning_hkbu/app/static'
    # database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
