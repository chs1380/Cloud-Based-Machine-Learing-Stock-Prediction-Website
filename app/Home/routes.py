from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from app.Home import bp
from model import *
import fileinput
from config import Config
from flask_login import login_required


@bp.route('/', methods=['GET'])
def home():
    return render_template('Home/home.html')
