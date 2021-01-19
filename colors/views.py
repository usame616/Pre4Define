from django.http import HttpResponse
from django.shortcuts import render
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import plotly



def ColorPlot(request):

df = pd.read_csv("ssta/color.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i}
                 for i in df.columns],
        data=df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender"),
        filter_action = 'native'
    )

])
app.run_server(debug=True)
return HttpResponse()

