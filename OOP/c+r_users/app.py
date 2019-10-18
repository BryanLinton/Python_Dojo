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
    all_users = User.query.all()
    return render_template("index.html", all_users = all_users)

@app.route("/add_user", methods=["POST"])
def add_user():
    create_user = User(first_name = request.form["first_name"], last_name = request.form["last_name"], email = request.form["email"], age = request.form["age"])
    db.session.add(create_user)
    db.session.commit()
    return redirect ("/")

if __name__ == "__main__":
    app.run(debug=True)