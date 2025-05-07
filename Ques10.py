# Ques 10. How do you handle errors in Flask (e.g., 404)?

# Solution 10.

from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

def factorial_recursive_with_base_case(n):
    # Base case: when n is 0, return 1
    if n == 0:
        return 1

    # Recursive call
    return n * factorial_recursive_with_base_case(n - 1)

import sys

sys.setrecursionlimit(10**6)

def fact(n):
  if(n == 0):
    return 1
  return n * fact(n - 1)

if __name__ == '__main__':
  f = 1001
  print(fact(f))
app.run(debug=True)