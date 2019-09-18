from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def survey_result():
    print("Returned Survey Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    favorite_language = request.form['language']
    comments = request.form['comments']
    return render_template("result.html", name_from_form, location_from_form, favorite_language, comments)

if __name__ == "__main__":
    app.run(debug=True)
