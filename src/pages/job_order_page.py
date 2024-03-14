import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import job_order_details_section, job_order_requirements_section
from constants.styles import PAGE_PADDING_STYLE

dash.register_page(__name__, path='/')

layout = dbc.Row([
        dbc.Row(job_order_details_section.render()),
        dbc.Row(job_order_requirements_section.render())
    ], style=PAGE_PADDING_STYLE)