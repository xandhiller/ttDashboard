# Get into correct working directory for custom module imports
import pandas as pd
import logging
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from htmlElements import (
    nosy_ankao_title,
    nosy_ankao_bn,
    lower_zambezi_title,
    lower_zambezi_bn,
    liuwa_title,
    liuwa_bn,
    south_luanga_title,
    south_luanga_bn
)


# Referential shortcut
app = dash.Dash()

# CONFIGURATIONS:
# For text formatting
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    html.H1('Time & Tide Dashboard'),
    html.Div([
        html.H4('Bednights (Confirmed and Prospective)'),

        dcc.Dropdown(id='dropdown', multi=True, options=[{'value': i, 'label': i} for i in ['Bednights Analysis', 'Currency Analysis']]),

        html.Div(
            id='output',
            children=''
            )
        ]
    )
])

@app.callback(Output('output', 'children'), [Input('dropdown', 'value')])
def display_focus(selected_values):
    focus = []
    for values in selected_values:
        if values == 'Bednights Analysis':
            # Figure out how to call the objects in the htmlElements file
            focus.append(lower_zambezi_title)
            focus.append(lower_zambezi_bn)
            focus.append(south_luanga_title)
            focus.append(south_luanga_bn)
            focus.append(liuwa_title)
            focus.append(liuwa_bn)
            focus.append(nosy_ankao_title)
            focus.append(nosy_ankao_bn)
        if values == 'Currency Analysis':
            focus.append(html.Div(
                html.H3(children='Currency Analysis')
            ))
    return focus




if __name__ == "__main__":
    app.run_server(debug=True)
