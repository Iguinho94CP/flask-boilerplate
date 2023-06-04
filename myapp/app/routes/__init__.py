# myapp/app/routes/__init__.py
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
customer_bp = Blueprint('customer', __name__, url_prefix='/customer')

from app.routes.auth.auth_views import *
from app.routes.customer.customer_views import *
