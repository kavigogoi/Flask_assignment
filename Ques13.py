# Ques 13. How can you redirect with query parameters in Flask?

# Solution 13.


from flask import Flask, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
    return '''<form action="/goto" method="POST">
            <input name="username">
            <input type="submit" value="Go">
        </form>'''

@app.route('/goto', methods=['POST'])
def login_post():
    username = request.form.get('username')
    if username is None or username == '':
        return redirect(url_for('user_page_central'))
    return redirect(url_for('user_page', name = username))

@app.route('/user/')
def user_page_central():
    return 'List of users'

@app.route('/user/<name>')
def user_page(name):
    return f'Page of {name}'

app.run(debug=True)