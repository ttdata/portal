# -*- coding: utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        dcc.Location(id='location'),
        html.Nav(
            className='navbar navbar-dark bg-dark',
            children=[
                html.Div(
                    className='container',
                    children=[
                        html.Span(
                            className='navbar-brand mb-0 h1',
                            children='TT-Data')
                    ])
            ]),
        html.Div(
            className='jumbotron jumbotron-fluid',
            children=[
                html.Div(
                    className='container',
                    children=[
                        html.H1(
                            className='display-4',
                            children='TT Data'),
                        html.P(
                            className='lead',
                            children='a data visualize project based on python dash.')
                    ])
            ]),
        html.Div(
            className='container',
            children=[
                html.Div(
                    className='row',
                    children=[
                        html.Div(
                            className='col-6',
                            children=[
                                html.Div(
                                    className='card',
                                    children=[
                                        html.Img(
                                            className='card-img-top w-25 ml-auto mr-auto mt-3',
                                            src='/assets/api.svg'),
                                        html.Div(className='card-body',
                                                 children=[
                                                     html.H5(className='card-title',
                                                             children='API'),
                                                     html.P(className='card-text',
                                                            children='show api demo'),
                                                     html.A(
                                                         id='api',
                                                         className='btn btn-dark btn-block',
                                                         href='#',
                                                         children='enter')
                                                 ])
                                    ])
                            ]),
                        html.Div(
                            className='col-6',
                            children=[
                                html.Div(
                                    className='card',
                                    children=[
                                        html.Img(
                                            className='card-img-top w-25 ml-auto mr-auto mt-3',
                                            src='/assets/visual.svg'),
                                        html.Div(className='card-body',
                                                 children=[
                                                     html.H5(className='card-title',
                                                             children='Visualization'),
                                                     html.P(className='card-text',
                                                            children='show visualization demo'),
                                                     html.A(
                                                         id='visual',
                                                         className='btn btn-dark btn-block',
                                                         children='enter',
                                                         href='#'
                                                     )
                                                 ])
                                    ])
                            ])
                    ]),
            ])
    ])


@app.callback(
    dash.dependencies.Output(component_id='api', component_property='href'),
    [dash.dependencies.Input(component_id='location',
                             component_property='search')]
)
def getUrlParams(search):
    return 'http://127.0.0.1:10087' + str(search)


@app.callback(
    dash.dependencies.Output(component_id='visual', component_property='href'),
    [dash.dependencies.Input(component_id='location',
                             component_property='search')]
)
def getUrlParams(search):
    return 'http://127.0.0.1:10088' + str(search)


if __name__ == '__main__':
    app.run_server(port=10086)
