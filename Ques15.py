# Ques 15. How do you capture URL parameters in Flask?

# Solution 15. 


from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def get_info():
    username = request.args.get("username")
    age = request.args.get("age")

    return f" Hello this is homepage : {username}, this is my age : {age}"

if __name__ == '__main__':
    app.run(debug=True)