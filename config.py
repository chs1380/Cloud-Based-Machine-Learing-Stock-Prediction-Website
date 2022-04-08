class Config(object):
    DEBUG = True
    SECRET_KEY = "YTGLBygn6C"
    WTF_CSRF_SECRET_KEY = "I7dz4PD7T6"
    STATIC_FOLDER = 'machine_learning_hkbu/app/static'
    # database URI
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://your_user_name:password_for_db@your_db_host_name/your_selected_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False