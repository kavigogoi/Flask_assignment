# Ques 4. How do you render HTML templates in Flask?

# Solution 4.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run()