import dash
# import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_auth
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
import requests
import json
import time 

# df = pd.read_csv("/Users/yangyuan/Documents/ttdata/dash/dash_sample.csv")
# DEVICEID = 'test_20200625'
# URL = 'http://108.48.52.183:7061'
# d_type = 2

# # def validate(URL, d_type):

# URL_upload = URL + '/uploaddata'
# URL_uploadbatch = URL + '/uploaddata'
# URL_get = URL + '/getshareddata'

# #register testing
# payload = {
# "device_id":DEVICEID,
# "category": "test"
# }

# #Passing payload as dict
# response_register= requests.post(URL_register, data = payload, timeout = 5)
# register_result = json.loads(response_register.text)

# #893f0bb8571bc3b51257cea17b88b206457864b3ef98bdf68a45f1bf907fe012
# appkey = None
# if register_result["data"]:
#      appkey = register_result["data"]
# print(appkey)

# # upload testing 
# payload = {"data_type": d_type, 
#             "device_id": DEVICEID, 
#             "key": "date|province_state|county|country_region", 
#             "device_data": [{
#                                 "date": "2020-05-08", 
#                                 "province_state": "ON",
#                                 "country_region": "Canada", 
#                                 "county": "Toronto",
#                                 "last_update": "2020-05-03T10:43:02",
#                                 "confirmed":370,
#                                 "deaths": 84,
#                                 "recovered": 14,
#                                 "latitude":43.6532,
#                                 "longitude": 79.3832
#                     }]   
#         }
#     #Passing payload as dict
# response_upload = requests.post(URL_upload, 
#     json = payload, 
#     timeout = 5, 
#     headers = {"appkey" : appkey})
# upload_result = json.loads(response_upload.text)

# print(upload_result['message'])


# time.sleep(5)
# # get data testing
# query = {"data_type": d_type, "device_id": DEVICEID}
# response_get = requests.get(URL_get, params=query, timeout = 5, headers = {"appkey" : appkey})
# get_result = json.loads(response_get.text)

# print(get_result['message'])


# Program to build the dashbaord
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'yang': 'yang'
}

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# validate('http://108.48.52.183:7061',2)

app.layout = html.Div([
    html.H1(children='TTDATA API Test'),

    html.Div(children='''
        A web application to test the TTDATA servers
    '''),
    #register input
    html.Label(["Selected API",
    dcc.Dropdown(
                id='API_selection',
                options=[{'label': 'RS serve: http://ttdata.life:7061', 'value': 'http://ttdata.life:7061'},
                {'label': 'ZN serve: http://112.17.170.154:7061', 'value': 'http://112.17.170.154:7061'},
                {'label': 'IXINBUY serve: http://ixinbuy.com:7061', 'value': 'http://ixinbuy.com:7061'},
                ],
                value='http://ttdata.life:7061'
            )]),

    html.H1(children='Register API'),
    dbc.FormGroup([dbc.Label("Device ID"), dbc.Input(id = "Input_device_id", placeholder="Input the device id here...", type="text")]),
    dbc.FormGroup([dbc.Label("Category"), dbc.Input(id = "Input_category", placeholder="Input the category here...", type="text")]),
    dbc.Button("Register", id = "reg_submit_button", color="primary", className="mr-1"),
    html.Br(),
    html.P(id="reg_output"),

    #Upload input
    html.H1(children='Uploaddata API'),
    
    dcc.Dropdown(
                id='dtype_selection',
                options=[{'label': 'Type 1', 'value': 1},
                {'label': 'Type 2', 'value': 2},
                {'label': 'Type 1001', 'value': 3},
                ],
                value='1'),
    dbc.FormGroup([dbc.Label("Key field"), dbc.Input(id = "Input_keyfield", placeholder="Input the key field of payload", type="text")]),
    dbc.FormGroup([dbc.Label("Payload"), dbc.Textarea(id = "Input_payload", placeholder="Input the payload", style = {'width': '30%',
        'height': '600%'},)]),
    html.Br(),
    dbc.Button("Uplaod", id = "upload_submit_button", color="primary", className="mr-1"),
    html.P(id="upload_output"),

    #Input of get ownerdata
    html.Br(),
    html.H1(children='Get owner data'),
    dbc.FormGroup([dbc.Label("Input the Owner of data"), dbc.Input(id = "Input_owner", placeholder="Input the owner of data", type="text")]),
    dbc.Button("Get the owner's data", id = "getowner_submit_button", color="primary", className="mr-1"),
    html.P(id="getowner_output"),

    #Inputs of requestsharing 
    html.Br(),
    html.H1(children='requestsharing'),
    dbc.FormGroup([dbc.Label("Payload"), dbc.Textarea(id = "Input_request", debounce = True, placeholder="requst for sharing", style = {'width': '30%',
        'height': '600%'},)]),
    #dbc.FormGroup([dbc.Label("Prepare the requesting"), dbc.Input(id = "Input_request", placeholder="requst for sharing", type="text")]),
    dbc.Button("Submit the request", id = "request_submit_button", color="primary", className="mr-1"),
    html.P(id="requestsharing_output"),

    #Inputs of getrequest
    html.Br(),
    html.H1(children='Owner get request and confirm the sharing'),
    dbc.FormGroup([dbc.Label("The owner of data"), dbc.Input(id = "Input_owner_request", placeholder="Input the owner of data here...", type="text")]),
    dbc.Button("Onwer get the request", id = "getrequest_submit_button", color="primary", className="mr-1"),
    html.P(id="getrequest_output"),
    html.Br(),
    dbc.FormGroup([dbc.Label("Payload"), dbc.Textarea(id = "Input_approve", debounce = True, placeholder="Input the approved load", style = {'width': '30%',
        'height': '600%'},)]),
    dbc.Button("Approve request", id = "approve_submit_button", color="primary", className="mr-1"),
    html.P(id="approverequest_output"),


    #get request data
    html.Br(),
    html.H1(children='Viewer get sharing data'),
    dbc.FormGroup([dbc.Label("Input the Viewer of data"), dbc.Input(id = "Input_viewer", placeholder="Input the viewer of data", type="text")]),
    dbc.Button("Get the shared data", id = "getshareddata_submit_button", color="primary", className="mr-1"),
    html.P(id="getshareddata_output"),
])
# register device id call function
@app.callback(
        Output("reg_output", "children"), 
        [Input("reg_submit_button", "n_clicks")],
        [State("API_selection", "value"),
        State("Input_device_id", "value"),
        State("Input_category", "value")])
def send_register_request(n_clicks, URL, DEVICEID, category):
    URL_register = URL + '/register'
    register_result = " "
    register_text = 'Fail to get response'
    if n_clicks:
        #register testing
        payload = {
        "device_id":DEVICEID,
        "category": category
        }
        #Passing payload as dict
        response_register= requests.post(URL_register, data = payload, timeout = 5)
        register_text = response_register.text
       # register_result = json.loads(register_text)
        global appkey
        appkey = None
        if register_text[3]:
            appkey = register_text[3]
    return register_text

#upload data 
@app.callback(
    Output("upload_output", "children"), 
    [Input("upload_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("dtype_selection", "value"),
    State("Input_device_id", "value"),
    State("Input_keyfield", "value"),
    State("Input_payload", "value")]
)
def send_upload_request(n_clicks,  URL, dtype, DEVICEID,  keyfield, payload):
    URL_upload = URL + '/uploaddata'
    upload_result = 'Fail to get response'
    if n_clicks:
        payload = {"data_type": dtype, 
                    "device_id": DEVICEID, 
                    "key": "", 
                    "required_field": "",
                    "device_data": payload   
                }
        #Passing payload as dict
        response_upload = requests.post(URL_upload, 
            json = payload, 
            timeout = 5, 
            headers = {"appkey" : appkey})
        upload_result = json.loads(response_upload.text)
        # upload_result_mesg = upload_result['message']
    return upload_result

#getownerdata
@app.callback(
    Output("getowner_output", "children"), 
    [Input("getowner_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("dtype_selection", "value"),
    State("Input_device_id", "value"),
    State("Input_owner", "value"),]
)
def send_getowner(n_clicks, URL, dtype, DEVICEID, OWNER):
    URL_getowner = URL + '/getownerdata'
    getowner_result = 'Fail to get response'
    if n_clicks:
        #query as request
        query = {"data_type": dtype, 
        "device_id": DEVICEID, 
        "owner": OWNER}
        response_get = requests.get(URL_getowner, params=query, timeout = 5, headers = {"appkey" : appkey})
        getowner_result = json.loads(response_get.text)
        # getowner_result_mesg = get_result['message']
    return getowner_result

#requestsharing
@app.callback(
    Output("requestsharing_output", "children"), 
    [Input("request_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("Input_request", "value")]
)
def send_requestsharing(n_clicks,  URL, requestload):
    URL_requestsharing = URL + '/requestsharing'
    requestsharing_result = 'Fail to get response'
    if n_clicks:
        #Passing payload as dict
        requestsharing_upload = requests.post(URL_requestsharing, 
            json = requestload, 
            timeout = 5, 
            headers = {"appkey" : appkey})
        requestsharing_result = json.loads(requestsharing_upload.text)
        # requestsharing_result_mesg = requestsharing_result['message']
    return requestsharing_result

#owner get request and approve
@app.callback(
    Output("getrequest_output", "children"), 
    [Input("getrequest_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("dtype_selection", "value"),
    State("Input_device_id", "value"),
    State("Input_owner_request", "value"),]
)
def get_request(n_clicks, URL, dtype, DEVICEID, OWNER_request):
    URL_getrequest = URL + '/getrequest'
    get_request_result = 'Fail to get respones'
    if n_clicks:
        #query as request
        query = {"data_type": dtype, 
        "device_id": DEVICEID, 
        "owner": OWNER_request}
        response_get = requests.get(URL_getrequest, params=query, timeout = 5, headers = {"appkey" : appkey})
        get_request_result = json.loads(response_get.text)
    return get_request_result

#owner approve
@app.callback(
    Output("approverequest_output", "children"), 
    [Input("approve_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("Input_approve", "value")]
)
def send_requestsharing(n_clicks,  URL, approveload):
    URL_approve = URL + '/approverequest_output'
    approve_result = 'Fail to get response'
    if n_clicks:
        #Passing payload as dict
        approve_upload = requests.post(URL_approve, 
            json = approveload, 
            timeout = 5, 
            headers = {"appkey" : appkey})
        approve_result = json.loads(approveload.text)
        # requestsharing_result_mesg = requestsharing_result['message']
    return approve_result

#getshareddata  
@app.callback(
    Output("getshareddata_output", "children"), 
    [Input("getshareddata_submit_button", "n_clicks")],
    [State("API_selection", "value"),
    State("dtype_selection", "value"),
    State("Input_device_id", "value"),
    State("Input_viewer", "value"),]
)
def send_getshareddata(n_clicks, URL, dtype, DEVICEID, viewer):
    URL_getshareddata = URL + '/getshareddata'
    getshareddata_result_mesg = None
    if n_clicks:
        #query as request
        query = {"data_type": dtype, 
        "device_id": DEVICEID, 
        "viewer": viewer}
        response_get = requests.get(URL_getshareddata, params=query, timeout = 5, headers = {"appkey" : appkey})
        get_result = json.loads(response_get.text)
        getshareddata_result_mesg = get_result['message']
    return getshareddata_result_mesg

if __name__ == '__main__':
    app.run_server(port=10087)

#ce3bc125f87bde6c57f785dce254d6d820d2636f4a8aa0f404a7f76bd55c11c8