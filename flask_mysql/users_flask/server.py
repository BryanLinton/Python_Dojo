from flask import Flask, render_template, redirect, request
from users_sql import connectToMySQL

app = Flask(__name__)

@app.route("/users")
def display_users():
    mysql = connectToMySQL("manage_users")
    users = mysql.query_db("SELECT users.id, concat(users.first_name, ' ', users.last_name) AS full_name, users.email, users.created_at FROM users")
    print(users)
    return render_template("users.html", all_users = users)

@app.route("/users/new", methods=["GET"])
def create_user():
    return render_template("new.html")

@app.route("/users/create", methods=["POST"])
def query_user():
    mysql = connectToMySQL("manage_users")
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    new_user_id = mysql.query_db(query, data)
    return redirect("/users/show/<id>")

@app.route("/users/show/", methods=["GET"])
def view_new_user():
    mysql = connectToMySQL("manage_users")
    user = mysql.query_db("SELECT id, concat(first_name, ' ', last_name) AS full_name, email, created_at, updated_at FROM users")
    return render_template("user_profile.html", current_user = user)

if __name__ == "__main__":
    app.run(debug=True) 