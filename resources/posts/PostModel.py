from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class PostModel(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String, nullable = False)
    post = db.Column(db.String, nullable = False)
    

    def __repr__(self):
        return f'<Author: {self.author} Post: {self.post}>'
    
    def from_dict(self, dict):
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()