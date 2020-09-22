import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
from dash.exceptions import PreventUpdate
import flask
from flask import Flask
server = Flask(__name__)
app = dash.Dash(__name__,
                server=server,
                meta_tags=[{
                    "content": "width=device-width"
                }],
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True
header = dbc.Jumbotron(
    [
        dbc.Container([
            html.H1("kristianjackson.page", className="display-3"),
            html.P("Find super deals at kristianjackson.page"),
            html.Hr(className="my-2"),
            html.P(" "
                   " "),
            html.P(" ")
        ],
                      fluid=True)  #end container
    ],
    fluid=True)  # end jumbo
footer = dbc.Jumbotron(
    [
        dbc.Container([
            html.H1("kristianjackson.page"),
            html.P(''),
            html.P("2287 Hope Cir", style={'text-align': 'center'}),
            html.P("Waldorf, MD 20601", style={'text-align': 'center'}),
            html.Hr(className="my-2"),
            html.P(''),
            html.P(
                'Copyright © 2020 kristianjackson.page - All Rights Reserved.')
        ],
                      fluid=True)  #end container
    ],
    fluid=True)  #end jumbo


def make_card(alert_message, color, cardbody, style_dict=None):
    return html.Div([
        html.P("  "),
        dbc.Card(
            [dbc.Alert(alert_message, color=color),
             dbc.CardBody(cardbody)])  #end card
        ,
        html.P("  "),
        html.P("  ")
    ])  #end div


def create_body(items):
    b = []
    for item in items:
        b.append(dbc.Col(make_card(item[0], "primary", item[1])))
    return b


def create_layout():
    layout = html.Div(
        style={
            'background-image': 'url("/assets/YOUR-BACKGROUND.jpg")',
            'background-position': 'center',
        },
        children=[
            header,
            dbc.Container(id='card-cont',
                          children=[dbc.Row(create_body(item_lists))],
                          style={
                              'background-color': 'white',
                          })  # end container
            ,
            footer
        ]  #end children
    )  #end div
    return layout


item_lists = [[
    "coca cola t-shirt",
    html.A(id='item1', href="item link", children=[html.Img(src="image link")])
],
              [
                  "coca cola t-shirt",
                  html.A(id='item2',
                         href="item 2 link",
                         children=[html.Img(src="image 2 link")])
              ]]  # end item list
app.layout = create_layout()
if __name__ == '__main__':
    app.run_server(debug=True)
