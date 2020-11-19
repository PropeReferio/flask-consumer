from flask import Flask, render_template, request
import requests

app = Flask(__name__)
base_url = 'http://127.0.0.1:5002'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get-names')
def get_names():
	r = requests.get(base_url + '/name').json()['names']
	length = len(r)
	return render_template('get-names.html', length=length, json=r)

@app.route('/get-name')
def get_name():
	return render_template('get-name.html')

@app.route('/change-name')
def change_name():
	return render_template('change-name.html')

@app.route('/delete-name')
def delete_name():
	return render_template('delete-name.html')

@app.route('/add-name')
def add_name():
	return render_template('add-name.html')

if __name__ == "__main__":
	app.run(debug=True)