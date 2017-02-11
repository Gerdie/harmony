from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

#For debugging - see Jinja fails
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True


@app.route('/')
def show_home():
    """Display homepage"""

    return render_template("index.html")

if __name__ == "__main__":
    # Change app.debug to False before launch
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run
