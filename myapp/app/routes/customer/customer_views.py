# myapp/app/routes/customer/customer_views.py
from flask import Blueprint

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/')
def index():
    return 'Customer index route'

@customer_bp.route('/profile')
def profile():
    return 'Customer profile route'
