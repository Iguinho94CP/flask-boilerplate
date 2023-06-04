# myapp/app/routes/auth/auth_views.py
from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return 'Login route'

@auth_bp.route('/register')
def register():
    return 'Register route'
