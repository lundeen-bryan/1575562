# %%
# imports pandas, plotly, graph offline and object
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go

# %%
# load y value with a list
snodgrass = [
    0.209,
    0.205,
    0.195,
    0.210,
    0.202,
    0.207,
    0.224,
    0.223,
    0.220,
    0.201,
]
twain = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]
# %%
# create data variable using list/dict comprehension
data1 = [go.Box(y=snodgrass, name="Snodgrass"), go.Box(y=twain, name="Twain")]


# %% Create layout
# layout = go.Layout(title="title")

# %%
# Create figure
# fig = go.Figure(data=data, layout=layout)

# %%
# Load plot to html
pyo.plot(data1, filename="box_plot.html")
