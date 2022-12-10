# %%
# imports plotly: pyo, go; pandas; xlwings; numpy;
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import xlwings as xw

# %%
# Read in data to data frame using pandas
df = pd.read_csv("./data/mpg.csv")
df.shape # show the col/rows of the df
df.info()

# %%
# view the dataframe
pd.options.display.min_rows=15
# |df,xw.view(df),df.head(),df.to_markdown()|
df.head()

# %%
# create data variable using list/dict comprehension
data = [go.Histogram(x=df["mpg"], xbins=dict(start=0, end=50, size=2))]

# %% Create layout
layout = go.Layout(title="Histogram")

# %%
# Create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Load plot to html
pyo.plot(fig, filename="histogram.html")
