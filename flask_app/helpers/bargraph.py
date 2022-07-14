# Run on CMD line: cd flask_app -> cd helpers -> python bargraph.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.DataFrame({  # Plug stuff into this dataset
    "Feature": ["Quizzes", "Videos", "Assignments", "Quizzes", "Videos", "Assignments"],
    "Time Spent": [1, 4, 7, 2, 4, 8],
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Female"]
})

fig = px.bar(df, x="Feature", y="Time Spent", color="Gender", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Example Bar Graph: Attention Retention'),

    html.Div(children='''
        Feature Attention Retention Bar Graph
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


def generate_bargraph():
    bargraph = app.layout = html.Div(children=[
        html.H1(children='Example Bar Graph: Attention Retention'),

        html.Div(children='''
            Feature Attention Retention Bar Graph
        '''),

        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

    return bargraph


def return_fig():
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)