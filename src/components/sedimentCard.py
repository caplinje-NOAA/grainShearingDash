# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:39:35 2023
The general options (top-left card) components and primary callback of the app
@author: jim
"""

# dash imports
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output



# project imports
from . import ids





N_Input = dbc.InputGroup(
            [
                dbc.InputGroupText('Porosity',className='input-group-label'),
                dbc.Input(type="number",id=ids.N_INPUT,value=0.377, min=0.371, max=.95),
                dbc.InputGroupText('frac.'),
            ],
            className="mb-3",
        )

u_Input = dbc.InputGroup(
            [
                dbc.InputGroupText('Grain Size',className='input-group-label'),
                dbc.Input(type="number",id=ids.U_INPUT,value=400.0, min = 1., max = 2000.),
                dbc.InputGroupText('um'),
            ],
            className="mb-3",
        )

depthInput = dbc.InputGroup(
            [
                dbc.InputGroupText('Depth in sediment',className='input-group-label'),
                dbc.Input(type="number",id=ids.DEPTH_INPUT,value=0.3,min=0.000000001),
                dbc.InputGroupText('m'),
            ],
            className="mb-3",
        )

characteristicDropdown = html.Div(
    dcc.Dropdown(['Sand', 'Mud'], 'Sand', id=ids.CHARACTERISTIC_DROPDOWN, searchable=False,clearable=False)
        
)

# coniguration card to open canvas and display current configuration
card = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Sediment Inputs", className="card-title"),
                N_Input,
                u_Input,
                depthInput,
                characteristicDropdown
                
                ,
        
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