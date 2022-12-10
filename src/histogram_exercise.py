'''
 *
 * Objective: Create histogram that  plots the
 * "length" field from the Abalone dataset.
 * Set the range from 0 to 1, with a bin size
 * of 0.02
 *
'''

# %%
# imports plotly: pyo, go; pandas; xlwings; numpy;
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# %%
# Read in data to data frame using pandas
df = pd.read_csv("./data/abalone.csv")
df.shape # show the col/rows of the df
# df.info()

# %%
# view the dataframe
pd.options.display.min_rows=10
# |df,xw.view(df),df.head(),df.to_markdown()|
df.head()

# %%
# create data variable using list/dict comprehension
data = [go.Histogram(x=df["length"], xbins=dict(start=0, end=1, size=0.02))]

# %% Create layout
layout = go.Layout(title="Histogram Abalone")

# %%
# Create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Load plot to html
pyo.plot(fig, filename="histogram_exercise_solution.html")
