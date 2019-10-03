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
def insert_user():
    mysql = connectToMySQL("manage_users")
    query = "INSERT INTO users (first_name, last_name, email, created_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"]
    }
    new_user_id = mysql.query_db(query, data)
    return redirect("/users/{}".format(new_user_id))

@app.route("/users/<user_id>")
def view_user(user_id):
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
        "user_id": id
    }
    mysql = connectToMySQL('manage_users')
    user = mysql.query_db(query, data)
    return render_template("user_profile.html", user = user[0])

@app.route("/delete/<user_id>")
def delete_user(user_id):
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        "user_id": id
    }
    mysql = connectToMySQL('manage_users')
    user = mysql.query_db(query, data)
    return redirect("/users")    

@app.route("/update_user/<user_id>", methods=['POST'])
def update_user(user_id):
    query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, description=%(dsc)s, updated_at=NOW()"
    data = {
      'fn': request.form['fname'],
      'ln': request.form['lname'],
      'em': request.form['email'],
    }
    mysql = connectToMySQL('manage_users')
    mysql.query_db(query, data)
    return redirect('/users/{}'.format(user_id))

if __name__ == "__main__":
    app.run(debug=True)