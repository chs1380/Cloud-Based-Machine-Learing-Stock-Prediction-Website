from wtforms import BooleanField, StringField, PasswordField, validators, SubmitField,SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class ml_form(FlaskForm):
    ml_model=SelectField('Select a machine learning prediction',choices=[],validators=[DataRequired()])
    stock_code=StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')