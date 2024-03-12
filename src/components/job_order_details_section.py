from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def render(app: Dash) -> dbc.Col:
    return dbc.Col([
        dbc.Row([
            dbc.Col(html.H3("JO No.:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=2, className="d-flex align-items-center"),
            dbc.Col(dcc.Input(id='jo-no', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}, className='mb-2'), width=4),
        ]),

        dbc.Row([
            dbc.Col(html.H3("Sales Executive:", style={
                    'font-family': 'Tahoma', 'font-size': '18px', }), width=2, className="d-flex align-items-center"),
            dbc.Col(dcc.Input(id='sales-exec', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}, className='mb-2'), width=4),
        ]),

        dbc.Row([
            dbc.Col(html.H3("Date Created:", style={
                    'font-family': 'Tahoma', 'font-size': '18px', }), width=2, className="d-flex align-items-center"),
            dbc.Col(dcc.Input(id='date-created', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}, className='mb-2'), width=4),
        ]),

        # Upload Button
        dbc.Row(
            dbc.Col(
                dcc.Upload(id='upload-layout',
                           children=html.Button('Upload Layout', style={
                               'font-family': 'Tahoma',
                               'font-weight': 'bold',
                               'color': 'white',
                               'background-color': 'rgb(37,80,45)',
                               'border': 'none',
                               'padding': '10px 20px',
                               'border-radius': '5px',
                           }
                           ),
                           style={
                               'borderStyle': 'none',
                               'display': 'inline-block',
                               'width': 'auto',
                               'height': 'auto'
                           }
                           ),
                width={'size': 3, 'offset': 1},
            ),
            className="d-flex justify-content-end"
        ),

        html.Br(),
        html.Br(),
        html.Br(),

        # Event Details Section
        dbc.Row([
            dbc.Col(html.H3("Event Details:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=12),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Event Name:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='event-name', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Venue:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='venue', type='text', placeholder="", style={
                'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Event Start Date:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='event-start-date', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Event End Date:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='event-end-date', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        html.Br(),

        # Client Details Section
        dbc.Row([
            dbc.Col(html.H3("Client Details:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=12),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Company Name:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='company-name', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Contact Person:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='contact-person', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Contact No.:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='contact-no', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Email Address:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='email-address', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        html.Br(),

        # Setup Schedule Section
        dbc.Row([
            dbc.Col(html.H3("Setup Schedule:", style={
                'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold'}), width=12),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Ingress Date:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='ingress-date', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Ingress Time", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='ingress-time', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Egress Date:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='egress-date', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

        dbc.Row([
            dbc.Col(html.Div("Egress Time:", style={
                'font-family': 'Tahoma', 'font-size': '18px'}), width=2),
            dbc.Col(dcc.Input(id='egress-time', type='text', placeholder="",
                              style={'font-family': 'Tahoma', 'width': '300px'}), width=10),
        ], className="mb-2"),

    ], width=8)
