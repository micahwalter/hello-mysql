hello-mysql
===

Just my notes on setting up a python/flask app with mysql, on RDS and Heroku...

Set up Amazon RDS add-on via Heroku admin panel, then

		$ pip install flask-mysql
    	$ heroku config:set MYSQL_USER=username
		$ heroku config:set MYSQL_PASSWORD=password
		$ heroku config:set MYSQL_HOST=rds-endpoint
		$ heroku config:set MYSQL_DB=database
		
		