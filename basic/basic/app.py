from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask (__name__)
app.config['SECRET_KEY'] = "secret_key"
debug = DebugToolbarExtension(app)

@app.route("/")
def import_form():
    """Render form to ask for input"""

    prompts= story.prompts

    return render_template("input.html", prompts = prompts)

@app.route("/story")
def render_story():
    """show result"""

    text = story.generate(request.args)

    render = render_template("story.html", text=text)