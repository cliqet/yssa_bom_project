from dash import html
from dash import dash_table, callback, Output, Input
import dash_bootstrap_components as dbc
from constants.styles import TABLE_HEADER_STYLE, TABLE_CELL_STYLE, TABLE_STYLE
from database.get_products import get_products
from models.product import Product


def render() -> dbc.Col:
    table_columns = [
        {'name': 'ID', 'id': 'ID'},
        {'name': 'Setup Type', 'id': 'Setup Type'},
        {'name': 'Name', 'id': 'Name'},
        {'name': 'Description', 'id': 'Description'},
    ]

    return dbc.Col([
        dbc.Row([
            dbc.Col(html.H3("Product List:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), className="d-flex align-items-center"),
        ]),

        dbc.Row([
            dbc.Col(dash_table.DataTable(
                id='product-table',
                columns=table_columns,
                # data=table_data,
                editable=False,
                page_size=30,
                style_table=TABLE_STYLE,
                style_cell=TABLE_CELL_STYLE,
                style_header=TABLE_HEADER_STYLE,
            ), width=12),
        ]),

    ], width=10, style={'margin-top': '20px', 'height': '100%', 'width': '100%'})

@callback(Output('product-table', 'data'), Input('url', 'pathname'))
def load_products(pathname):
    if pathname == '/productlist':
        products: list[Product] = get_products()
        table_data = [
            {
                'ID': product.product_id,
                'Setup Type': product.setup_type,
                'Name': product.name,
                'Description': product.description
            }
            for product in products
        ]
    else:
        table_data = []

    return table_data
