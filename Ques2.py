# Ques 2. How do you serve static files like images or CSS in Flask?

# Solution

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    message = "Hello world"
    return render_template("index.html",message=message)

if __name__ == "__main__":
    app.run(debug=True)