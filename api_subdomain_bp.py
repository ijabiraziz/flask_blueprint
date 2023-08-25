from flask import Blueprint

api_blueprint = Blueprint("api", __name__, subdomain="api")


@api_blueprint.route("/")
def api_home():
    return "<h3>API home</h3>"
