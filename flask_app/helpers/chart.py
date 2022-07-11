# Run on CMD line: cd flask_app -> cd helpers -> python chart.py
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html
import pandas as pd

# Replace with our CSV file -> Edit CSV file dynamically


f = open('../data/chart_data.csv', 'w')  # insert in chart format
f.write("""
Index , Role, Name, Concentration, Time Logged
1,Student,Zou,CS, 1087.68
2,Student,Kabdou,English,567.89
3,Teacher,To,Math,1000.50
4,Administrator,Mao,Bio,7681.50
5,Administrator,Chadha,STEM,15134.67
""")
f.close()

#open and read the file after the appending:
f = open('../data/chart_data.csv', 'r')
print(f.read())

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
    html.H2(children='User Statistics Chart'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)