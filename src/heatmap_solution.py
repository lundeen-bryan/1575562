#######
# Objective: Using the "flights" dataset available
# from the data folder as flights.csv
# create a heatmap with the following parameters:
# x-axis="year"
# y-axis="month"
# z-axis(color)="passengers"
######

# %%
## imports plotly: pyo, go; pandas; xlwings; numpy;
import plotly.graph_objects as go
import plotly.io as io  # use instead of pyo
from plotly.subplots import make_subplots
import pandas as pd

# %%
## Read in data to data frame using pandas
df = pd.read_csv("./data/flights.csv")
df.shape  # show the col/rows of the df

# %%
## view the dataframe
pd.options.display.min_rows = 15
# |df,xw.view(df),df.head(),df.to_markdown()|
df.head()

# %%
## create data variable using list/dict comprehension (turbo = best for temperature)
data = [
    go.Heatmap(
        x=df["year"],
        y=df["month"],
        z=df["passengers"],
        colorscale="turbo",
    )
]

# %%
## Create figure
fig = go.Figure(data=data)

# %% Create layout
fig.update_layout(
    dict(
        title_text="Passengers Per Flight",
        plot_bgcolor="#b2b2b2",
        title_xanchor="auto",
        title_x=0.5,
        title_font_size=20,
    )
)

# %%
## Load plot to html
io.write_html(fig=fig, file="heatmap_multi.html", auto_open=True)

#######
# Excellent! This shows two distinct trends - an increase in
# passengers flying over the years, and a greater number of
# passengers flying in the summer months.
######
