from dash import Dash
import dash_bootstrap_components as dbc
from components import jo_bom_list_details


def render(app: Dash) -> dbc.Row:
    return dbc.Row([
        dbc.Row(jo_bom_list_details.render(app))
    ])