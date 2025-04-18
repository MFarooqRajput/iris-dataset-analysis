import dash
from dash import Dash
from typing import List

external_stylesheets: List[str] = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    title='Iris Dataset Analysis Using Dash',
    external_stylesheets=external_stylesheets
)