from dash import Dash, html, dcc
import dash_table
import dash_bootstrap_components as dbc

# Define Table
table_data = [
    {'JO Date Created': '',
     'JO No.': '',
     'Sales Executive': '',
     'Event Name': '',
     'Venue': '',
     'Event Start Date': '',
     'Event End Date': '',
     'BOM Preparer': '',
     'BOM Reviewer': '',
     'BOM Approver': '',     
     } for _ in range(50)
] 

table_columns = [
    {'name': 'JO Date Created', 'id' : 'JO Date Created'},
    {'name': 'JO No.', 'id' : 'JO No.'},
    {'name': 'Sales Executive', 'id' : 'Sales Executive'},
    {'name': 'Event Name', 'id' : 'Event Name'},
    {'name': 'Venue', 'id' : 'Venue'},
    {'name': 'Event Start Date', 'id' : 'Event Start Date'},
    {'name': 'Event End Date', 'id' : 'Event End Date'},
    {'name': 'BOM Preparer', 'id' : 'BOM Preparer'},
    {'name': 'BOM Reviewer', 'id' : 'BOM Reviewer'},
    {'name': 'BOM Approver', 'id' : 'BOM Approver'},
]

def render(app: Dash) -> dbc.Col:
    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("JO-BOM List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='jobom-table',
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