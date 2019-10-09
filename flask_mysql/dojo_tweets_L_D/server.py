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
        # conf_pw_hash = bcrypt.generate_password_hash(request.form['conf_pass'])
        mysql = connectToMySQL("dojo_tweets")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(fname)s, %(lname)s, %(em)s, %(pass)s, now());"
        data = {
            "fname" : request.form['first_name'],
            "lname" : request.form['last_name'],
            "em" : request.form["email"],
            "pass" : pw_hash
        }
        id = mysql.query_db(query, data) 
        session["id"] = id 
        flash("You successfully registered!")
        return redirect ("/dashboard")
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
        mysql = connectToMySQL("dojo_tweets")
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = { 
            "email" : request.form["lemail"] 
        }
        user = mysql.query_db(query, data)

        if not user:
            flash("User not found")
            return redirect ("/")
        
        if not bcrypt.check_password_hash(user[0]["password"], request.form["lpassword"]):
            is_valid = False
            flash("Password is not valid")
    
        if is_valid:
            session["id"] = user[0]["id"]
            return redirect ("/dashboard")
        else:
            flash("User not found")
            return redirect ("/")

@app.route("/dashboard")
def tweet_home():
    if 'id' not in session:
        return redirect("/")

    mysql = connectToMySQL('dojo_tweets')
    query = "SELECT * FROM users WHERE id = %(id)s"
    data = {'id': session['id']}
    user = mysql.query_db(query, data)

    mysql = connectToMySQL("dojo_tweets")
    query = "SELECT users.first_name, tweets.content, tweets.created_at, tweets.id FROM tweets JOIN users ON tweets.users_id = users.id ORDER BY tweets.created_at DESC"
    tweets = mysql.query_db(query)

    mysql = connectToMySQL("dojo_tweets")
    query = "SELECT tweet_id FROM liked_tweets WHERE user_id = %(user_id)s"
    data = {
        "user_id": session["id"]
    }
    liked_tweets = [ tweet ["tweet_id"] for tweet in mysql.query_db(query,data) ]
    return render_template("dashboard.html", user=user[0], tweets = tweets, liked_tweets = liked_tweets)

@app.route("/tweets/create", methods=["POST"])
def post_tweet():
    if "id" not in session:
        return redirect("/")

    is_valid = True
    if len(request.form["post_tweet"]) < 1:
        is_valid = False
        flash("Tweet can not be blank")
    if len(request.form["post_tweet"]) > 255:
        is_valid = False
        flash("Tweet can not be more than 255 characters")

    if is_valid:
        mysql = connectToMySQL("dojo_tweets")
        query = "INSERT INTO tweets (content, users_id, created_at) VALUES (%(content)s, %(user_id)s, NOW())"
        data = {
            "user_id": session["id"],
            "content": request.form["post_tweet"]
        }
        mysql.query_db(query, data)
        return redirect("/dashboard")
    else:
        return redirect ("/dashboard")

@app.route("/like_tweet/<tweet_id>")
def user_liked_tweet(tweet_id):
    mysql = connectToMySQL("dojo_tweets")
    query = "INSERT INTO liked_tweets (user_id, tweet_id) VALUES (%(user_id)s, %(tweet_id)s)"
    data = {
        "user_id" : session["id"],
        "tweet_id" : tweet_id
    }
    mysql.query_db(query, data)
    return redirect("/dashboard")

@app.route("/unlike_tweet/<tweet_id>")
def user_unlike_tweet(tweet_id):
    mysql = connectToMySQL("dojo_tweets")
    query = "DELETE FROM liked_tweets WHERE user_id = %(user_id)s AND tweet_id = %(tweet_id)s"
    data = {
        "user_id" : session["id"],
        "tweet_id" : tweet_id
    } 

    mysql.query_db(query, data)
    return redirect ("/dashboard")





@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)