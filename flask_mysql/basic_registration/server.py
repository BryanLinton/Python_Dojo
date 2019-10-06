from flask import Flask, render_template, request, redirect, flash
from sqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = ("secret")

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/validation", methods=["POST"])
def validate_form():
    is_valid = True

    if len(request.form["first_name"]) < 1:
        is_valid = False
        flash("First name can not be blank")
    
    if len(request.form["last_name"]) < 1:
        is_valid = False
        flash("Last name can not be blank")

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
        mysql = connectToMySQL("basic_registration")
        query = "INSERT INTO registration (first_name, last_name, password, pw_cnfm, created_at) VALUES (%(fname)s, %(lname)s, %(pass)s, %(cf_pass)s, now());"
        data = {
            "fname" : request.form['first_name'],
            "lname" : request.form['last_name'],
            "pass" : request.form['password'],
            "cf_pass" : request.form["conf_pass"]
        }
        mysql.query_db(query, data)  
        flash("You successfully registered!")
        return redirect ("/")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)