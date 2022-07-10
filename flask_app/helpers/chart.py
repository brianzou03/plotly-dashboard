# Run on CMD line: cd flask_app -> cd helpers -> python chart.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd

# Replace with our CSV info
df = pd.read_csv('../data/chart_data.csv')

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


app = Dash(__name__)

app.layout = html.Div([
    html.H2(children='Example Chart: US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)