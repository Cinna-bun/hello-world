from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '447226F85B4AD2438A4D9491739E6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	age = db.Column(db.String(3), nullable=False)
	gender = db.Column(db.String(7), nullable=False)

	def __repr__(self):
		return "User('" + self.name + ", '" + self.age + "', '" + self.gender + "')"




#This is some dummy data to use a placeholder; pretend we got this from the database then proceeded to use it.
data = [
	{
		'title': 'Michael S',
		'age': '35'
	},
	{
		'title': 'Bill G',
		'age': '19'
	}
]

#This block says that if the web address bar is either blank or has "/home" on the end, then it'll pull this page up.
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', data=data, title="Home")

#This block says if the web address bar has "/about" on the end then it'll display this page.
@app.route("/about")
def about():
	return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('{} has been added to the list.' .format(form.name.data), 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

#unimportant code that doesn't really do anything right now.
if __name__ == '__main__':
	app.run(debug=true)