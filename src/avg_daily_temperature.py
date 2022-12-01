# %%
# import pandas, plotly, graph offline and object
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go
import xlwings as xw

# %%
# Read the 2010YumaAZ.csv file to data frame day as index
df = pd.read_csv("./data/2010YumaAZ.csv")
# df.set_index("DAY", inplace=True)
df.drop(["LST_DATE"], axis=1, inplace=True)
df
#xw.view(df)

# %%
# create data list using list comprehension
'''
 *
 * For each day in Day column
 * get the time matching the Day index
 * get the temp matching the Day index
 *
'''
# data = {dict(x=df["LST_TIME"], y=df[df["DAY"]==day]["T_HR_AVG"], name=day) for day in df["DAY"].unique()}
data = [
    {
        "x": df["LST_TIME"],
        "y": df[df["DAY"]==day]["T_HR_AVG"],
        "name":day
    } for day in df["DAY"].unique()
]
type(data)

# %%
# create layout
layout = go.Layout(title="Avg Daily Temperature")

# %%
# Create figure
fig = go.Figure(data=data, layout=layout)

# %%
# Load plot to html
pyo.plot(fig, filename="avg_temp_plot.html")