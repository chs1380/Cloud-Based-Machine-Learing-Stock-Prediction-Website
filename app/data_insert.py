from app import db
from model import Model,User
from config import Config

model1=Model(Model_name="linear regression")
model2=Model(Model_name="MLP prediction")

user1=User(User_name="tester1", User_Password="123456")

db.session.add(model1)
db.session.add(model2)

db.session.commit()
