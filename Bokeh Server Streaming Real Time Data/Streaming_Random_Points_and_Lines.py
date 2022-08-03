# import libraries
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from random import randrange

"""
This sections focuses on how to stream data with bokeh or plot realtime data
"""

# create figure
f = figure(x_range=(0, 11), y_range=(0, 11))

# create columndatasource
source = ColumnDataSource(data=dict(x=[], y=[]))

# create glyphs
f.circle(x="x", y="y", size=8, fill_color="olive", line_color="brown", source=source)
f.line(x="x", y="y", source=source)


# create periodic function
def update():
    new_data = dict(x=[randrange(1, 10)], y=[randrange(1, 10)])
    # # rollover defines how many glyphs you want to keep in the plot
    # # stream method on a columndatasource is synonymous to an append method on a List
    source.stream(new_data, rollover=15)
    print(source.data)


# add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)  # 1000 milliseconds = 1 second
