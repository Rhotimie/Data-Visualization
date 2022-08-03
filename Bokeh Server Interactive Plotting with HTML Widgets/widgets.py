# Importing libraries
from bokeh.plotting import figure

# from bokeh.io import output_file, show
from bokeh.io import curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout


"""
Bokeh Server Interactive Plotting with HTML Widgets

Bokeh server is like a components builts in bokeh used to create graphs using bokeh codes, interactivity on 
bokeh graph are achievable with tools like Hovertools, while widgets tools for interactivity are achievable 
using bokeh server. This section will be using bokeh server to build graphs rather than the usual bokeh

widgets allow user to interact with the graph

Bokeh server has tornado embedded which allows it to serve application
"""


# prepare bokeh output file: this is used to create a static output file
# output_file("simple_bokeh.html")

# Create widgets
text_input = TextInput(value="Ayodeji")
button = Button(label="Generate Text")
output = Paragraph()


def update():
    output.text = "Hello " + text_input.value


button.on_click(update)

lay_out = layout([[button, text_input], [output]])

# # run with python widgets.py
# show(lay_out)

# # run with python -m bokeh serve widgets.py   OR   bokeh serve widgets.py   OR  bokeh serve widgets.py --port 5000
curdoc().add_root(lay_out)
