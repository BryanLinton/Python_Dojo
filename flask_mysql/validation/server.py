from flask import Flask, render_template, request, redirect, flash
from sqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = ("hoopla")

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/validation", methods=["POST"])
def validate_form():
    is_valid = True

    if len(request.form["full_name"]) < 1:
        is_valid = False
        flash("Name can not be blank")

    if len(request.form["comments"]) > 120:
        is_valid = False
        flash("comment can not be more than 120 characters")

    if is_valid:
        mysql = connectToMySQL("validation")
        query = "INSERT INTO users (name, location, language, comment) VALUES (%(n)s, %(l)s, %(lan)s, %(com)s);"
        data = {
            "n" : request.form['full_name'],
            "l" : request.form['location'],
            "lan" : request.form['language'],
            "com" : request.form['comments']
        }
        id = mysql.query_db(query, data)  
        return redirect ("/result/{}".format(id))
    else:
        return redirect("/")

@app.route("/result/<id>")
def survey_result(id):
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    data = {
        "user_id" : id
    }
    mysql = connectToMySQL("validation")
    survey_info = mysql.query_db(query, data)
    return render_template("result.html", result = survey_info[0])

if __name__ == "__main__":
    app.run(debug=True)
