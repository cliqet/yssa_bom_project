from dash import Dash
import dash_bootstrap_components as dbc
from components import employee_list_details_section


def render(app: Dash) -> dbc.Row:
    return dbc.Row([
        dbc.Row(employee_list_details_section.render(app))
    ])