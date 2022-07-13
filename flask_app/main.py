from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from __init__ import start
import pandas as pd
from helpers import chart, scatterplot
import json
import plotly
import csv


# To run through commandline, use flask run
app, mysql = start()

# TODO: Embed dash into flask server
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


# Developer note: This is a randomized list of grades, don't take it personally :D
@app.route("/", methods=['GET', 'POST'])
def write_to_chart():  # Writes to chart_data.csv, run chart.py
    row_c = chart_row_count()
    data_tuple = get_chart_db_val()
    data_vals = []

    data = list(csv.reader(open("flask_app/data/chart_data.csv")))
    print(data)

    f = open('flask_app/data/chart_data.csv', 'w')  # insert in chart format
    f.write("Index,Name,Section,Attention Span,Grade Average\n")

    for i in range(0, row_c):
        data_vals.append(data_tuple[i].values())  # adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        further_mod_str = modified_str.replace("'", "")  # removes quotes from LastName
        f.write(further_mod_str[0:-2] + "\n")
    f.close()

    return render_template('index.html', data=data)


@app.route("/scatterplot", methods=['GET', 'POST'])
def write_to_scatterplot():  # Writes to scatterplot.py, run scatterplot.py
    row_c = scatter_row_count()
    data_tuple = get_scatter_db_val()
    data_vals = []
    fig = scatterplot.return_fig()

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    f = open('flask_app/data/scatterplot_data.csv', 'w')  # insert in chart format
    f.write("Index,Name,Section,Time Logged,Grade Average\n")

    for i in range(0, row_c):
        data_vals.append(data_tuple[i].values())  # adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        further_mod_str = modified_str.replace("'", "")  # removes quotes from LastName
        f.write(further_mod_str[0:-2] + "\n")
    f.close()

    return render_template('scatterplot.html', graphJSON=graphJSON)


def get_chart_db_val():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM chart_table")
    data_tuple = cursor.fetchall()
    return data_tuple


def get_scatter_db_val():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM scatter_table")
    data_tuple = cursor.fetchall()
    return data_tuple


def chart_row_count():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM chart_table")
    data_tuple = cursor.fetchall()
    row_c = len(data_tuple)
    return row_c


def scatter_row_count():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM scatter_table")
    data_tuple = cursor.fetchall()
    row_c = len(data_tuple)
    return row_c


if __name__ == "__main__":
    app.run(debug=True)