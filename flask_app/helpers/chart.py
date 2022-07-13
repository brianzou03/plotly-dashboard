# Run on CMD line: cd flask_app -> cd helpers -> python chart.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd


f = open('../chart_data.csv', 'r')

df = pd.read_csv('../chart_data.csv')


def generate_table(dataframe, max_rows=10):
    table = html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

    return table


app = Dash(__name__)

app.layout = html.Div([
    html.H2(children='User Chart: Attention Span to Grade Average'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)