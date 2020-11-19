from flask import Flask, render_template, request
import requests

app = Flask(__name__)
base_url = 'http://127.0.0.1:5002' #from flask-db-no-auth projects

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get-names')
def get_names():
	r = requests.get(base_url + '/name').json()['names']
	length = len(r)
	return render_template('get-names.html', length=length, json=r)

@app.route('/get-name', methods=['POST'])
def get_name():
	if 'name' in request.form:
		name = request.form['name']
		r = requests.get(base_url + f"/name/{name}").json()
		return render_template('get-name.html', json=r)

@app.route('/change-name', methods=['POST'])
def change_name():
	if 'old_name' in request.form and 'new_name' in request.form:
		old_name = request.form['old_name']
		new_name = request.form['new_name']
		r = requests.put(base_url + f"/name/{old_name}", json={'name': new_name})
		return render_template('change-name.html', json=r.text)

@app.route('/delete-name', methods=['POST'])
def delete_name():
	if 'erase_name' in request.form:
		r = requests.delete(base_url + f"/name/{request.form['erase_name']}")
	
	return render_template('delete-name.html', json=r.text)

@app.route('/add-name', methods=['POST'])
def add_name():
	if 'add_name' in request.form:
		add_name = request.form['add_name']
		r = requests.post(base_url + '/name', json={'name': add_name})

	return render_template('add-name.html', json=r.text)

if __name__ == "__main__":
	app.run(debug=True)