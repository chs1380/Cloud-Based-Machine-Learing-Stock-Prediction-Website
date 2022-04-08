class Config(object):
    DEBUG = True
    SECRET_KEY = "YTGLBygn6C"
    WTF_CSRF_SECRET_KEY = "I7dz4PD7T6"
    STATIC_FOLDER = 'machine_learning_hkbu/app/static'
    # database URI
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:b.d3ZFDNfAdtaXr-EW3W=OA5G1oOFF@auroradb-auroracluster23d869c0-g2kpuhzw35rl.cluster-cssae9afjapw.ap-southeast-1.rds.amazonaws.com/sys'
    SQLALCHEMY_TRACK_MODIFICATIONS = False