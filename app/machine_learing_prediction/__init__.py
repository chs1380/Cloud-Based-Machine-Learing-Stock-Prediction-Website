from flask import Blueprint

bp=Blueprint("machine_learning_prediction",__name__)

from app.machine_learing_prediction import routes