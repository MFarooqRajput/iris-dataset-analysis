import plotly.express as px
from dash import html, dcc
from data import df, opts1, opts3
 
# builds the pie chart
pie_fig = px.pie(
    data_frame = df,
    names = df['Species'], 
    hole = .3, 
    height = 400,
    title = 'Iris Species (%)',
    color_discrete_sequence=px.colors.qualitative.Dark24 
)

# builds the heatmap
heatmap_fig = px.imshow(df.drop('Species', axis=1).corr(),
    height = 400,
    color_continuous_scale = px.colors.sequential.Bluyl, 
    title = 'Correlation matrix of Iris variables'
)

#dashboard
dashboard = html.Div( 
    children =[
        html.Div(
            className="twelve columns",
            children=[
                html.H2(
                    children='Iris Dataset Analysis Uisng Dash',
                    style={
                        'textAlign': 'center',
                        }
                    ),

                html.Div(
                    children='''
                        Dash: A web application framework for Python.
                    ''',
                    style={
                        'textAlign': 'center',
                        'color': 'gray'
                        }
                    ),
                html.Div([ 
                    html.Div(
                        className='two columns',
                        children=[
                            html.Label(["Select feature ofor X-axis:", 
                                dcc.Dropdown(
                                    id = 'opt1', 
                                    options = opts1, 
                                    value = 'SepalWidth')]),
                        ],
                    ),
                    html.Div(
                        className='four columns',
                        children=[
                            html.Label(["Select feature ofor Y-axis:", 
                                dcc.RadioItems(
                                    id = 'opt2', 
                                    options = opts1, 
                                    value = 'SepalLength', 
                                    labelStyle={'display': 'inline-block', 'text-align': 'justify'} )]),
                        ],   
                    ),
                ], 
                style={"margin": "50px 20px 20px 20px"} # Marign: TOP, RIGHT, BOTTOM, LEFT
                ),
                html.Div(
                    className="twelve columns",
                    children=
                    [
                        html.Div(
                            className='five columns',
                            children=[
                                dcc.Loading(id = "loading-icon1", 
                                children=[html.Div(dcc.Graph(id='line-chart'))], type="circle", color="#2c2c2e"), 
                            ],
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                html.Div(dcc.Graph(id='pie-chart', figure = pie_fig))
                            ],   
                        ),
                        html.Div(
                            className='three columns',
                            children=[
                                html.Div(dcc.Graph(id='heatmap-plot', figure = heatmap_fig))
                            ],   
                        ),

                    ],
                    style={"margin": "20px 20px 20px 20px"}
                ),
                html.Div(
                    className="twelve columns",
                    children=
                    [
                        html.Div(
                            className='two columns',
                            children=[
                                html.Label(["Select table columns:", 
                                    dcc.Checklist(
                                        id = 'opt3', 
                                        options = opts3, 
                                        value =  ['SepalWidth','Species'])]),
                            ],   
                        ),
                        html.Div(
                            className='nine columns',
                            children=[
                                html.Div(id='table1', style={"margin-left": "10px", "margin-right": "10px", "margin-botton": "60px"}) 
                            ],
                        ),
                    ],
                    style={"margin": "20px 20px 20px 20px"}
                ),

            ],
        )
])

#main layout
main_layout = html.Div(
    [
        dcc.Location(
            id = 'url',
            refresh = False
        ),

        html.Div(
            id = 'page-content'
        )
    ]
)