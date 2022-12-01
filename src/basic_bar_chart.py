# %%
# import plotly and pandas
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# %%
# read in 2018WinterOlympics.csv
df = pd.read_csv("./data/2018WinterOlympics.csv")
df

# %%
# Create traces
trace1 = go.Bar(x=df["NOC"], y=df["Gold"], marker={"color":"#d5d500"}, name="Gold")
trace2 = go.Bar(x=df["NOC"], y=df["Silver"], marker={"color":"#c0c0c0"}, name="Silver")
trace3 = go.Bar(x=df["NOC"], y=df["Bronze"], marker={"color":"#808000"}, name="Bronze")

# %%
# Create data list
data = [trace1, trace2, trace3]

# %%
# create layout
layout = go.Layout(title="Medals", barmode="stack")

# %%
# Create fig
fig = go.Figure(data, layout=layout)

# %%
# Load chart into html
pyo.plot(fig, filename="basic_bar_chart.html")