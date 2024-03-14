import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from components import side_panel


def render_layout() -> dbc.Container:
    return dbc.Container([
        dcc.Location(id='url', refresh=False),

        # Header
        dbc.Row([
            dbc.Col(html.Img(src='/assets/msdlogo.png', style={
                'width': '30vw',
                'height': '100%',
                'margin-left': '10px'
            }), width=2),

            dbc.Col(html.Div('JO-BOM System', style={
                'text-align': 'right',
                'font-size': '40px',
                'font-family': 'Tahoma',
                'font-weight': 'bold',
                'color': 'rgb(37,80,45)',
                'margin-right': '40px',
                'position': 'relative',
                'top': '-8px',
                'display': 'flex',
                'align-items': 'center',
                'justify-content': 'flex-end'
            }), width=10)

        ], style={
            'justify-content': 'space-between',
            'align-items': 'center',
            'border-bottom': '3px solid black',
            'padding': '0 40px',
            'box-sizing': 'border-box',
            'height': '100px'
        }),

        dbc.Row([
            dbc.Col(side_panel.render(), style={'flex': '1', 'padding': '0px'}),
            dbc.Col(dash.page_container, style={'flex': '6'})
        ], style={'display': 'flex'})

    ], fluid=True)
