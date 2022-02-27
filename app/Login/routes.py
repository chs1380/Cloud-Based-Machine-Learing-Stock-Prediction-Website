from flask import Flask, request, render_template, flash, url_for, redirect
from app.Login import bp
import fileinput
from config import Config
from app.Login.form import loginform
from model import User
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user, logout_user


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = loginform(csrf_enabled=False)
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user = User.query.filter_by(User_name=user_name).first()
        if not user or not check_password_hash(user.User_Password, password):
            flash('Please check your login details and try again.', category='danger')
            return redirect(url_for('login.login'))
        else:
            login_user(user)
            flash('Welcome ' + user.User_name, category='success')
            return redirect(url_for('home.home'))
    return render_template('Login/login.html', form=form)

@bp.route('/logout')
def logout():
    user_id = current_user.get_id()
    logout_user()
    flash( 'Success logout', category='success')
    return redirect(url_for('login.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    mainbarquery = Mainbar.query.all()
    return render_template('Login/register.html', title='Register', form=form, mainbarquery=mainbarquery)

