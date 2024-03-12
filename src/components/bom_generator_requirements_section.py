from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def render(app: Dash) -> dbc.Col:
    return dbc.Col([
    
# Cluster Booth Requirements
    dbc.Row([
        dbc.Col(html.H3("RM Count Summary List:", style={'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold', 'white-space': 'nowrap'}), width=12),
    ], className="mb-2"),

    dbc.Row([
        dbc.Col(html.Div("Post:", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='post-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='post-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='post-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),

    dbc.Row([
        dbc.Col(html.Div("Panel", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='panel-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='panel-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='panel-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),

    dbc.Row([
        dbc.Col(html.Div("Beam", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='beam-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='beam-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='beam-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),

    dbc.Row([
        dbc.Col(html.Div("Facia Length", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='facia-length-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='facia-length-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='facia-length-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),
    
    dbc.Row([
        dbc.Col(html.Div("Facia Width", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='facia-width-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='facia-width-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='facia-width-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),
    
    dbc.Row([
        dbc.Col(html.Div("Corner Length Beam:", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='corner-length-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='corner-length-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='corner-length-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),
    
    dbc.Row([
        dbc.Col(html.Div("Corner Width Beam", style={'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='corner-width-count', type='text', placeholder="count", style={'font-family': 'Tahoma', 'width': '80px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='corner-width-contingency', type='text', placeholder="%", style={'font-family': 'Tahoma', 'width': '40px'}), width=1),
        dbc.Col(width=1),
        dbc.Col(dcc.Input(id='corner-width-total', type='text', placeholder="total", style={'font-family': 'Tahoma', 'width': '100px'}), width=1),
    ], className="mb-2"),

html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),

    dbc.Row([
        dbc.Col(html.Div("Prepared by:", style={'font-family': 'Tahoma', 'font-weight': 'bold', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='prepared-by', type='text', placeholder="", style={'font-family': 'Tahoma', 'width': '210px'}), width=3),
        ], className="mb-2"),
    
    dbc.Row([
        dbc.Col(html.Div("Reviewed by:", style={'font-family': 'Tahoma', 'font-weight': 'bold', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='reviewed-by', type='text', placeholder="", style={'font-family': 'Tahoma', 'width': '210px'}), width=3),
        ], className="mb-2"),
    
    dbc.Row([
        dbc.Col(html.Div("Approved by:", style={'font-family': 'Tahoma', 'font-weight': 'bold', 'font-size': '18px'}), width=5),
        dbc.Col(dcc.Input(id='approved-by', type='text', placeholder="", style={'font-family': 'Tahoma', 'width': '210px'}), width=3),
        ], className="mb-2"),


    
], width=3, style={'margin-left': '-500px', 'margin-top': '230px'})