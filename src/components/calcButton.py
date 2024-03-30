# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:39:35 2023
The general options (top-left card) components and primary callback of the app
@author: jim
"""

# dash imports
from dash import Dash, html, Input, Output, State
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output

# data science imports
import pandas as pd

# plotting imports
import plotly.express as px

# project imports
from . import ids
from ..dataHandling.VGS_script_sand import VGSdf





button = html.Div(
    [   dbc.Row(
        [     
            dbc.Col(dbc.Button("Calculate", id=ids.CALC_BUTTON, className="button", n_clicks=0)),
            
            
        ]
      )
    ]
        
)

# coniguration card to open canvas and display current configuration
card = dbc.Card(
    [

        dbc.CardBody(
            [
                
                button
                
                ,
        
            ]
        ),
    ],
    style={"width": "100%"},
)

def logLine(df:pd.DataFrame,y:str)->px.line:   
    """plots compressional sound speed"""

    fig = px.line(df,x='f',y=y, log_x=True)
      

      

    
    return fig




def render(app: Dash) -> html.Div:
 
    @app.callback(
        output = [Output(ids.CP_PLOT, "figure"),
                  Output(ids.CS_PLOT, "figure"),
                  Output(ids.ALPHAP_PLOT, "figure"),
                  Output(ids.ALPHAS_PLOT, "figure"),
                  
                  ],
       
        
        inputs = dict(nclicks=Input(ids.CALC_BUTTON, "n_clicks")),
        
        state = dict(parameters=
                      dict(d = State(ids.DEPTH_INPUT, "value"),
                          N = State(ids.N_INPUT, "value"),
                          T = State(ids.TEMPERATURE,"value"),
                          S = State(ids.SALINITY,"value"),
                          dw = State(ids.WATER_DEPTH_INPUT,"value"),
                          cw = State(ids.WATER_SS_INPUT,"value"),
                          n = State(ids.EXP_SLIDER,"value"),
                          taup = State(ids.TAUP_SLIDER,"value"),
                          taus = State(ids.TAUS_SLIDER,"value"),
                          gammap = State(ids.GAMMAP_SLIDER,"value"),
                          gammas = State(ids.GAMMAS_SLIDER,"value"),
                          )
                      )
        
      
        )
    def main_callback(nclicks,parameters):
        if nclicks:
            df = VGSdf(parameters)
            cpfig = logLine(df,'cp')
            csfig = logLine(df,'cs')
            alphapfig = logLine(df,'alpha_p')
            alphasfig = logLine(df,'alpha_s')
            
            return [cpfig, csfig, alphapfig, alphasfig]
    return card
            


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