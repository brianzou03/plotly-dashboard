# Run on CMD line: cd flask_app -> python bargraph.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.DataFrame({  # Plug stuff into this dataset
    "Stuff": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Stuff", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Dash Bar Graph'),

    html.Div(children='''
        Bar Graph: Contains info on SF and Montreal
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)