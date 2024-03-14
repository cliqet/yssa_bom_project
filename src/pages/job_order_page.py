from dash import Dash
import dash_bootstrap_components as dbc
from components import job_order_details_section, job_order_requirements_section
from constants.styles import PAGE_PADDING_STYLE


def render(app: Dash) -> dbc.Row:
    return dbc.Row([
        dbc.Row(job_order_details_section.render(app)),
        dbc.Row(job_order_requirements_section.render(app))
    ], style=PAGE_PADDING_STYLE)