from dash import Dash, html, dcc
from dash import dash_table
import dash_bootstrap_components as dbc

# Define Table
table_data = [
    {'ID': '1', 'Setup Type': 'Cluster', 'Name': 'Cluster 2x2 meters', 'Description': 'Standard Booth'},
    {'ID': '2', 'Setup Type': 'Cluster', 'Name': 'Cluster 2x3 meters', 'Description': 'Standard Booth'},
    {'ID': '3', 'Setup Type': 'Cluster', 'Name': 'Cluster 3x3 meters', 'Description': 'Standard Booth'},
    {'ID': '4', 'Setup Type': 'Cluster', 'Name': 'Cluster 3x4 meters', 'Description': 'Standard Booth'},
    {'ID': '5', 'Setup Type': 'Cluster', 'Name': 'Cluster 4x4 meters', 'Description': 'Standard Booth'},
    {'ID': '6', 'Setup Type': 'Perimeter', 'Name': 'Perimeter 2x2 meters', 'Description': 'Standard Booth'},
    {'ID': '7', 'Setup Type': 'Perimeter', 'Name': 'Perimeter 2x3 meters', 'Description': 'Standard Booth'},
    {'ID': '8', 'Setup Type': 'Perimeter', 'Name': 'Perimeter 3x3 meters', 'Description': 'Standard Booth'}    
] 

table_columns = [
    {'name': 'ID', 'id' : 'ID'},
    {'name': 'Setup Type', 'id' : 'Setup Type'},
    {'name': 'Name', 'id' : 'Name'},
    {'name': 'Description', 'id' : 'Description'},
]

def render() -> dbc.Col:
    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("Product List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='product-table',
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