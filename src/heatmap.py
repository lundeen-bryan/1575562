# %%
## imports plotly: pyo, go; pandas; xlwings; numpy;
# import plotly.offline as pyo
import plotly.graph_objects as go
import plotly.io as io  # use instead of pyo
import pandas as pd

# %%
## Read in data to data frame using pandas
df = pd.read_csv("./data/2010YumaAZ.csv")
df.shape  # show the col/rows of the df
# df.info()

# %%
## view the dataframe
pd.options.display.min_rows = 15
# |df,xw.view(df),df.head(),df.to_markdown()|
df.head(2)

# %%
## create data variable using list/dict comprehension
data = [
    go.Heatmap(
        x=df["DAY"],
        y=df["LST_TIME"],
        z=df["T_HR_AVG"].values.tolist(),
        colorscale="Inferno",
        colorbar=dict(
            title="Celsius",
            titleside="top",
            ticktext=["Cool", "Mild", "Hot"],
        ),
    )
]

# %% Create layout
layout = go.Layout(title="Santa Barbara Temperature")

# %%
## Create figure
fig = go.Figure(data=data, layout=layout)

# %%
## place the title in the center of the chart
fig.update_layout(
    dict(
        title_xanchor="auto",
        title_x=0.5,
    )
)

# %%
## show the figure
fig.show()

# %%
## Load plot to html
# pyo.plot(fig, filename="heatmap.html")
io.write_html(fig=fig, file="heatmap.html", auto_open=True)
