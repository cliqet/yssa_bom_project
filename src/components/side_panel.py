from dash import Dash, dcc
import dash_bootstrap_components as dbc


def render(app: Dash) -> dbc.Col:
    return dbc.Col([
        dcc.Link('Job Order', href='/joborder', id='joborder', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif',
            'color': 'black',
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

        dcc.Link('BOM Generator', href='/bomgenerator', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif',
            'color': 'black',
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

        dcc.Link('JO-BOM List', href='/jobomlist', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif',
            'color': 'black',
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

        dcc.Link('Product List', href='/productlist', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif', 
            'color': 'black', 
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

        dcc.Link('Client List', href='/clientlist', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif',
            'color': 'black',
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

        dcc.Link('Employee List', href='/employeelist', style={
            'display': 'block',
            'margin': '8px',
            'font-size': '20px',
            'font-family': 'Arial, sans-serif',
            'color': 'black',
            'text-decoration': 'none',
            'padding': '5px',
            'background-color': 'rgb(216,231,214)'
        }),

    ], style={
        'border-right': '3px solid black',
        'border-left': '3px solid black',
        'border-bottom': '3px solid black',
        'height': 'calc(100vh)',
        'width': '200px',
        'display': 'inline-block',
        'vertical-align': 'top',
        'padding': '8px',
        'background-color': 'rgb(216,231,214)',
        'box-sizing': 'border-box',
    }, width=2)
