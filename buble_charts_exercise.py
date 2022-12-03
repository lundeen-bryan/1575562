# %%
# import packs
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import xlwings as xw

# %%
# Create data frame from pandas mpg csv
df = pd.read_csv("./data/mpg.csv")
pd.set_option("display.max_rows", None)
df # view entire dataframe to ensure the values contain "?"

# %% [markdown]
#### Replace Missing Horsepower Values in DataFrame
# Use iloc to replace the values below in the dataframe
# ```
# | loc | horsepower | name                 |
# |-----|------------|----------------------|
# | 32  | 100        | ford pinto           |
# | 126 | 91         | ford maverick        |
# | 330 | 53         | renault lecar deluxe |
# | 336 | 119        | ford mustang cobra   |
# | 354 | 81         | renault 18i          |
# | 374 | 82         | amc concord dl       |
# ```

# %%
# using at function, change values from comment above
df.at[32, "horsepower"]=100 # ford pinto
df.at[126, "horsepower"]=91 # ford maverick
df.at[330, "horsepower"]=53 # renault lecar deluxe
df.at[336, "horsepower"]=119 # ford mustang cobra
df.at[354, "horsepower"]=81 # renalut 18i
df.at[374, "horsepower"]=82 # amc concord dl

# %%
df # again view frame to determine if the values were changed

# %%
# create data
data = [
    go.Scatter(
        x=df["horsepower"],
        y=df["mpg"],
        text=df["name"],
        mode="markers",
        marker=dict(size=2*df["cylinders"])
    )
]
# %%
# create layout
layout = go.Layout(
    title="Bubble Chart"
)

# %%
# create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Create plot in html
pyo.plot(fig, filename="bubble_chart.html")
