from dash import Dash, html, dcc
import dash_bootstrap_components as dbc


def render(app: Dash) -> dbc.Col:
    return dbc.Col(html.H3("Requirements Sections"))
    # return dbc.Col([

    #     # Cluster Booth Requirements
    #     dbc.Row([
    #         dbc.Col(html.H3("Cluster Booth Requirements:", style={
    #             'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold', 'white-space': 'nowrap'}), width=12),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("2x2 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='2x2-cluster-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='2x2-cluster-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("2x3 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='2x3-cluster-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='2x3-cluster-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("3x3 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='3x3-cluster-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='3x3-cluster-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("3x4 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='3x4-cluster-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='3x4-cluster-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("4x4 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='4x4-cluster-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='4x4-cluster-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     html.Br(),

    #     # Perimeter Booth Requirements
    #     dbc.Row([
    #         dbc.Col(html.H3("Perimeter Booth Requirements:", style={
    #             'font-family': 'Tahoma', 'font-size': '25px', 'font-weight': 'bold', 'white-space': 'nowrap'}), width=12),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("2x2 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='2x2-perimeter-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='2x2-perimeter-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("2x3 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='2x3-perimeter-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='2x3-perimeter-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     dbc.Row([
    #         dbc.Col(html.Div("3x3 meters:", style={
    #             'font-family': 'Tahoma', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='3x3-perimeter-count', type='text', placeholder="booth count",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #         dbc.Col(width=1),
    #         dbc.Col(dcc.Input(id='3x3-perimeter-total', type='text', placeholder="total",
    #                           style={'font-family': 'Tahoma', 'width': '100px'}), width=3),
    #     ], className="mb-2"),

    #     html.Br(),
    #     html.Br(),
    #     html.Br(),
    #     html.Br(),
    #     html.Br(),
    #     html.Br(),
    #     html.Br(),
    #     html.Br(),

    #     dbc.Row([
    #         dbc.Col(html.Div("Prepared by:", style={
    #             'font-family': 'Tahoma', 'font-weight': 'bold', 'font-size': '18px'}), width=5),
    #         dbc.Col(dcc.Input(id='prepared-by', type='text', placeholder="",
    #                           style={'font-family': 'Tahoma', 'width': '210px'}), width=3),
    #     ], className="mb-2")
    # ], width=2, style={'margin-left': '-500px', 'margin-top': '230px'})
