from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from pages import job_order_page, bom_generator_page, jo_bom_list_page, product_list_page, client_list_page, employee_list_page


def render(app: Dash) -> dbc.Col:
    # TODO: dynamically render the proper page based on the route
    # return dbc.Col(job_order_page.render(app))
    # return dbc.Col(bom_generator_page.render(app))
    # return dbc.Col(jo_bom_list_page.render(app))
    # return dbc.Col(product_list_page.render(app))
    # return dbc.Col(client_list_page.render(app))
    return dbc.Col(employee_list_page.render(app))








