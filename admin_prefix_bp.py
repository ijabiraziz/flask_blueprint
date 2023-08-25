from flask import Blueprint

# Create a blueprint with a URL prefix
admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blueprint.route("/")
def admin_dashboard():
    return "Admin dashboard"


@admin_blueprint.route("/<name>")
def admin_online(name):
    return f"<h3>Admin Online {name}</h3>"
