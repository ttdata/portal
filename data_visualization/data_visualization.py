import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
from dash.dependencies import Input, Output, State

############################################################################################################################################

df = pd.read_csv('testdata.csv')

## Creating values and lables for dropdown

options_list = []
for i in df['name'].unique():
    options_list.append({'label': i, 'value': i})
    


###############################################################################################################################################



def fig_generator(sample_data):
    sample_data = sample_data.reset_index(drop=True)
    sample_data.head()
    plot_data =[]
    columns=["Heart rate","temperature","glucose","blood_pressure_high","blood_pressure_low"]
    for i in columns:
        plot_data.append(go.Scatter(x=sample_data['time'], y=sample_data[i], name = i ))
        plot_layout = go.Layout(title = "   ")

    fig = go.Figure( data = plot_data ,layout = plot_layout)
    return(fig.data,fig.layout)
        
def fig(sample_data,i):
    sample_data = sample_data.reset_index(drop=True)
    sample_data.head()
    plot_data =[]
    plot_data.append(go.Scatter(x=sample_data['time'], y=sample_data[i], name = i ))
    plot_layout = go.Layout(title = "   ")

    fig = go.Figure( data = plot_data ,layout = plot_layout)
    return(fig.data,fig.layout)

def fig_pressure(sample_data,n,m):
    sample_data = sample_data.reset_index(drop=True)
    sample_data.head()
    plot_data =[]
    plot_data.append(go.Scatter(x=sample_data['time'], y=sample_data[n], name = n ))
    plot_data.append(go.Scatter(x=sample_data['time'], y=sample_data[m], name = m ))
    plot_layout = go.Layout(title = "   ")

    fig = go.Figure( data = plot_data ,layout = plot_layout)
    return(fig.data,fig.layout)  
### Dash board code 
    
app = dash.Dash()

### defining the HTML component


app.layout = html.Div(children=[html.Div("Welcome to the dashboard",style= {   "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"100%"
                                                      
                                                    }),
                       html.Div(dcc.Dropdown(id = "drop_down_1" ,options= options_list , value= 'Andy'
                                                       ),style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                      "display":"inline-block","width":"100%"
                                                      
                                                    }),
                       html.Div(children=[html.P(
                            id="map-title",
                            children = " Health Daily Data ",
                        ), html.Div(dcc.Graph(id ="plot_area"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"100%",
                                                                                                            
                                                    }),
                        html.Div(children=[html.P(
                            id="map-title2",
                            children = "  ",
                        ), html.Div(dcc.Graph(id ="plot_area2"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    }),
                        html.Div(children=[html.P(
                            id="map-title3",
                            children = "  ",
                        ), html.Div(dcc.Graph(id ="plot_area3"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    }),
                        html.Div(children=[html.P(
                            id="map-title4",
                            children = " ",
                        ), html.Div(dcc.Graph(id ="plot_area4"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    }),
                        html.Div(children=[html.P(
                            id="map-title5",
                            children = "  ",
                        ), html.Div(dcc.Graph(id ="plot_area5"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    }),   
                        html.Div(children=[html.P(
                            id="map-title6",
                            children = "  ",
                        ), html.Div(dcc.Graph(id ="plot_area6"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    }),
                        html.Div(children=[html.P(
                            id="map-title7",
                            children = "  ",
                        ), html.Div(dcc.Graph(id ="plot_area7"))
                                                       ],style= {
                                                      "color": "black",
                                                      "text-align": "center","background-color": "white",
                                                     "display":"inline-block","width":"50%",
                                                                                                            
                                                    })                                                                                                                                                                   
                                                    ],
                      
              style={"width":"100%",'paffing':24})

## Creating callback buttons

@app.callback(Output("plot_area", 'figure'),           
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ]   
    trace,layout = fig_generator(sample_data)
    
    return {
        'data': trace,
        'layout':layout
    }

@app.callback(Output("plot_area2", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ]  
    trace,layout = fig(sample_data,'height')
    
    return {
        'data': trace,
        'layout':go.Layout(title = "height")
    }

@app.callback(Output("plot_area3", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ] 
    trace,layout = fig(sample_data,'weight')
    
    return {
        'data': trace,
        'layout':go.Layout(title = "weight")
    }

@app.callback(Output("plot_area4", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ] 
    trace,layout = fig(sample_data,'Heart rate')
    
    return {
        'data': trace,
        'layout':go.Layout(title = "Heart rate")
    }

@app.callback(Output("plot_area5", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ] 
    trace,layout = fig(sample_data,'temperature')
    
    return {
        'data': trace,
        'layout':go.Layout(title = "temperature")
    }

@app.callback(Output("plot_area6", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ] 
    trace,layout = fig(sample_data,'glucose')
    
    return {
        'data': trace,
        'layout':go.Layout(title = "glucose")
    }

@app.callback(Output("plot_area7", 'figure'),            
              [Input("drop_down_1", "value")])

def updateplot(input_cat):
    sample_data = df[df["name"] == input_cat ] 
    trace,layout = fig_pressure(sample_data,'blood_pressure_high','blood_pressure_low')
    return {
        'data': trace,
        'layout':go.Layout(title = "blood pressure high and blood pressure low")
    }
if __name__=='__main__':
    app.run_server()
	
	
###################################################################################################################################


