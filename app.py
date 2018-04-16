# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return ('</br>hello?</br>oh, hello!')

@app.route('/zen')
def zen():
	return ('hello from zen')

@app.route('/user/<username>')
	return ('User {}'.format(username))


if __name__ == "__main__":
	app.run()