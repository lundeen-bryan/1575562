# %%
# imports plotly: pyo, go; pandas; xlwings; numpy;
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import xlwings as xw

# %%
# Read in data to data frame using pandas
df = pd.read_csv("./data/abalone.csv")
df.shape # show the col/rows of the df
df.info

# %%
# view the dataframe
pd.options.display.min_rows=35
# |df,xw.view(df),df.head(),df.to_markdown()|
xw.view(df)

# %%
# take 2 random samples of diff sizes
a = np.random.choice(df["rings"], 30, replace=False)
b = np.random.choice(df["rings"], 20, replace=False)

# %%
# create data variable
data = [go.Box(y=a, name="A"), go.Box(y=b, name="B")]

# %% Create layout
layout = go.Layout(title="Two Random Samples")

# %%
# Create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Load plot to html
pyo.plot(fig, filename="box_exercise_solution.html")
