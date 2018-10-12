from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=1, max=30)])

	age = StringField('Age', validators=[DataRequired(), Length(min=1, max=3)])

	gender = StringField('Gender', validators=[DataRequired(), Length(min=1, max=7)])

	submit = SubmitField('Send Data')


