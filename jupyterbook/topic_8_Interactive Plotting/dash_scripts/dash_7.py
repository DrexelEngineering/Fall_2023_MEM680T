
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

app.layout = html.Div([
    html.Div([

        # x column
        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(), # all the unique indicator names
                'Fertility rate, total (births per woman)', # default
                id='xaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'], # log or linear
                'Linear',
                id='xaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        # y column
        html.Div([
            dcc.Dropdown(
                df['Indicator Name'].unique(), # all the unique indicator names
                'Life expectancy at birth, total (years)', # default
                id='yaxis-column'
            ),
            dcc.RadioItems(
                ['Linear', 'Log'],
                'Linear',
                id='yaxis-type',
                inline=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        df['Year'].min(), # min year range
        df['Year'].max(), # max year range
        step=None,
        id='year--slider',
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()}, # where the marks go

    )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    # note that we take all of  the input paramters each time the callback is called
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year--slider', 'value'))
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    # filters the data based on year
    dff = df[df['Year'] == year_value]
    
    # filters the data in the scatterplot
    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    # sets the scales of the axis
    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
