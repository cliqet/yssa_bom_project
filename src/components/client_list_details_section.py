from dash import Dash, html, dcc
import dash_table
import dash_bootstrap_components as dbc

# Define Table
table_data = [
    {'ID': '',
     'Company Name': '',
     'Contact Person': '',
     'Contact No.': '',
     'Email Address': '',    
     } for _ in range(50)
] 

table_columns = [
    {'name': 'ID', 'id' : 'ID'},
    {'name': 'Company Name', 'id' : 'Company Name'},
    {'name': 'Contact Person', 'id' : 'Contact Person'},
    {'name': 'Contact No.', 'id' : 'Contact No.'},
    {'name': 'Email Address', 'id' : 'Email Address'},
    
]


def render(app: Dash) -> dbc.Col:
    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("Client List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='client-table',
            columns=table_columns,
            data=table_data,
            editable=False,
            page_size=30,
            style_table={'height': '950px', 'overflowX': 'auto'},
            style_cell={
                'height': 'auto',
                'minWidth': '150px', 'width': '15px', 'maxWidth': '150px',
                'whiteSpace': 'normal',
                'font-size': '14px',
                'font-family': 'Arial, sans-serif',
                'textAlign': 'left',
            },
            
            style_header={
                'backgroundColor': 'white',
                'fontWeight': 'bold',
                'textAlign': 'center',
            },
        ), width=12),
    ]),
    
], width=10, style={'margin-top': '20px'})