# %%
# import packages
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# %%
# read in mocksurvey.csv
df = pd.read_csv("./../data/mocksurvey.csv", index_col=0)
df
# %%
# create traces
"""
 *
 * Colors are:
 * Strongly Disagree = BlueViolet, Somewhat Disagree = Red
 * Neutral = Green, Somewhat Agree = Orange, Strongly Agree = Blue
 *
"""

# %%
# Create data list
data = [
    go.Bar(
        y=df.index,
        x=df[response],
        name=response,
        orientation="h",
    )
    for response in df.columns
]

# %%
# create layout
colors = [
    "Neon Blue" "Scarlet",
    "LimeGreen",
    "BlueViolet",
    "DarkOrange",
].reverse()
layout = go.Layout(
    title="Survey Results",
    barmode="stack",
    colorway=colors,
    plot_bgcolor="WhiteSmoke",
)

# %%
# create fig
fig = go.Figure(data=data, layout=layout)

# %%
# load chart into html
pyo.plot(fig, filename="bar_chart_exercise.html")
