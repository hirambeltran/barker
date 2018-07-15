import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table_experiments as dt

import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.plotly as py
import flask
import os

import pandas as pd
import scipy
import numpy as np
from textwrap import dedent as s

app = dash.Dash(__name__)
server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')

app.title='Mean mortality rates across copies: Barker vs. Background'

# get data
shift_pred = pd.read_csv('data/summary_results_at_age40.csv')

# menus
#proportion_Barker = shift_pred.prop.unique()
#label_proportion_Barker = [w.replace('_', ' ') for w in proportion_Barker]
#dict_proportion_Barker = dict(zip(prop, label_proportion_Barker))

excess_Barker = shift_pred.R.unique()
label_excess_Barker = [w.replace('_', ' ') for w in excess_Barker]
dict_excess_Barker = dict(zip(R, label_excess_Barker))



# colors
dict_colors_shift = dict(zip(['1.5', '2', '2.5', '3', '3.5', '4'],
                       ['#e34a33', '#2b8cbe', '#31a354', '#fdae6b', '#e34a33', '#2b8cbe']))

dict_colors_back = dict(zip(['Background'],
                       ['#31a354']))

all_options = dict()

for c in excess_Barker:
    l = shift_pred.loc[(shift_pred.R==c), 'cohort'].unique().tolist()
    s = shift_pred.loc[(shift_pred.nmx.backg), 'cohort'].unique().tolist()
    td = {c : {'year':l, 'segment':l}}
all_options.update(td)
