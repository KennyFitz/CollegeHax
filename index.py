from flask import Flask
from flask import render_template
app = Flask(__name__)

# get colleges from db
colleges = ['Stony Brook', 'Buffalo', 'Nassau']

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/colleges')
def list_colleges():
	return render_template('colleges.html', colleges=colleges)

@app.route('/colleges/<id>')
def display_college(id):



	return render_template('college.html', college=colleges[int(id)])


#collegehax.com/hello/
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)