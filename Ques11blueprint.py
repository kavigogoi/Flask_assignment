from flask import Blueprint

bp = Blueprint("blueprint", __name__)

@bp.route("/")
def home():
    return "<h1>Hello Kavita Gogoi</h1>"
@bp.route("/user")
def user_info():
    return "<h1>User Info</h1>"


