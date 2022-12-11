## Import packages dash: html, dcc
import dash

# import dash_core_components as dcc ## deprecated
from dash import dcc

# import dash_html_components as html ## depreceted
from dash import html

## initialize the dash app
app = dash.Dash()
## create the dash app layout
app.layout = html.Div(
    children=[
        html.H1("Hello Dash"),
        html.Div("Dash: Web Dashboards with Python"),
        dcc.Graph(
            id="example",
            figure={
                "data": [
                    {
                        "x": [1, 2, 3],
                        "y": [4, 1, 2],
                        "type": "bar",
                        "name": "SF",
                    },
                    {
                        "x": [1, 2, 3],
                        "y": [4, 1, 2],
                        "type": "bar",
                        "name": "NYC",
                    },
                ],
                "layout": {
                    "title": "BAR PLOTS!",
                },
            },
        ),
    ]
)
## create the main function
if __name__ == '__main__':
    app.run_server(debug=True)
