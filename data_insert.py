from model import Model
from app import db

def init_app(model):
    model1=Model(Model_name="linear regression")
    model2=Model(Model_name="MLP prediction")

    db.session.add(model1)
    db.session.add(model2)
    db.session.commit()


