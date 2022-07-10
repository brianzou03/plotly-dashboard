from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from __init__ import start

# To run through commandline, use flask run
app, mysql = start()


# Displays text form of data table, (PersonID, LastName, Grade1, Grade2, Grade3 CompositeGrade)
@app.route("/", methods=['GET', 'POST'])
def index():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM dash_table")
    data = cursor.fetchall()
    print(data)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)