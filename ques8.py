# Ques 8. How do you manage sessions in Flask?

# Solution.

from flask import Flask, render_template_string, request, session, redirect, url_for

from datetime import timedelta

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Replace with a strong, randomly generated key
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session.permanent = True  # Mark session as permanent
        return redirect(url_for("index"))
    return """
        <form method="post">
            <input type="text" name="username" placeholder="Username">
            <button type="submit">Log in</button>
        </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)