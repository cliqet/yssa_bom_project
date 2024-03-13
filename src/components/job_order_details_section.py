from datetime import datetime
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from constants.styles import LABEL_STYLE, INPUT_STYLE, FORM_GROUP_HEADER_STYLE
from database.get_employees import get_employee_names

employee_names: list[dict] = get_employee_names()

def render(app: Dash) -> dbc.Col:
    return dbc.Col([
        # First row
        dbc.Row([
            dbc.Col([
                # JO field row
                dbc.Row([
                    dbc.Col(
                        html.H3("JO No.:", style={
                            'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}
                        )
                    ),
                    dbc.Col(
                        dcc.Input(
                            id='jo-no', 
                            type='text', 
                            placeholder="Enter J.O. Number",
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ]),

                # Sales executive field row
                dbc.Row([
                    dbc.Col(
                        html.H3("Sales Executive:", style=LABEL_STYLE)
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='sales-exec',
                            options=employee_names,
                            value=employee_names[0].get('value'),
                            style=INPUT_STYLE,
                            className='mb-2'
                        )
                    )
                ]),

                # Date created field row
                dbc.Row([
                    dbc.Col(
                        html.H3("Date Created:", style=LABEL_STYLE)
                    ),
                    dbc.Col(
                        dcc.Input(
                            id='date-created', 
                            type='date',
                            value=datetime.now().strftime('%Y-%m-%d'), 
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ])
            ]),

            # Column for upload button
            dbc.Col(
                dcc.Upload(
                    id='upload-layout',
                    children=html.Button('Upload Layout', style={
                        'font-family': 'Tahoma',
                        'font-weight': 'bold',
                        'color': 'white',
                        'background-color': 'rgb(37,80,45)',
                        'border': 'none',
                        'padding': '10px 20px',
                        'border-radius': '5px',
                        'display': 'flex',
                        'margin-left': 'auto'
                    }),
                    style={
                        'borderStyle': 'none',
                        'display': 'inline-block',
                        'width': '100%',
                        'height': 'auto'
                    }
                )
            )
        ]),

        # Second row
        dbc.Row([
            # Event details
            dbc.Col([
                dbc.Row(html.H3("Event Details:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Event Name", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='event-name', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Venue:", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='venue', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Event Start Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='event-start-date', 
                            type='date',
                            value=datetime.now().strftime('%Y-%m-%d'), 
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Event End Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='event-end-date', 
                            type='date',
                            value=datetime.now().strftime('%Y-%m-%d'), 
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ])
            ]),
            
            # Client details
            dbc.Col([
                dbc.Row(html.H3("Client Details:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Company Name:", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='client-company-name', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Contact Person:", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='client-contact-person', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Contact Number:", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='client-contact-number', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Email Address:", style=LABEL_STYLE)),
                    dbc.Col(dcc.Input(
                        id='client-email', type='text', placeholder="", style=INPUT_STYLE, className='mb-2'
                    ))
                ])
            ]),

            # Setup schedule
            dbc.Col([
                dbc.Row(html.H3("Setup Schedule:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Ingress Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='ingress-date', 
                            type='date',
                            value=datetime.now().strftime('%Y-%m-%d'), 
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Ingress Time:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='ingress-time', 
                            type='time',
                            value=datetime.strptime('12:00', '%H:%M').strftime('%H:%M'),
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Egress Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='egress-date', 
                            type='date',
                            value=datetime.now().strftime('%Y-%m-%d'), 
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Egress Time:", style=LABEL_STYLE)),
                    dbc.Col(
                        dcc.Input(
                            id='egress-time', 
                            type='time',
                            value=datetime.strptime('12:00', '%H:%M').strftime('%H:%M'),
                            style=INPUT_STYLE, 
                            className='mb-2'
                        )
                    )
                ])
            ]),
        ], style={'margin-top': '20px'})
    ])
