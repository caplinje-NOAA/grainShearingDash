from dash import Dash, html
import dash_bootstrap_components as dbc
#from . import card_dropdown
from . import waterCard, sedimentCard, bulkCard, calcButton, plots



def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
  
            html.Div([dbc.Row([   ## inputs row
                            # Left hand side
                            dbc.Col([
                                html.Div(waterCard.render(app),className="app-div"),
                                html.H4('Based on the Viscus Grain-Shearing model.'),
                                html.Div('Buckingham 2007,2010,2020')
                                ]),
                            dbc.Col([
                                html.Div(sedimentCard.render(app),className="app-div"),
                                calcButton.render(app),
                                ]),
                            dbc.Col([
                                html.Div(bulkCard.render(app),className="app-div"),
                                ]),
                            ]),
                               
            
                    ]
                ),
            html.Hr(),
            
            html.Div([dbc.Row([   ## inputs row
                            # Left hand side
                            dbc.Col([
                                    plots.cpFigure,
                                    plots.alphapFigure
                                ]),
                            dbc.Col([
                                    plots.csFigure,
                                    plots.alphasFigure           
                                ]),
                            ])

                               
            
                    ]
                ),
            ]
        )
