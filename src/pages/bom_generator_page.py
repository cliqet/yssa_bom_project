from dash import Dash
import dash_bootstrap_components as dbc
from components import bom_generator_details_section, bom_generator_requirements_section


def render(app: Dash) -> dbc.Row:
    return dbc.Row([
        dbc.Row(bom_generator_details_section.render(app)),
        dbc.Row(bom_generator_requirements_section.render(app))
    ])