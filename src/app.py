from dash import Dash
import dash_bootstrap_components as dbc
from layout import main_layout
from config.configuration import config
from database.postgres import initialize_sql_database

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
application = app.server

initialize_sql_database()

app.layout = main_layout.render_layout()

if __name__ == '__main__':
    application.run(host=config.application.host, port=config.application.port, debug=config.application.debug)