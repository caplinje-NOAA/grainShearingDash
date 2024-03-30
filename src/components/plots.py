# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:53:59 2023
This module handles the rendering of SSP data
@author: jim
"""

# dash imports
from dash import dcc, html


# plotting imports
import plotly.express as px

from . import ids



cpFigure = html.Div(dcc.Graph(figure=px.line(),id=ids.CP_PLOT))

csFigure = html.Div(dcc.Graph(figure=px.line(),id=ids.CS_PLOT))

alphapFigure = html.Div(dcc.Graph(figure=px.line(),id=ids.ALPHAP_PLOT))

alphasFigure = html.Div(dcc.Graph(figure=px.line(),id=ids.ALPHAS_PLOT))




