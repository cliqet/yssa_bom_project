from datetime import datetime
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from constants.styles import (
    PAGE_HEADER_STYLE, 
    INPUT_STYLE, 
    LABEL_STYLE,
    FORM_GROUP_HEADER_STYLE
)
from database.get_job_orders import get_job_order_numbers

job_order_numbers: list[dict] = get_job_order_numbers()

job_order_details = {
    'event_name': 'TEST EVENT',
    'venue': 'TEST VENUE',
    'start_date': 'TEST START DATE',
    'end_date': 'TEST END DATE',
    'company': 'TEST COMPANY',
    'contact_person': 'TEST_CONTACT_PERSON',
    'contact_number': 'TEST_CONTACT_NUMBER',
    'email': 'TEST_EMAIL',
    'ingress_date': 'TEST_INGRESS_DATE',
    'ingress_time': 'TEST_INGRESS_TIME',
    'egress_date': 'TEST_EGRESS_DATE',
    'egress_time': 'TEST_EGRESS_TIME'
}


def render(app: Dash) -> dbc.Col:
    return dbc.Col([
        dbc.Row([
            dbc.Col(html.H3("Standard Booth BOM", style=PAGE_HEADER_STYLE)),
            dbc.Col(
                dbc.Row([
                    dbc.Col(
                        html.H3("JO No.:", style={
                            **PAGE_HEADER_STYLE,
                            'text-align': 'right'
                        })
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='job-orders',
                            options=job_order_numbers,
                            value=job_order_numbers[0].get('value'),
                            style=INPUT_STYLE
                        )
                    )
                ])
            )
        ]),

        dbc.Row([
            # Event details
            dbc.Col([
                dbc.Row(html.H3("Event Details:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Event Name", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('event_name'),
                            id="event-name-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Venue:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('venue'),
                            id="venue-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Event Start Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('start_date'),
                            id="event-start-date-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Event End Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('end_date'),
                            id="event-end-date-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ])
            ]),
            
            # Client details
            dbc.Col([
                dbc.Row(html.H3("Client Details:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Company Name:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('company'),
                            id="company-name-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Contact Person:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('contact_person'),
                            id="event-contact-person-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Contact Number:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('contact_number'),
                            id="event-contact-number-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Email Address:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('email'),
                            id="event-email-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ])
            ]),

            # Setup schedule
            dbc.Col([
                dbc.Row(html.H3("Setup Schedule:", style=FORM_GROUP_HEADER_STYLE)),
                dbc.Row([
                    dbc.Col(html.H3("Ingress Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('ingress_date'),
                            id="event-ingress-date-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Ingress Time:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('ingress_time'),
                            id="event-ingress-time-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Egress Date:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('egress_date'),
                            id="event-egress-date-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ]),
                dbc.Row([
                    dbc.Col(html.H3("Egress Time:", style=LABEL_STYLE)),
                    dbc.Col(
                        html.H3(
                            job_order_details.get('egress_time'),
                            id="event-egress-time-value", 
                            style=LABEL_STYLE,
                            className="mb-2"
                        )
                    )
                ])
            ]),
        ], style={'margin-top': '20px'})
    ])