from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "madlibs123"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    return render_template("home.j2")


@app.route('/form')
def show_form():
    return render_template("form.j2")


@app.route('/story')
def get_story():
    prompt = ["place", "noun", "verb", "adj", "plural_noun"]

    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adj = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    answers = {"place": place,
               "noun": noun,
               "verb": verb,
               "adjective": adj,
               "plural_noun": plural_noun,
               }
    generated_story = story.generate(answers)
    return render_template("story.j2", my_story=generated_story, **answers)
