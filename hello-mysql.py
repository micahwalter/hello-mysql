import os
from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_PASSWORD']
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DB']

mysql.init_app(app)

@app.route('/')
def hello():
	cursor = mysql.get_db().cursor()
	
	# test sql statement
	sql = 'SELECT * FROM authors'
	cursor.execute(sql)
	data=cursor.fetchall()
	
	return data