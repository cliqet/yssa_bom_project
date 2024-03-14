import dash
from dash import Dash
import dash_bootstrap_components as dbc
from components import employee_list_details_section

dash.register_page(__name__, path='/employeelist')

layout = dbc.Row([
        dbc.Row(employee_list_details_section.render())
    ])