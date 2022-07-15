from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('../scatterplot_data.csv')

# Edit frame with CSV column values
fig = px.scatter(df, x="Grade Average", y="Time Logged",
                 size="Grade Average", color="Section", hover_name="Name",
                 log_x=True, size_max=60)

app.layout = html.Div([  # Layout defines The HTML organization on a whole
    html.H1(children='User Scatterplot: The effect of time logged on grade average'),

    html.Div(children='''
    Color denotes section, scatterplot adapts class range
    '''),

    dcc.Graph(
        id='time-log-vs-grade-avg',
        figure=fig
    )
])


def return_fig():  # Returns figure for use in main.py > display_scatterplot()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)