from dash import html
from dash import dash_table, callback, Output, Input
import dash_bootstrap_components as dbc
from constants.styles import TABLE_STYLE, TABLE_CELL_STYLE, TABLE_HEADER_STYLE
from database.get_clients import get_clients
from models.client import Client


def render() -> dbc.Col:
    table_columns = [
        {'name': 'ID', 'id' : 'ID'},
        {'name': 'Company Name', 'id' : 'Company Name'},
        {'name': 'Contact Person', 'id' : 'Contact Person'},
        {'name': 'Contact No.', 'id' : 'Contact No.'},
        {'name': 'Email Address', 'id' : 'Email Address'},
        
    ]

    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("Client List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='client-table',
            columns=table_columns,
            # data=table_data,
            editable=False,
            page_size=10,
            style_table=TABLE_STYLE,
            style_cell=TABLE_CELL_STYLE,
            style_header=TABLE_HEADER_STYLE,
        ), width=12),
    ]),
    
], width=10, style={'margin-top': '20px', 'height': '100%', 'width': '100%'})

@callback(Output('client-table', 'data'), Input('url', 'pathname'))
def load_clients(pathname):
    if pathname == '/clientlist':
        clients: list[Client] = get_clients()
        table_data = [
            {
                'ID': client.client_id,
                'Company Name': client.company_name,
                'Contact Person': client.contact_person,
                'Contact No.': client.contact_no,
                'Email Address': client.email_address
            }
            for client in clients
        ]
    else:
        table_data = []

    return table_data