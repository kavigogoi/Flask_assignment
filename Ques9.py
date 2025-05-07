# Ques 9. How do you redirect to a different route in Flask?

# Solution 9.

from flask import Flask, redirect
 
# instance of flask application
app = Flask(__name__)
 
# home route that redirects to 
# helloworld page
@app.route("/")
def home():
    return redirect("/helloworld")
 
# route that returns hello world text
@app.route("/helloworld")
def hello_world():
    return "<p>Hello, World from \
                redirected page.!</p>"
 
 
if __name__ == '__main__':
    app.run(debug=True)