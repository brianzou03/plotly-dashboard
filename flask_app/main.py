from flask import render_template
from __init__ import start
from flask_app.helpers import scatterplot, bargraph
import json
import plotly
import csv

# To run through commandline, use flask run
app, mysql = start()


@app.route("/", methods=['GET', 'POST'])
def display_chart():
    row_c = chart_row_count()
    data_tuple = get_chart_db_val()
    data_vals = []

    data = list(csv.reader(open("flask_app/data/chart_data.csv")))

    f = open('flask_app/data/chart_data.csv', 'w')  # Insert in chart format
    f.write("Index,Name,Section,Attention Span,Grade Average\n")  # Defines the fields for the chart

    for i in range(0, row_c):  # Iterating through the SQL data
        data_vals.append(data_tuple[i].values())  # Adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        further_mod_str = modified_str.replace("'", "")  # Removes quotes from LastName
        f.write(further_mod_str[0:-2] + "\n")
    f.close()

    return render_template('index.html', data=data)


@app.route("/scatterplot", methods=['GET', 'POST'])
def display_scatterplot():
    row_c = scatter_row_count()
    data_tuple = get_scatter_db_val()
    data_vals = []

    fig = scatterplot.return_fig()  # Accessing figure from scatterplot.py
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    f = open('flask_app/data/scatterplot_data.csv', 'w')  # Insert in chart format
    f.write("Index,Name,Section,Time Logged,Grade Average\n")  # Defines the fields for the scatterplot

    for i in range(0, row_c):  # Iterating through the SQL data
        data_vals.append(data_tuple[i].values())  # Adding to list of data values
        temp_str = str(data_vals[i])  # "dict_values([1, 'Zou', 1.0, 50.0, 100.0])"
        modified_str = temp_str[13:]
        further_mod_str = modified_str.replace("'", "")  # Removes quotes from LastName
        f.write(further_mod_str[0:-2] + "\n")
    f.close()

    return render_template('scatterplot.html', graphJSON=graphJSON)


@app.route("/bargraph", methods=['GET', 'POST'])
def display_bargraph():  # Bargraph data is located within bargraph.py, doesn't read from a file
    fig = bargraph.return_fig()
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('bargraph.html', graphJSON=graphJSON)


def get_chart_db_val():  # Gets chart values from SQL table
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM chart_table")
    data_tuple = cursor.fetchall()
    return data_tuple


def get_scatter_db_val():  # Gets scatterplot values from SQL table
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM scatter_table")
    data_tuple = cursor.fetchall()
    return data_tuple


def chart_row_count():  # Gets chart row count
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM chart_table")
    data_tuple = cursor.fetchall()
    row_c = len(data_tuple)
    return row_c


def scatter_row_count():  # Gets scatterplot row count
    cursor = mysql.connect.cursor()
    cursor.execute("SELECT * FROM scatter_table")
    data_tuple = cursor.fetchall()
    row_c = len(data_tuple)
    return row_c


if __name__ == "__main__":
    app.run(debug=True)