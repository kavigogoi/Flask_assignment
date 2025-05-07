# Ques 5. How can you generate URLs for routes in Flask using url_for?

# Solution 5.

from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to kavitagogoipodcast!"

@app.route("/student")
def student():
    return "welcome students to kavita's podcast!"
@app.route("/faculty")
def faculty():
    return "welcome faculty to kavita's podcast"

@app.route("/user/<name>")
def user(name):
    if name=="student":
        return redirect(url_for("student"))
    if name=="faculty":
        return redirect(url_for("faculty"))
 
app.run(debug=True)