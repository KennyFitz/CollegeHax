from flask import Flask, render_template, request
app = Flask(__name__)

# db configuration
from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://kennyfitz:Brismell1!@collegehax.corbsmdjxstj.us-east-2.rds.amazonaws.com:1433/collegehax?driver=SQL+Server+Native+Client+11.0'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	major = db.Column(db.String(50))

	def __repr__(self):
		return '<User %r>' % self.username


db.create_all()

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


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
	# if method is GET, return adding user inerface
	if request.method == 'GET':
		return render_template('new-user.html')
	# if method is POST, persist data to db
	else:
		app.logger.debug('got a post request major: ')
		app.logger.debug(request.form)

		new_user = User(
			username=request.form['username'],
			email=request.form['email'],
			major=request.form['major']
		)

		db.session.add(new_user)
		db.session.commit()

		return 'added user!'


@app.route('/all-users')
def all_users():
	# get users from the database
	users = User.query.all()

	#app.logger.debug('users are: ', users)
	#app.logger.debug('first user: ', users[0].username)

	return 'first user is: %s' % users[0].username

#collegehax.com/hello/
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)