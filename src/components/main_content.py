from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from pages import job_order_page


def render(app: Dash) -> dbc.Col:
    # TODO: dynamically render the proper page based on the route
    return dbc.Col(job_order_page.render(app))







