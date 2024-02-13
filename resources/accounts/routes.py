from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources.posts.PostModel import PostModel
from schemas import AccountSchema
from . import bp 
from .AccountModel import AccountModel

@bp.route('/account')
class AccountList(MethodView):

    @bp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()
    