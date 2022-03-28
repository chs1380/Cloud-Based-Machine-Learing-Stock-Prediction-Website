class Config(object):
    DEBUG = True
    SECRET_KEY = "YTGLBygn6C"
    WTF_CSRF_SECRET_KEY = "I7dz4PD7T6"
    STATIC_FOLDER = 'machine_learning_hkbu/app/static'
    # database URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:l5N7.e1=Od_EW2XP0kDXQiUQWZToqU@auroradb-auroracluster23d869c0-zcnly9oqxnqf.cluster-cssae9afjapw.ap-southeast-1.rds.amazonaws.com/ml_website'
    SQLALCHEMY_TRACK_MODIFICATIONS = False