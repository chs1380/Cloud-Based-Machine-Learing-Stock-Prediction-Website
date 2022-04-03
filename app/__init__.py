from flask import Flask, session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager
from datetime import timedelta
from flask_httpauth import HTTPBasicAuth
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) #delcare before create app
auth = HTTPBasicAuth(app)

migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
mail = Mail(app)




def create_app():
    db.init_app(app)
    migrate.init_app(app, db) # declare after init app

    from app.machine_learing_prediction import bp as ml_prediction
    from app.Login import bp as login
    from app.Home import bp as home
    from model import User
    app.register_blueprint(ml_prediction)
    app.register_blueprint(login)
    app.register_blueprint(home)


    #delcare after init app
    login_manager = LoginManager(app)  # login manager use for
    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login_page.login'

    @login_manager.user_loader
    def load_user(User_id): #setup login manager to get user table
         # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(User_id))

    @app.before_request
    def before_request():
        session.permanent = True #setup session
        app.permanent_session_lifetime = timedelta(minutes=60)

    with app.app_context():
        db.create_all()  # Create sql tables for our data models, init creation after all import
        # setup
    return app

