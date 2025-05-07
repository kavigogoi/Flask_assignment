# Ques 6. How do you handle forms in Flask?

# Solution 6.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    email = request.form["email"]
    return f"Hello, {username}! Your email is {email}"
        
if __name__ == '__main__':
    app.run(debug=True)