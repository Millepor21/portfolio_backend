from flask_smorest import Blueprint

bp = Blueprint('accounts',__name__)

from . import routes, auth_routes