from flask import Flask, request, render_template, flash, url_for, redirect
from app.Login import bp
import fileinput
from config import Config
from app.Login.form import loginform, RegistrationForm, ResetPasswordForm
from model import User
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from flask_login import login_user, logout_user, current_user, login_required


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Home_Page.home'))
    form = loginform(csrf_enabled=False)
    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user = User.query.filter_by(User_name=user_name).first()
        if not user or not check_password_hash(user.User_Password, password):
            flash('Please check your login details and try again.', category='danger')
            return redirect(url_for('login_page.login'))
        else:
            login_user(user)
            flash('Welcome ' + user.User_name, category='success')
            return redirect(url_for('Home_Page.home'))
    return render_template('Login/login.html', form=form)


@login_required
@bp.route('/logout')
def logout():
    user_id = current_user.get_id()
    logout_user()
    flash('Success logout', category='success')
    return redirect(url_for('Home_Page.home'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Home_Page.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(User_name=form.username.data, email=form.email.data,
                    User_Password=generate_password_hash(form.password.data, method='sha256'))
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login_page.login'))
    return render_template('Login/register.html', title='Register', form=form)

