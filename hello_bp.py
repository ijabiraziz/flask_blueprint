from flask import Blueprint

hello_blueprint = Blueprint("hello", __name__)


@hello_blueprint.route("/")
def main():
    return "Hello"


@hello_blueprint.route("/hello")
def hello():
    return "Hello Again"


@hello_blueprint.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name.capitalize()}."
