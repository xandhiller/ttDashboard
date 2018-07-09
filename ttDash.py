import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd



def generate_table(dataframe, max_rows = 10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # html.Tr: Is a row cell in an html table
        # html.Th: Is a header cell in html table

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))]
    )

app = dash.Dash()

# For text formatting
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server()
