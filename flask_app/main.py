from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from __init__ import start
from dash import *
import pandas as pd

# To run through commandline, use flask run
app, mysql = start()

"""
def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/style.css',
        ]
    )

    dash_app.layout = html.Div(id='dash-container')

    return dash_app.server
"""


@app.route("/", methods=['GET', 'POST'])
def write_to_file():
    row_c = row_count()
    data_tuple = get_db_val()
    data_vals = []

    f = open('../chart_data.csv', 'w')  # insert in chart format
    f.write("Index , Role, Name, Concentration, Time Logged\n")

    for i in range(0, row_c):
        data_vals.append(data_tuple[i].values())  # adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        further_mod_str = modified_str.replace("'", "")  # removes '' from LastName
        f.write(further_mod_str[0:-2] + "\n")
    f.close()

    return render_template('index.html')


def get_db_val():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM dash_table")
    data_tuple = cursor.fetchall()
    print(data_tuple)
    return data_tuple


def row_count():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM dash_table")
    data_tuple = cursor.fetchall()
    row_c = len(data_tuple)
    return row_c


if __name__ == "__main__":
    app.run(debug=True)