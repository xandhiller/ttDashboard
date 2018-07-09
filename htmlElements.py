import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from cleanData import cleanData


# GLOBALS:
# TODO: Can this be done from the net? This is obviously a local path
path_to_spreadsheet = '/Users/alexanderhiller/Downloads/Bednight_Report_2018_180702.xlsx'

bednight_graphs = []
df_lz, df_na, df_liu, df_sl = cleanData(path_to_spreadsheet)

# Bednight graphs and titles
nosy_ankao_title = html.Div(html.H4(children='Nosy Ankao'))
nosy_ankao_bn = html.Div(
    dcc.Graph(
        id='Nosy Ankao',
        figure={
            'data': [
                go.Scatter(
                    x=df_na.index,
                    y=df_na[i],
                    text='Nosy Ankao',
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df_na.keys()
            ],
            'layout': go.Layout(
                xaxis={'type': 'series', 'title': 'Date'},
                yaxis={'title': 'Beds', },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                # hovermode='closest',
                height = 400,
                width = 500
            )
        }
    )
)
south_luanga_title = html.Div(html.H4(children='South Luanga'))
south_luanga_bn = html.Div(
    dcc.Graph(
        id='South Luanga',
        figure={
            'data': [
                go.Scatter(
                    x=df_sl.index,
                    y=df_sl[i],
                    text='South Luanga',
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df_sl.keys()
            ],
            'layout': go.Layout(
                xaxis={'type': 'series', 'title': 'Date'},
                yaxis={'title': 'Beds', },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                # hovermode='closest',
                height = 400,
                width = 500
            )
        }
    )
)
liuwa_title = html.Div(html.H4(children='Liuwa'))
liuwa_bn = html.Div(
    dcc.Graph(
        id='Liuwa',
        figure={
            'data': [
                go.Scatter(
                    x=df_liu.index,
                    y=df_liu[i],
                    text='Liuwa',
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df_liu.keys()
            ],
            'layout': go.Layout(
                xaxis={'type': 'series', 'title': 'Date'},
                yaxis={'title': 'Beds', },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                # hovermode='closest',
                height = 400,
                width = 500
            )
        }
    )
)
lower_zambezi_title = html.Div(html.H4(children='Lower Zambezi'))
lower_zambezi_bn = html.Div(
    dcc.Graph(
        id='Lower Zambezi',
        figure={
            'data': [
                go.Scatter(
                    x=df_lz.index,
                    y=df_lz[i],
                    text='Lower Zambezi',
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=str(i)
                ) for i in df_lz.keys()
            ],
            'layout': go.Layout(
                xaxis={'type': 'series', 'title': 'Date'},
                yaxis={'title': 'Beds', },
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                # hovermode='closest',
                height = 400,
                width = 500
            )
        }
    )
)

# Currency graphs
