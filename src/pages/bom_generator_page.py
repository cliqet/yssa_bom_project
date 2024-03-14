import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import bom_generator_details_section, bom_generator_requirements_section
from constants.styles import PAGE_PADDING_STYLE

dash.register_page(__name__, path='/bomgenerator')

layout = dbc.Row([
        dbc.Row(bom_generator_details_section.render()),
        dbc.Row(bom_generator_requirements_section.render())
    ], style=PAGE_PADDING_STYLE)