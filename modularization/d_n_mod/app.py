from flask import Flask, render_template, request, redirect	
from config import app, db, migrate
from sqlalchemy.sql import func				

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

@app.route("/")
def dojo_users():
    display_info = Dojo.query.all()
    return render_template("index.html", display_info = display_info)

@app.route("/add_dojo", methods=["POST"])
def add_dojo():
    create_dojo = Dojo(dojo_name = request.form["dojo"], city = request.form["city"], state = request.form["state"])
    db.session.add(create_dojo)
    db.session.commit()
    return redirect ("/")

@app.route("/add_ninja", methods=["POST"])
def add_ninja():
    create_ninja = User(first_name = request.form["first_name"], last_name = request.form["last_name"], dojo_id=request.form["dojo_name"])
    db.session.add(create_ninja)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

