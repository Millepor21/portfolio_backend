from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources.posts.PostModel import PostModel
from schemas import AccountSchema, AuthAccount, UpdateAccount
from . import bp 
from .AccountModel import AccountModel

@bp.route('/account')
class AccountList(MethodView):

    @bp.response(200, AccountSchema(many=True))
    def get(self):
        return AccountModel.query.all()
    
    @jwt_required()
    @bp.arguments(AuthAccount)
    def delete(self, account_data):
        account_id = get_jwt_identity()
        account = AccountModel.query.get(account_id)
        if account and account.username == account_data['username'] and account.check_password(account_data['password']):
            account.delete()
            return {'message':f'{account_data['username']} deleted'}
        abort(400, message='Username or Password Invalid')

    @jwt_required()
    @bp.arguments(UpdateAccount)
    @bp.response(202, AccountSchema)
    def put(self, account_data):
        account_id = get_jwt_identity()
        account = AccountModel.query.get(account_id)
        if account and account.check_password(account_data['password']) and account.username == account_data['username']:
            try:
                account.from_dict(account_data)
                account.save()
                return account
            except IntegrityError:
                abort(400, message='Username Already Taken')
        abort(400, message='Invalid Permisions')
    
@bp.route('/account/<account_id>')
class Account(MethodView):

    @bp.response(200, AccountSchema)
    def get(self, account_id):
        account = AccountModel.query.get_or_404(account_id, description='Account Not Found')
        return account
