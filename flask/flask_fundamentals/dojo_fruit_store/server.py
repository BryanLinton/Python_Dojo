from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name_from_order = request.form['first_name']
    last_name_from_order = request.form['last_name']
    optional_id = request.form['student_id']
    number_of_strawberries = request.form['strawberry']
    number_of_raspberries = request.form['raspberry']
    number_of_apples = request.form['apple']
    number_of_blackberries = request.form['blackberries']
    count = int(number_of_strawberries) + int(number_of_raspberries) + int(number_of_apples) + int(number_of_blackberries)
    customer_name = first_name_from_order + " " + last_name_from_order
    print("Charging" + " " + str(customer_name) + " " + "for" + " " + str(count) + " " + "fruits")
    return render_template("checkout.html", first_name = first_name_from_order, last_name = last_name_from_order,
    student_id = optional_id, strawberry = number_of_strawberries, raspberry = number_of_raspberries,
    apple = number_of_apples, blackberry = number_of_blackberries, total = count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    