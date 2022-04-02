from app import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    User_id = db.Column(db.Integer(),unique=True, primary_key=True, nullable=False)
    User_name = db.Column(db.String(20), nullable=False)
    User_Password=db.Column(db.String(300),nullable=False)
    result=db.relationship('Result',backref='user',lazy=True)
    email=db.Column(db.String(100),nullable=False)

    def get_id(self):
        return (self.User_id)

    def __repr__(self):
        return '<User %r>' % self.User_name

class Result(db.Model):
    Result_id = db.Column(db.Integer(),unique=True, primary_key=True, nullable=False)
    Stock_code=db.Column(db.String(20), nullable=False)
    Date_that_init_predict=db.Column(db.DateTime)
    Old_price=db.Column(db.Float(),nullable=False)
    price_after_10=db.Column(db.Float())
    price_after_60=db.Column(db.Float())
    price_after_360=db.Column(db.Float())
    user_id=db.Column(db.Integer,db.ForeignKey('user.User_id'))
    Model=db.Column(db.String(20),nullable=False)
    Model_id=db.Column(db.Integer,db.ForeignKey('model.Model_id'))
    def __repr__(self):
        return '<Result %r>' % self.Result_id

class Model(db.Model):
    Model_id = db.Column(db.Integer(),unique=True, primary_key=True, nullable=False)
    Model_name=db.Column(db.String(20),nullable=False)
    result_model_id=db.relationship('Result',backref='model',lazy=True)
    def __repr__(self):
        return '<Model %r>' % self.Model_name
