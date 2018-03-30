from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Kenny'}
	posts = [
		{
			'author': {'username': 'Sunryu Suzuki'},
			'body': 'The most important thing is to find out<br> what is the most important thing'
		},
		{
			'author': {'username': 'Basho'},
			'body': 'Old pond,<br> frog jumps in-<br> splash'
		}
	]
	return render_template ('index.html', title='Home', user=user, posts=posts)

@app.route('/farts')
def farts():
	return "You fartin heard it here first!"