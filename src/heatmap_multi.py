# %%
## imports plotly: go, ff, io, subplots; pandas
import plotly.graph_objects as go
import plotly.io as io  # use instead of pyo
from plotly.subplots import make_subplots
import pandas as pd

# %%
## make list of cities used in titles
cities = ["Sitka, Alaska", "Santa Barbara, CA", "Yuma, Arizona"]

# %%
## Read in data from each city to a dataframe
df1 = pd.read_csv("../data/2010sitkaAK.csv")
df2 = pd.read_csv("../data/2010SantaBarbaraCA.csv")
df3 = pd.read_csv("../data/2010YumaAZ.csv")

# %%
## func to convert celsius to fahrenheit
def cel_to_fahr(cel):
    fahr = (cel * 1.8) + 32
    return fahr


# %%
## convert dataframe celsius temperature to fahrenheit
df1["Fahrenheit"] = cel_to_fahr(df1["T_HR_AVG"])
df2["Fahrenheit"] = cel_to_fahr(df2["T_HR_AVG"])
df3["Fahrenheit"] = cel_to_fahr(df3["T_HR_AVG"])


# %%
## combine all dataframes to 1 for reference min/max
combine = [df1, df2, df3]
frames = pd.concat(combine)  # combined dataframes
print(f"DataFrame Shape: {frames.shape}")  # show the col/rows of the df
print(frames.head())

# %%
## print min max values
zmin = int(pd.to_numeric(arg=frames["Fahrenheit"].min(), downcast="integer"))
zmax = int(pd.to_numeric(arg=frames["Fahrenheit"].max(), downcast="integer"))
print(f"zmin = {zmin}\nzmax = {zmax}")

# %%
## create traces for 3 cities as trace1, trace2, trace3
trace1 = [
    go.Heatmap(
        x=df1["DAY"],
        y=df1["LST_TIME"],
        z=df1["Fahrenheit"].values.tolist(),
        colorscale="Turbo",
        zmin=zmin,
        zmax=zmax,
        name=cities[0],
    )
]
trace2 = [
    go.Heatmap(
        x=df2["DAY"],
        y=df2["LST_TIME"],
        z=df2["Fahrenheit"].values.tolist(),
        colorscale="Turbo",
        zmin=zmin,
        zmax=zmax,
        name=cities[1],
    )
]
trace3 = [
    go.Heatmap(
        x=df3["DAY"],
        y=df3["LST_TIME"],
        z=df3["Fahrenheit"].values.tolist(),
        colorscale="Turbo",
        zmin=zmin,
        zmax=zmax,
        name=cities[2],
    )
]

# %%
## Create figure
"""
 * "make_subplots" is deprecated so instead use subplots.make_subplots
"""
fig = make_subplots(
    rows=1,
    cols=3,
    subplot_titles=cities,
    shared_yaxes=True,
)

# %%
## append traces to show graphs for ea city
# fig.append_trace ## deprecated, replace w/add_traces
fig.add_traces(data=trace1, rows=1, cols=1)
fig.add_traces(data=trace2, rows=1, cols=2)
fig.add_traces(data=trace3, rows=1, cols=3)

# %%
# create layout (update "layout_title_text" etc.)
fig.update_layout(
    dict(
        title_text="Avg Temperatures Across The USA",
        plot_bgcolor="#b2b2b2",
        title_xanchor="auto",
        title_x=0.5,
        title_font_size=20,
    )
)

# %%
## Load plot to html
io.write_html(fig=fig, file="heatmap_multi.html", auto_open=True)
