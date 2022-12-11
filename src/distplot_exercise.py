# %% [markdown]
# ## Objective: Distplot for Iris Dataset
#
# Using the iris dataset, develop a Distplot that compares the petal lengths of each class.
#
# File: '../data/iris.csv'
#
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
#
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'

# %%
## imports plotly: pyo, go; pandas; xlwings; numpy;
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd
import plotly.io as io

# %%
## Read in data to data frame using pandas
df = pd.read_csv("../data/iris.csv")
df.shape  # show the col/rows of the df

# %%
## view the dataframe
pd.options.display.min_rows = 10
# |df,xw.view(df),df.head(),df.to_markdown()|
df.head()

# %%
## create lists for holding petal len
# Fields: sepal_length,sepal_width,petal_length,petal_width,class
# Classes: Iris-setosa,Iris-versicolor,Iris-virginica
fields = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class",
]
classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

# %%
## Create dataframe string for each class using list comprehension
traces = ['df[df["class"]=="' + x + '"]["petal_length"]' for x in classes]

# %%
## traces 0, 1, 2 just ctrl+enter 3 times
trace0 = traces[0]
print("trace0 = " + trace0)
trace1 = traces[1]
print("trace1 = " + trace1)
trace2 = traces[2]
print("trace2 = " + trace2)

# %%
## Define the traces
# This grabs the petal_length column for a particular flower
trace0 = df[df["class"] == "Iris-setosa"]["petal_length"]
trace1 = df[df["class"] == "Iris-versicolor"]["petal_length"]
trace2 = df[df["class"] == "Iris-virginica"]["petal_length"]

# %%
## create data variable for traces and labels
data = [trace0, trace1, trace2]
group_labels = ["Setosa", "Versicolor", "Virginica"]

# %%
## Create figure
fig = ff.create_distplot(
    hist_data=data, group_labels=group_labels, show_rug=False
)


# %% Create layout
fig.update_layout(
    dict(
        title_text="Distribution of Petal Length",
        legend_title=dict(text="class", font_color="#000000"),
        plot_bgcolor="#d7d7d7",
        title_xanchor="auto",
        title_x=0.45,
    )
)
fig.update_xaxes(dict(title_text="Petal Length", title_font_color="#000000"))
fig.update_yaxes(dict(title_text="Density", title_font_color="#000000"))

# %%
## Load plot to html
# pyo.plot(fig, filename="distplot.html") ## deprecated
io.write_html(fig=fig, file="distplot_io.html", auto_open=True)
