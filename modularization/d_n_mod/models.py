from sqlalchemy.sql import func
from config import db

class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(db.Integer, db.ForeignKey("dojo.id"), nullable=False)
    uDojo = db.relationship("Dojo", foreign_keys=[dojo_id], backref="user_dojo", cascade="all")
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Dojo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dojo_name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())