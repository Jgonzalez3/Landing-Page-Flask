# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")

@app.route("/dojos/new")
def dojos():
    return render_template("dojos.html")

# @app.route("")
# def show_form():
#     print "POSTED info"
#     name = request.form['name']
#     email = request.form['email']
#     ninjaname = request.form["ninjaname"]
#     print name
#     print email
#     print ninjaname
app.run(debug=True)