from datetime import datetime
from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
from constants.styles import (
    LABEL_STYLE, 
    INPUT_STYLE, 
    FORM_GROUP_HEADER_STYLE, 
    PAGE_HEADER_STYLE,
    BUTTON_STYLE
)
from database.get_employees import get_employee_names, get_employees, get_sales_executives


def render() -> dbc.Col:
    return dbc.Col([
        # First row
        dbc.Row([
            dbc.Col([
                # JO field row
                dbc.Row([
                    dbc.Col(
                        html.H3("JO No.:", style=PAGE_HEADER_STYLE)
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
                            # options=employee_names,
                            # value=employee_names[0].get('value'),
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
                        **BUTTON_STYLE,
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

        html.Hr(),
        
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
        ], style={'margin-top': '20px'}),
    
        html.Hr()
    ])

@callback([
        Output('sales-exec', 'options'),
        Output('sales-exec', 'value'),
    ], Input('url', 'pathname'))
def load_sales_executives(pathname):
    if pathname == '/':
        employee_names: list[dict] = get_employee_names(get_sales_executives)
        dropdown_values = [
            employee.get('value') for employee in employee_names
        ]
    else:
        employee_names = []
        dropdown_values = []

    return employee_names, dropdown_values