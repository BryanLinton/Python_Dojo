from flask import Flask, render_template, request, redirect	
from config import app, db, migrate
from models import User, Dojo			

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

