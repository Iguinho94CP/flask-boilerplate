# myapp/app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import auth_bp, customer_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)

    return app
