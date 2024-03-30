# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:39:35 2023
The general options (top-left card) components and primary callback of the app
@author: jim
"""

# dash imports
from dash import Dash, html
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output



# project imports
from . import ids


# water inputs
WATER_DEPTH_INPUT = 'water-depth-input'
WATER_SS_INPUT = 'water-sound-speed'
TEMPERATURE = 'water-temperature'
SALINITY = '34.615341'


depthInput = dbc.InputGroup(
            [
                dbc.InputGroupText('water depth',className='input-group-label'),
                dbc.Input(type="number",id=ids.WATER_DEPTH_INPUT,value=0.1,min=0.0,max=20.0),
                dbc.InputGroupText('km'),
            ],
            className="mb-3",
        )

soundspeedInput = dbc.InputGroup(
            [
                dbc.InputGroupText('SS near seafloor',className='input-group-label'),
                dbc.Input(type="number",id=ids.WATER_SS_INPUT,value=1500.0, min=1000.0, max = 2000.0),
                dbc.InputGroupText('m/s'),
            ],
            className="mb-3",
        )

temperatureInput = dbc.InputGroup(
            [
                dbc.InputGroupText('Temperature',className='input-group-label'),
                dbc.Input(type="number",id=ids.TEMPERATURE,value=25.,max=35.,min=0.),
                dbc.InputGroupText('degrees c'),
            ],
            className="mb-3",
        )

salinityInput = dbc.InputGroup(
            [
                dbc.InputGroupText('Salinity',className='input-group-label'),
                dbc.Input(type="number",id=ids.SALINITY,value=34.615341,max=37.,min=31.),
                dbc.InputGroupText('PSU'),
            ],
            className="mb-3",
        )


        


# coniguration card to open canvas and display current configuration
card = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Water Inputs", className="card-title"),
                depthInput,
                soundspeedInput,
                temperatureInput,
                salinityInput,
                
                
        
            ]
        ),
    ],
    style={"width": "100%"},
)




def render(app: Dash) -> html.Div:
 



    return html.Div(
        [
            card
            
        ]
    )


## dictionary version of callback signature
# output = dict(
#             fig = Output(ids.TAB_SPINNER, 'children'),
#             outSecondaryChild = Output(ids.TAB_SPINNER_SECONDARY, "children",allow_duplicate=True),
#             mapLayer = Output(ids.MAP_LAYER, "children"),
#             alert = Output(ids.ALERT, "children")
#     )

# inputs = dict(n = Input(ids.GET_DATA_BUTTON, "n_clicks"))

# state = dict(
#         tab_value = State(ids.TABS, 'value'),
#         lat = State(ids.LAT_INPUT,'value'),
#         lon = State(ids.LON_INPUT,'value'),
#         minutes = State(ids.BB_MIN,'value'),
#         month = State(ids.SSP_MONTH_DROPDOWN,'value'),
#         bathsource = State(ids.BATH_SOURCE_DROPDOWN,'value'),
#         secondaryChild = State(ids.TAB_SPINNER_SECONDARY, "children")
#     )


## Old callback from tabs (used to be the fundamental callback)
    # @callback(
    # Output(ids.TAB_SPINNER, 'children'),
    # Output(ids.TAB_SPINNER_SECONDARY, "children",allow_duplicate=True),
    # Output(ids.MAP_LAYER, "children"),
    # Output(ids.ALERT, "children"),
    # [Input(ids.TABS, 'value'),
    # State(ids.MAP_FIG, "clickData"),
    # State(ids.BB_MIN,'value'),
    # State(ids.SSP_MONTH_DROPDOWN,'value'),
    # State(ids.BATH_SOURCE_DROPDOWN,'value'),
    # State(ids.TAB_SPINNER_SECONDARY, "children")],
    # prevent_initial_call=True
    # )
    # def update_tabs(value,clickData,minutes,month,bathsource,secondaryChild):
    #     """This is the primary callback.  When tab value is triggered, gather all inputs, retrieve appropriate data, 
    #     and update figures"""
    #     lat = clickData['latlng']['lat']
    #     lng = clickData['latlng']['lng']
    #     click_lat_lng = [lat,lng]
        
    #     # secondary child div contains transects for the bath tab
    #     # passing the child through this callback allows it to remain
    #     # 
    #     if value == 'bath-tab':
    #         outSecondaryChild = secondaryChild
    #     else:
    #         outSecondaryChild = []
            
    #     fig, mapLayer, alert = renderer[value].render(click_lat_lng,minutes,month,bathsource)


    #     return fig, outSecondaryChild, mapLayer, alert