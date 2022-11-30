# %%
# import pandas, plotly, graph offline and object
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objects as go
import xlwings as xw

# %%
# read in nst-est2017-alldata.csv with pandas as data frame
df = pd.read_csv("./data/nst-est2017-alldata.csv")
df.head()

# %%
# Load df into excel for better view
xw.view(df)

# %%
# Create new dataframe that holds north east division states
## ! Note that DIVISION filter must be a string to work
df2 = df[df["DIVISION"] == "1"]
# Use the name column as the new index
df2.set_index("NAME", inplace=True)
# Use list comprehension to create a list of columns that start with "POP"
population_column_names = [col for col in df2.columns if col.startswith("POP")]
# create a new data frame showing state names and pop columns
df2 = df2[population_column_names]
df2

# %%
# Create traces
'''
 *
 * Using List Comprehension:
 * for each state in the name column
 * get the x value from the population column
 * get the y value by matching the state[name] with the population column
 *
'''
data = [
    go.Scatter(x=df2.columns, y=df2.loc[name], mode="lines", name=name)
    for name in df2.index
]

# %%
# plot data in html file
pyo.plot(data, filename="line_with_data.html")