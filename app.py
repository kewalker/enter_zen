# app.py
from flask import Flask
import enter_zen_train_model

app = Flask(__name__)

@app.route('/')
def index():
	# enter_zen_train_model.main()
	return ('</br>hello?</br>oh, hello!')


@app.route('/zen')
def zen():
	return ('hello from zen')

@app.route('/user/<username>')
def user(username):	
	return ('User {}'.format(username))


if __name__ == "__main__":
	app.run()