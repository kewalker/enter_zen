# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
	return ('</br>hello?</br>oh, hello!')

if __name__ == "__main__":
	app.run()