from flask import Blueprint
from .main import main

main_bp = Blueprint('main', __name__)
main_bp.register_blueprint(main)
