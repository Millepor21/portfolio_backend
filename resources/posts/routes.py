from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from resources.accounts.AccountModel import AccountModel
from schemas import PostSchema
from . import bp
from .PostModel import PostModel

@bp.route('/post')
class PostList(MethodView):

    @bp.response(200, PostSchema(many=True))
    def get(self):
        posts = PostModel.query.all()
        return posts
    
    @jwt_required()
    @bp.arguments(PostSchema)
    @bp.response(200, PostSchema)
    def post(self, post_data):
        author_id = get_jwt_identity()
        author = AccountModel.query.get(author_id)
        if author:
            post = PostModel(**post_data, author_id=author_id)
            try:
                post.save()
                return post
            except IntegrityError:
                abort(400, message='Please create an account')
        abort(400, message='Create an account to make a post')

    