from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from __init__ import start
from dash import Dash, html
import pandas as pd

# To run through commandline, use flask run
app, mysql = start()

# TODO: Use Python Dash to create interactive dashboards
# 1. Link table data to dash statistics

"""
@app.route("/", methods=['GET', 'POST'])
def index():
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM dash_table")
    data = cursor.fetchall()
    return render_template('index.html')
"""


def display_table():
    write_to_file()
    df = pd.read_csv('flask_app/data/chart_data.csv')

    app = Dash(__name__)

    app.layout = html.Div([
        html.H2(children='Class Engagement Chart'),
        generate_table(df)
    ])


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


@app.route("/", methods=['GET', 'POST'])
def write_to_file():
    row_c = row_count()
    data_tuple = get_db_val()
    data_vals = []

    f = open('flask_app/data/chart_data.csv', 'w')  # insert in chart format

    for i in range(0, row_c):
        data_vals.append(data_tuple[i].values())  # adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        f.write(modified_str[0:-2] + "\n")
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