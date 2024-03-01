from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from schemas import AuthAccount, AccountSchema
from . import bp
from .AccountModel import AccountModel

@bp.post('/register')
@bp.arguments(AccountModel)
@bp.response(201, AccountSchema)
def register(account_data):
    account = AccountModel()
    account.from_dict(account_data)
    try:
        account.save()
        return account_data
    except IntegrityError:
        abort(400, message='Username Already Taken')

@bp.post('/login')
@bp.arguments(AuthAccount)
def login(login_info):
    account = AccountModel.query.filter_by(username=login_info['username']).first()
    if account and account.check_password(login_info['password']):
        access_token = create_access_token(identity=account.id)
        return {'access_token':access_token}
    abort(400, message='Invalid Username or Password')