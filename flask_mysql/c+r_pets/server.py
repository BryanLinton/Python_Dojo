from flask import Flask, render_template, redirect, request
from pets_sql import connectToMySQL

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL("pets")
    pets = mysql.query_db('SELECT * FROM pets_input')
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    mysql = connectToMySQL("pets")
    query = "INSERT INTO pets_input (name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, now(), now())"
    data = {
        "n": request.form["name"],
        "t": request.form["type"]
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect ("/")
if __name__ == "__main__":
    app.run(debug=True)    