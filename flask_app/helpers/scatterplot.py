# Run on CMD line: cd flask_app -> cd helpers -> python scatterplot.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('../data/scatterplot_data.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    html.H1(children='Example Scatterplot: Life Expectancy'),

    html.Div(children='''
    Example Text
    '''),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)