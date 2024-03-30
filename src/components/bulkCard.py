# -*- coding: utf-8 -*-
"""
Created on Sun May  7 08:39:35 2023
Input card for sliders associated with bulk parameters which carry uncertainty
@author: jim
"""

# dash imports
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
#from dash.dependencies import Input, Output



# project imports
from . import ids

n_range = {'min':0.05054,'default':0.08854,'max':0.12654}
tau_p_range = {'min':0.054,'default':0.12,'max':0.186}
tau_s_range = {'min':1.77,'default':1.77,'max':100.}
gamma_po_range = {'min':193.6e6,'default':354.53e6,'max':515.45e6}
gamma_so_range = {'min':27.962e6,'default':44.677e6,'max':61.436e6}

dcc.Slider(0, 20, marks=None, value=10)

EXP_SLIDER = 'n-slider'
TAUP_SLIDER = 'taup-slider'
TAUS_SLIDER = 'taus-slider'
GAMMAP_SLIDER = 'gammapo-slider'
GAMMAS_SLIDER = 'gammaso-slider'

nSlider = dcc.Slider(n_range['min'],
                     n_range['max'],
                     marks=None, 
                     value=n_range['default'],
                    # tooltip={"placement": "bottom", "always_visible": True},
                     id=ids.EXP_SLIDER)

taupSlider = dcc.Slider(tau_p_range['min'],
                        tau_p_range['max'],
                        marks=None, value=tau_p_range['default'],
                        tooltip={"placement": "bottom", "always_visible": True},
                        id=ids.TAUP_SLIDER)

tausSlider = dcc.Slider(tau_s_range['min'],
                        tau_s_range['max'],
                        marks=None, 
                        value=tau_s_range['default'],
                        tooltip={"placement": "bottom", "always_visible": True},
                        id=ids.TAUS_SLIDER)

gammapSlider = dcc.Slider(gamma_po_range['min'],
                          gamma_po_range['max'],
                          marks=None,
                          value=gamma_po_range['default'],
                          tooltip={"placement": "bottom", "always_visible": True},
                          id=ids.GAMMAP_SLIDER)

gammasSlider = dcc.Slider(gamma_so_range['min'],
                          gamma_so_range['max'],
                          marks=None,
                          value=gamma_so_range['default'],
                          tooltip={"placement": "bottom", "always_visible": True},
                          id=ids.GAMMAS_SLIDER)

nGroup = html.Div(
            [
                html.Div('n',className='input-group-label'),
                nSlider,
            ],
#            className="mb-3",
        )

taupGroup = html.Div(
            [
                html.Div('tau_p (ms)',className='input-group-label'),
                html.Div(taupSlider),
            ],
#            className="mb-3",
        )

tausGroup = html.Div(
            [
                html.Div('tau_s (ms)',className='input-group-label'),
                tausSlider,
            ],
#            className="mb-3",
        )

gammapGroup = html.Div(
            [
                html.Div('gamma_p',className='input-group-label'),
                gammapSlider,
            ],
#            className="mb-3",
        )

gammasGroup = html.Div(
            [
                html.Div('gamma_s',className='input-group-label'),
                gammasSlider,
            ],
#            className="mb-3",
        )


# coniguration card to open canvas and display current configuration
card = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Bulk Constants", className="card-title"),
                nGroup,
                tausGroup,
                taupGroup,
                gammapGroup,
                gammasGroup
                
                ,
        
            ]
        ),
    ],
    style={"width": "100%"},
)




def render(app: Dash) -> html.Div:
 
    @app.callback(
        Output(ids.CALC_BUTTON,'n_clicks',allow_duplicate=True),
        Input(ids.EXP_SLIDER,'value'),
        State(ids.CALC_BUTTON,'n_clicks'),
        prevent_initial_call=True
        )
    
    def ncallback(val,n):
        return n+1
    
    @app.callback(
        Output(ids.CALC_BUTTON,'n_clicks',allow_duplicate=True),
        Input(ids.TAUS_SLIDER,'value'),
        State(ids.CALC_BUTTON,'n_clicks'),
        prevent_initial_call=True
        )
    def tauscallback(val,n):
        return n+1
    
    @app.callback(
        Output(ids.CALC_BUTTON,'n_clicks',allow_duplicate=True),
        Input(ids.TAUP_SLIDER,'value'),
        State(ids.CALC_BUTTON,'n_clicks'),
        prevent_initial_call=True
        )
    def taupcallback(val,n):
        return n+1
    
    @app.callback(
        Output(ids.CALC_BUTTON,'n_clicks',allow_duplicate=True),
        Input(ids.GAMMAP_SLIDER,'value'),
        State(ids.CALC_BUTTON,'n_clicks'),
        prevent_initial_call=True
        )
    def gpcallback(val,n):
        return n+1
    
    @app.callback(
        Output(ids.CALC_BUTTON,'n_clicks',allow_duplicate=True),
        Input(ids.GAMMAS_SLIDER,'value'),
        State(ids.CALC_BUTTON,'n_clicks'),
        prevent_initial_call=True
        )
    def gscallback(val,n):
        return n+1


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