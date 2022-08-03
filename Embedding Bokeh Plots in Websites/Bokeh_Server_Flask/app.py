# flask app

from flask import Flask, render_template
from datetime import datetime
from bokeh.embed import server_session  # use server_session instead of autoload_server
from bokeh.client import pull_session

"""
server_session is a function that returns the source code for bokeh scripts
pull_session enables bokeh to be pulled from flask
To allow bokeh with flask, you need to run the command for bokeh serve like below to include flask local port so as to
allow flask display it on the web
"bokeh serve --allow-websocket-origin=127.0.0.1:5000 random_generator.py"
                                    OR
"bokeh serve random_generator.py --host="*"


1. python manage.py startapp bokehapp
2. Change 'DIRS': [] to 'DIRS': [os.path.join(BASE_DIR, 'bokehapp/templates')], inside TEMPLATES contained
    settings.py
"""

# instantiate the flask app
app = Flask(__name__)


# create index page function
# @app.route("/")
# def index():
#     return render_template("index.html", context=datetime.now())


@app.route("/")
def index():
    session = pull_session(url="http://localhost:5006/random_generator")
    bokeh_scripts = server_session(
        None, url="http://localhost:5006/random_generator", session_id=session.id
    )
    return render_template("index.html", bokeh_scripts=bokeh_scripts)


# run the app with "python app.py"
# set your debug = false when you are deploying your application
if __name__ == "__main__":
    app.run(debug=True)
