from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({  # Dataframe contains the data for the bargraph
    "Feature": ["Quizzes", "Videos", "Assignments", "Quizzes", "Videos", "Assignments"],
    "Time Spent": [1, 4, 7, 2, 4, 8],
    "Gender": ["Male", "Male", "Male", "Female", "Female", "Female"]
})

# x and y are axis labels, color and barmode alter graph display
fig = px.bar(df, x="Feature", y="Time Spent", color="Gender", barmode="group")

app.layout = html.Div(children=[  # Layout defines The HTML organization on a whole
    html.H1(children='Example Bar Graph: Attention Retention'),

    html.Div(children='''
        Feature Attention Retention Bar Graph
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])


def return_fig():  # Returns figure for use in main.py > display_bargraph()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)