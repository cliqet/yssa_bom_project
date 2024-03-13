from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from constants.styles import LABEL_STYLE, INPUT_STYLE, FORM_GROUP_HEADER_STYLE
from database.get_employees import get_employee_names

employee_names: list[dict] = get_employee_names()

def render(app: Dash) -> dbc.Col:
    return dbc.Col([
        # Requirement inputs section
        dbc.Row([
            # Cluster booth
            dbc.Col([
                dbc.Row(html.H3("Cluster Booth Requirements:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(),
                    dbc.Col(html.H3("Booth Count", style=LABEL_STYLE)),
                    dbc.Col(html.H3("Total Count", style=LABEL_STYLE)),
                ]),
                dbc.Row([
                    dbc.Col(html.H3("2 x 2 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='cluster-booth-2x2', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='cluster-total-2x2', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("2 x 3 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='cluster-booth-2x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='cluster-total-2x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("3 x 3 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='cluster-booth-3x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='cluster-total-3x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("3 x 4 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='cluster-booth-3x4', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='cluster-total-3x4', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("4 x 4 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='cluster-booth-4x4', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='cluster-total-4x4', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),

                # Prepared by section
                dbc.Row([
                    dbc.Col(html.H3("Prepared by:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Dropdown(
                            id='prepared-by',
                            options=employee_names,
                            value=employee_names[0].get('value'),
                            style=INPUT_STYLE
                        )
                    ),
                    # dbc.Col(dcc.Input(
                    #     id='prepared-bys', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    # )),
                    dbc.Col(
                        html.Button('Save', style={
                            'font-family': 'Tahoma',
                            'font-weight': 'bold',
                            'color': 'white',
                            'background-color': 'rgb(37,80,45)',
                            'border': 'none',
                            'padding': '10px 20px',
                            'border-radius': '5px',
                            'width': '200px'
                        })
                    )
                ], style={'margin-top': '30px', 'margin-bottom': '20px'})              
        ]),

            # Perimeter booth
            dbc.Col([
                dbc.Row(html.H3("Perimeter Booth Requirements:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(),
                    dbc.Col(html.H3("Booth Count", style=LABEL_STYLE)),
                    dbc.Col(html.H3("Total Count", style=LABEL_STYLE)),
                ]),
                dbc.Row([
                    dbc.Col(html.H3("2 x 2 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='perimeter-booth-2x2', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='perimeter-total-2x2', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("2 x 3 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='perimeter-booth-2x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='perimeter-total-2x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("3 x 3 meters", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='perimeter-booth-3x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    )),
                    dbc.Col(dcc.Input(
                        id='perimeter-total-3x3', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ])
            ])
        ]),
    ], style={'margin-top': '20px'})
