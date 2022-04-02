from flask import render_template
from app.Home import bp


@bp.route('/', methods=['GET'])
def home():
    return render_template('Home/home.html')
