from flask import Flask, render_template, redirect, request
from users_sql import connectToMySQL

app = Flask(__name__)

@app.route("/users")
def display_users():
    mysql = connectToMySQL("manage_users")
    users = mysql.query_db("SELECT users.id, concat(users.first_name, ' ', users.last_name) AS full_name, users.email, users.created_at FROM users")
    print(users)
    return render_template("users.html", all_users = users)

if __name__ == "__main__":
    app.run(debug=True) 