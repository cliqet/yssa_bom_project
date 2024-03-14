import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import client_list_details_section

dash.register_page(__name__, path='/clientlist')

layout = dbc.Row([
        dbc.Row(client_list_details_section.render())
    ])