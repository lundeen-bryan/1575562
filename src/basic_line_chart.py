# %%
# import numpy, plotly, graph offline and object
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

# %%
# random seed 56
np.random.seed(56)

# %%
# Set x and y values
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

# %%
# linecharts on a figure is called a trace, create trace
trace0 = go.Scatter(x=x_values, y=y_values+5, mode="markers", name="markers")
trace1 = go.Scatter(x=x_values, y=y_values, mode="lines", name="lines")
trace2 = go.Scatter(x=x_values, y=y_values-5, mode="lines+markers", name="lines and markers")
# %%
# Pass trace to data list
data = [trace0, trace1, trace2]

# %%
# create layout
layout = go.Layout(title="Line Charts")

# %%
# create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Create basic line chart object in html
pyo.plot(fig, filename="basic_line_chart.html")