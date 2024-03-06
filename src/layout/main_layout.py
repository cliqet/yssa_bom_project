from dash import Dash, html
import dash_bootstrap_components as dbc
from components import side_panel, main_content


def render_layout(app: Dash) -> dbc.Container:
    return dbc.Container([
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
            'height': '100px',
            'margin-bottom': '3px'
        }),

        dbc.Row([
            side_panel.render(app),
            main_content.render(app)
        ])

    ], fluid=True)
