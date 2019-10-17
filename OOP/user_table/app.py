from flask import Flask, render_template, request, redirect					
from flask_sqlalchemy import SQLAlchemy			
from sqlalchemy.sql import func                         
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_table.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    email = db.Column(db.String(45))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=func.now())   
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

@app.route("/")
def test():
    return render_template("index.html")

@app.route("/add_user")
def add_user():
    create_user = User(first_name = "fname", last_name = "lname", email = "email", age = "a")
    db.session.add(create_user)
    db.session.commit()
    user = {
        "fname" : request.form["first_name"],
        "lname" : request.form["last_name"],
        "email" : request.form["form_email"],
        "a" : request.form["age"]
    }
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)