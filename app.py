from flask import Flask
from flask import request, send_from_directory, render_template
import numpy as np
from flask_cors import CORS

app = Flask(__name__,template_folder='template')
CORS(app)

@app.route("/")
def index():
	print("asd")
	return "Hello World!"

@app.route("/test")
def test():
	print("test")
	return "test API"

@app.route("/predict")
def predict():
	g = request.args.get('gen')
	t = request.args.get('temp')
	print("predict")
	# training code

	# prediction code
	pred = 1

	return pred

@app.route("/tt")
def tt():
    return render_template('index.html')

# app.run(port=5000)
