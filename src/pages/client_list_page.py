from dash import Dash
import dash_bootstrap_components as dbc
from components import client_list_details_section


def render(app: Dash) -> dbc.Row:
    return dbc.Row([
        dbc.Row(client_list_details_section.render(app))
    ])