from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class AccountModel(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, pimary_key = True)
    username = db.Column(db.String, unique = True)
    password_hash = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    
    def __repr__(self):
        return f'<Username: {self.username}>'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def from_dict(self, dict):
        password = dict.pop('password')
        self.hash_password(password)
        for k,v in dict.items():
            setattr(self, k, v)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()