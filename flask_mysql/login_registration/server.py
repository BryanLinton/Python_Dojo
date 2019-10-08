from flask import Flask, render_template, request, redirect, flash, session
from sqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = ("secret")
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route("/validation", methods=["POST"])
def validate_form():
    is_valid = True

    if len(request.form["first_name"]) < 1:
        is_valid = False
        flash("First name can not be blank")
    
    if len(request.form["last_name"]) < 1:
        is_valid = False
        flash("Last name can not be blank")

    if len(request.form["email"]) < 1:
        is_valid = False
        flash("Email can not be blank")

    if not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid email address" )

    if len(request.form["password"]) < 5:
        is_valid = False
        flash("Password must be at least 5 characters")

    if len(request.form["conf_pass"]) < 1:
        is_valid = False
        flash("Confirm password can not be blank")

    if request.form["conf_pass"] != request.form["password"]:
        is_valid = False
        flash("Passwords must match")

    if is_valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        conf_pw_hash = bcrypt.generate_password_hash(request.form['conf_pass'])
        mysql = connectToMySQL("basic_registration")
        query = "INSERT INTO registration (first_name, last_name, email, password, pw_cnfm, created_at) VALUES (%(fname)s, %(lname)s, %(em)s, %(pass)s, %(cf_pass)s, now());"
        data = {
            "fname" : request.form['first_name'],
            "lname" : request.form['last_name'],
            "em" : request.form["email"],
            "pass" : pw_hash,
            "cf_pass" : conf_pw_hash
        }
        id = mysql.query_db(query, data) 
        session["id"] = id 
        flash("You successfully registered!")
        return redirect ("/success")
    else:
        return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    is_valid = True

    if len(request.form['lemail']) < 1:
        is_valid = False
        flash("Please enter your email")

    if len(request.form['lpassword']) < 1:
        is_valid = False
        flash("Please enter your password")

    if not is_valid:
        return redirect("/")

    else:
        mysql = connectToMySQL("basic_registration")
        query = "SELECT * FROM registration WHERE email = %(email)s;"
        data = { 
            "email" : request.form["lemail"] 
        }
        user = mysql.query_db(query, data)

        if user:
            hashed_password = user[0]["password"]
    
            if bcrypt.check_password_hash(user[0]["password"], request.form["lpassword"]):
                session["id"] = user[0]["id"]
                flash("You successfully logged in!")
                return redirect ("/success")
            else:
                flash("Please us a valid email address")
                return redirect ("/")

@app.route("/success")
def landing():
    if 'id' not in session:
        return redirect("/")

    mysql = connectToMySQL('basic_registration')
    query = "SELECT * FROM registration WHERE id = %(id)s"
    data = {'id': session['id']}
    user = mysql.query_db(query, data)

    return render_template("success.html", user=user[0])

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)