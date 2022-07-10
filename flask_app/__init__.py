def start():
    from flask import Flask
    from flask_mysqldb import MySQL
    import yaml

    app = Flask(__name__, template_folder='templates/', static_folder='static/')

    with open("flask_app/config.yaml", "r") as stream:
        config = yaml.safe_load(stream)

    # Change this to your secret key (can be anything, it's for extra protection)
    app.secret_key = 'your secret key'

    # Enter your database connection details below
    app.config['MYSQL_HOST'] = config['MYSQL_HOST']
    app.config['MYSQL_USER'] = config['MYSQL_USER']
    app.config['MYSQL_PASSWORD'] = config['MYSQL_PASSWORD']
    app.config['MYSQL_DB'] = config['MYSQL_DB']
    app.config['MYSQL_CURSORCLASS'] = config['MYSQL_CURSORCLASS']

    # Initialize MySQL
    mysql = MySQL(app)

    return app, mysql