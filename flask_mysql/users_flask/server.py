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
    id = mysql.query_db(query, data)
    return redirect("/users/{}".format(id))

@app.route("/users/<id>")
def view_user(id):
    mysql = connectToMySQL('manage_users')
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
         "user_id": id
    }
    user = mysql.query_db(query, data)
    return render_template("user_profile.html", user = user[0])

@app.route("/delete/<id>")
def delete_user(id):
    mysql = connectToMySQL('manage_users')
    query = "DELETE FROM users WHERE id = %(user_id)s"
    data = {
        "user_id": id
    }
    user = mysql.query_db(query, data)
    return redirect("/users")

@app.route("/update_user/<id>", methods=['POST'])
def update_user(id):
    mysql = connectToMySQL('manage_users')
    query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, updated_at = NOW() WHERE id = %(user_id)s"
    data = {
      'fn': request.form['fname'],
      'ln': request.form['lname'],
      'em': request.form['email'],
      'user_id': id
    }
    mysql.query_db(query, data)
    return redirect('/users/{}'.format(id))

@app.route("/edit_user/<id>")
def edit_user(id):
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
        'user_id': id
    }
    mysql = connectToMySQL('manage_users')
    user = mysql.query_db(query, data)
    return render_template("edit_user.html", user = user[0])    


if __name__ == "__main__":
    app.run(debug=True)