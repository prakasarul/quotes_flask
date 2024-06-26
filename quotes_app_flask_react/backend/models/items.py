from db import db

class Favquotes(db.Model):
    __tablename__ = "favquotes"
    
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))
    category = db.Column(db.String(2000))
