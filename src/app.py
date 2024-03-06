from dash import Dash
import dash_bootstrap_components as dbc

from layout import main_layout

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
application = app.server

app.layout = main_layout.render_layout(app)

if __name__ == '__main__':
    application.run(port=8080)