from flask import Flask

from hello_bp import hello_blueprint
from admin_prefix_bp import admin_blueprint
from api_subdomain_bp import api_blueprint

app = Flask(__name__)
app.register_blueprint(hello_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
