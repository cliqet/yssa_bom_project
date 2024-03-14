from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from constants.styles import (
    BUTTON_STYLE, 
    FORM_GROUP_HEADER_STYLE, 
    LABEL_STYLE,
    INPUT_STYLE
)
from database.get_employees import get_employee_names

employee_names: list[dict] = get_employee_names()


def render() -> dbc.Col:
    return dbc.Col([
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col(html.H3('RM Summary List', style=FORM_GROUP_HEADER_STYLE)),
                    dbc.Col(html.H3('Count (pc)', style=LABEL_STYLE)),
                    dbc.Col(html.H3('Contingency', style=LABEL_STYLE)),
                    dbc.Col(html.H3('Total Count (pc)', style=LABEL_STYLE)),
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Post:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='post-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='post-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='post-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Panel:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='panel-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='panel-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='panel-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Beam:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='beam-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='beam,-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='beam-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Facia Length:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='facia-length-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='facia-length-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='facia-length-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),
                
                dbc.Row([
                    dbc.Col(html.H3('Facia Width:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='facia-width-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='facia-width-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='facia-width-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Corner Length Beam:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='corner-length-beam-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='corner-length-beam-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='corner-length-beam-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

                dbc.Row([
                    dbc.Col(html.H3('Corner Width Beam:', style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(id='corner-width-beam-count', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='corner-width-beam-contingency', style=INPUT_STYLE, className='mb-2')),
                    dbc.Col(dcc.Input(id='corner-width-beam-total-count', style=INPUT_STYLE, className='mb-2'))
                ]),

            ], style={'flex': '3'}),

            dbc.Col(
                html.Button('Calculate BOM', style=BUTTON_STYLE),
                style={'flex': '1'}
            )
        ], style={'display': 'flex'}),

        html.Hr(),
        
        dbc.Row([
            dbc.Col(
                dbc.Row([
                    dbc.Col(dbc.Col(html.H3('Reviewed by:', style=LABEL_STYLE))),
                    dbc.Col(
                        dcc.Dropdown(
                            id='reviewer',
                            options=employee_names,
                            value=employee_names[0].get('value'),
                            style=INPUT_STYLE,
                            className='mb-2'
                        )
                    ),
                    dbc.Col()
                ], style={'display': 'flex', 'align-items': 'center'})
            ),
            dbc.Col(
                dbc.Row([
                    dbc.Col(dbc.Col(html.H3('Approved by:', style=LABEL_STYLE))),
                    dbc.Col(
                        dcc.Dropdown(
                            id='approver',
                            options=employee_names,
                            value=employee_names[0].get('value'),
                            style=INPUT_STYLE,
                            className='mb-2'
                        )
                    ),
                    dbc.Col(html.Button('Save', style=BUTTON_STYLE))
                ], style={'display': 'flex', 'align-items': 'center'})
            )
        ], style={'margin-top': '30px'})
    ], style={'margin-top': '30px'})