import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import jo_bom_list_details

dash.register_page(__name__, path='/jobomlist')

layout = dbc.Row([
    jo_bom_list_details.render()
])