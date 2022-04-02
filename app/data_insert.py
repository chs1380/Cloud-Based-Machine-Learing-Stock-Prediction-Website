from app import db
from model import *
from werkzeug.security import generate_password_hash, check_password_hash

model1=Model(Model_name="linear regression")
model2=Model(Model_name="MLP prediction")

db.session.add(model1)
db.session.add(model2)
db.session.commit()
