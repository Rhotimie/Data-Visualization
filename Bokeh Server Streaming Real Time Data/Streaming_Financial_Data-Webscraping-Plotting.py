from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure
from random import randrange

# request is used to load the content of a web page as a string in python
import requests

# bs4 is a library that understands HTML and is a able to parse the code
from bs4 import BeautifulSoup

"""
webscraping function is the name of the process/process that consist of extracting data from web pages

"""

# create figure
f = figure()


# create webscraping function
def extract_value():
    r = requests.get(
        "http://bitcoincharts.com/markets/btcnCNY.html",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net


# create ColumnDataSource
source = ColumnDataSource(dict(x=[1], y=[extract_value()]))

# create glyphs
f.circle(x="x", y="y", color="olive", line_color="brown", source=source)
f.line(x="x", y="y", source=source)


# create periodic function
def update():
    new_data = dict(x=[source.data["x"][-1] + 1], y=[extract_value()])
    source.stream(new_data, rollover=200)
    print(source.data)


# add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update, 2000)
