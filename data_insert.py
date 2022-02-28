from app import db
from model import *
from werkzeug.security import generate_password_hash, check_password_hash

model1=Model(Model_name="linear regression")
model2=Model(Model_name="MLP prediction")


def create_user(User_name, Email, password):
    new_Teacher = User(User_name=User_name, User_Password=generate_password_hash(password, method='sha256'),
                       email=Email)
    db.session.add(new_Teacher)
    db.session.commit()

db.session.add(model1)
db.session.add(model2)
db.session.commit()
create_user('Tester1','leungwinghin599@gmail.com','933260')
