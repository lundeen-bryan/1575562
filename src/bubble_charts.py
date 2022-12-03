# %%
# import packs
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
import xlwings as xw

# %%
# Create data frame from pandas mpg csv
df = pd.read_csv("././data/mpg.csv")

# %%
# replace missing horsepower using xlwings
xw.view(df)

# %% [markdown]
#### Replace Missing Horsepower Values in DataFrame
# While Excel is open filter blank cells in the
# horsepower column and replace with the following
# ```
#| name                 | horsepower |
#|----------------------|------------|
#| ford pinto           | 100        |
#| ford maverick        | 91         |
#| renault lecar deluxe | 53         |
#| ford mustang cobra   | 119        |
#| renault 18i          | 81         |
#| amc concord dl       | 82         |
# ```
# Then unfliter the Excel workbook and select A1

# %%
# Return Excel table back to DataFrame
wb = xw.books.active
sheet1 = wb.sheets[0]
# new_data = sheet1.range("A1").expand("table").value
df = xw.load(index=1, header=1)

# %%
# View the DataFrame to ensure that it doesn't
# have blank values
xw.view(df)

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