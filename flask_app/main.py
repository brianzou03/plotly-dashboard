from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from __init__ import start

# To run through commandline, use flask run
app, mysql = start()


# TODO: Use Python Dash to create interactive dashboards
# Link table data to dash statistics
@app.route("/", methods=['GET', 'POST'])
def index():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM dash_table")
    data = cursor.fetchall()
    print(data)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)