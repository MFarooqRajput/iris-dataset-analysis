from app import app
from dash.dependencies import Input, Output 
from dash import dash_table
import plotly.express as px
from layouts import dashboard
from data import *

# defines callback to the dashboard
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    return dashboard # This is the "home page"

# defines callback to the table
@app.callback(
    Output('table1', 'children'),
    [Input('opt3', 'value')])
def update_table(input1):

    table = dash_table.DataTable(
        columns=[{"name": i, "id": i} 
                    for i in input1], 
        data=df.to_dict('records'), 
        style_cell={'minWidth': 40, 'maxWidth': 40, 'width': 40, 'font_family': 'Arial', 'font_size': '15px','text_align': 'left'},
        style_header=dict(backgroundColor="rgb(239, 243, 255)"),
        style_data=dict(backgroundColor="white"),
        page_size=7,
        fixed_rows={'headers': True},
        style_table={'overflowY': 'auto'},
    )

    return table

# defines callback to the scatter plot
@app.callback(
    Output('line-chart', 'figure'),
    Input('opt1', 'value'),
    Input('opt2', 'value'))
def update_graph(input1, input2):

    fig = px.scatter(
        data_frame = df,
        x=input1,
        y=input2,
        color= df['Species'],
        height = 400,
        title = 'Clustering Iris Species',
        color_discrete_sequence=px.colors.qualitative.Dark24
    )

    return fig