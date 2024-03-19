from dash import html
from dash import dash_table, callback, Output, Input
import dash_bootstrap_components as dbc
from constants.styles import TABLE_HEADER_STYLE, TABLE_CELL_STYLE, TABLE_STYLE
from database.get_employees import get_employees
from models.employee import Employee


def render() -> dbc.Col:
    table_columns = [
        {'name': 'ID', 'id': 'ID'},
        {'name': 'Employee Name', 'id': 'Employee Name'},
        {'name': 'Department', 'id': 'Department'},
        {'name': 'Position title', 'id': 'Position Title'},
        {'name': 'Contact No.', 'id': 'Contact No.'},
        {'name': 'Email Address', 'id': 'Email Address'},

    ]
    
    return dbc.Col([
        dbc.Row([
            dbc.Col(html.H3("Employee List:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), className="d-flex align-items-center"),
        ]),

        dbc.Row([
            dbc.Col(dash_table.DataTable(
                id='employee-table',
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

@callback(Output('employee-table', 'data'), Input('url', 'pathname'))
def load_employees(pathname):
    if pathname == '/employeelist':
        employees: list[Employee] = get_employees()
        table_data = [
            {
                'ID': employee.employee_id,
                'Employee Name': f'{employee.first_name} {employee.last_name}',
                'Department': employee.department_name,
                'Position Title': employee.employee_position_title,
                'Contact No.': employee.contact_no,
                'Email Address': employee.email_address
            }
            for employee in employees
        ]
    else:
        table_data = []

    return table_data
