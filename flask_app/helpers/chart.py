from dash import Dash, html
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('../chart_data.csv')  # Reading the csv file


def generate_table(dataframe, max_rows=10):  # Generates table using the CSV dataframe
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


app.layout = html.Div([  # Layout defines The HTML organization on a whole
    html.H2(children='User Chart: Attention Span to Grade Average'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)