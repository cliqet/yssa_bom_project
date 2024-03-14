from dash import Dash, html, dcc
from dash import dash_table
import dash_bootstrap_components as dbc

# Define Table
# TODO: get data from db
table_data = [
    {'ID': '1', 'Employee Name': 'Winlove Campos', 'Department': 'Sales', 'Position Title': 'Sales & Marketing Head', 'Contact No.': '9159785683', 'Email Address': 'msd.winlove@gmail.com'},
    {'ID': '2', 'Employee Name': 'Dennis Domingo', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9458502261', 'Email Address': 'denisdomingo72@gmail.com'},
    {'ID': '3', 'Employee Name': 'Keren Huarde', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9953101809', 'Email Address': 'kbh.msdgodspeed@gmail.com'},
    {'ID': '4', 'Employee Name': 'Elvis Lorenzo', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9277441819', 'Email Address': 'elvisdlorenzo07@gmail.com'},
    {'ID': '5', 'Employee Name': 'Cecil Derama', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9291661163', 'Email Address': 'mgd.msdgodspeed@gmail.com'},
    {'ID': '6', 'Employee Name': 'Joshua Martinez', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9281820017', 'Email Address': 'mjm.msdgodspeed@gmail.com'},
    {'ID': '7', 'Employee Name': 'Lester Visitacion', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9456135614', 'Email Address': 'ljv.msdgodspeed@gmail.com'},
    {'ID': '8', 'Employee Name': 'Alma Guilalas', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9458317497', 'Email Address': 'alma.msd09@gmail.com'},
    {'ID': '9', 'Employee Name': 'Shaica Naoe', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9777187698', 'Email Address': 'shaicanaoe.msd@gmail.com'},
    {'ID': '10', 'Employee Name': 'Gem Guillermo', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9325252056', 'Email Address': 'gem.msdgodspeed2022@gmail.com'},
    {'ID': '11', 'Employee Name': 'Jesus Bigcas', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9777187698', 'Email Address': 'bjbigcas.msd@gmail.com'},
    {'ID': '12', 'Employee Name': 'Loremer Elbano', 'Department': 'Sales', 'Position Title': 'Sales Executive', 'Contact No.': '9651729833', 'Email Address': 'lhelbano.msdgodspeed@gmail.com'},
    {'ID': '13', 'Employee Name': 'Jean Mae Cayona', 'Department': 'Sales', 'Position Title': 'Freelance Sales', 'Contact No.': '9052443406', 'Email Address': 'jeanmae.msd@gmail.com'},
    {'ID': '14', 'Employee Name': 'Gizelle Domingo', 'Department': 'Operations', 'Position Title': 'Operations Head', 'Contact No.': '9175750226', 'Email Address': 'gizelle.msd@gmail.com'},
    {'ID': '15', 'Employee Name': 'Gabriel Campos', 'Department': 'Purchasing', 'Position Title': 'Purchasing Officer', 'Contact No.': '9064631849', 'Email Address': ''},
    {'ID': '16', 'Employee Name': 'Christine Cunanan', 'Department': 'Finance', 'Position Title': 'Finance Head', 'Contact No.': '9159721081', 'Email Address': 'mcj.msd@gmail.com'},
    {'ID': '17', 'Employee Name': 'Sherwin Mapa', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '18', 'Employee Name': 'Raymond Bigo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '19', 'Employee Name': 'Nikki Nariz', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '20', 'Employee Name': 'JJ Macahya', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '21', 'Employee Name': 'Rubert Atanacio', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '22', 'Employee Name': 'Julianne Fellone', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '23', 'Employee Name': 'Beth Garbo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '24', 'Employee Name': 'Dolor Domingo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '25', 'Employee Name': 'Melchor Domingo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '26', 'Employee Name': 'Eric Estrada', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '27', 'Employee Name': 'Precious Nim', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '28', 'Employee Name': 'Angelyn Domingo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '29', 'Employee Name': 'Pepe Bejarin', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '30', 'Employee Name': 'Hennessy Balinggit', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '31', 'Employee Name': 'Kristel Tellerva', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '32', 'Employee Name': 'Ernesto Suba', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '33', 'Employee Name': 'Ferdimar ', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '34', 'Employee Name': 'Maricel De Rama', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '35', 'Employee Name': 'Gerhard Gaston', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '36', 'Employee Name': 'Bernedeth Sabuero', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '37', 'Employee Name': 'Raymond Barja', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '38', 'Employee Name': 'Joel Ranes', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '39', 'Employee Name': 'Penefrancia ', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '40', 'Employee Name': 'Bernard Jordan', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '41', 'Employee Name': 'Ernani Balino', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '42', 'Employee Name': 'Ryan Domingo', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '43', 'Employee Name': 'Jay Valdez', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '44', 'Employee Name': 'Susan Ratcho', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '45', 'Employee Name': 'Henry Alcantara', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '46', 'Employee Name': 'Felimon Doron', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '47', 'Employee Name': 'Allen Andrada', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '48', 'Employee Name': 'Gem Cunanan', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '49', 'Employee Name': 'Jairus Nariz', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '50', 'Employee Name': 'Levi Capitly', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '51', 'Employee Name': 'Arnold Puenliona', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '52', 'Employee Name': 'Michael Pinon', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '53', 'Employee Name': 'Loremer Elbano', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '54', 'Employee Name': 'Raul Busa', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''},
    {'ID': '55', 'Employee Name': 'Rose Uno', 'Department': '', 'Position Title': '', 'Contact No.': '', 'Email Address': ''}

] 

table_columns = [
    {'name': 'ID', 'id' : 'ID'},
    {'name': 'Employee Name', 'id' : 'Employee Name'},
    {'name': 'Department', 'id' : 'Department'},
    {'name': 'Position title', 'id' : 'Position Title'},
    {'name': 'Contact No.', 'id' : 'Contact No.'},
    {'name': 'Email Address', 'id' : 'Email Address'},
    
]

def render() -> dbc.Col:
    return dbc.Col([
    dbc.Row([
        dbc.Col(html.H3("Employee List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
    ]),

    dbc.Row([
        dbc.Col(dash_table.DataTable(
            id='employee-table',
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