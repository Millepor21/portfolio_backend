from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from Config import Config
app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from resources.accounts import bp as account_bp
api.register_blueprint(account_bp)
from resources.posts import bp as post_bp
api.register_blueprint(post_bp)

from resources.accounts.AccountModel import AccountModel
from resources.posts.PostModel import PostModel