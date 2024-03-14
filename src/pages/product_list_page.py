import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import product_list_details_section

dash.register_page(__name__, path='/productlist')

layout = dbc.Row([
        dbc.Row(product_list_details_section.render())
    ])