import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, suppress_callback_exceptions = True, title = 'Iris Dataset Analysis Uisng Dash', external_stylesheets=external_stylesheets)