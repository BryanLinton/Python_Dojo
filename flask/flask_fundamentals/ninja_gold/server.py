from flask import Flask, render_template, redirect, request, session  
app = Flask(__name__)
app.secret_key = "make dat money"
import random

@app.route('/')          
def gold():
    if 'available_gold' not in session:
        session['available_gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods = ['POST', 'GET'])
def get_rich():    
 
    if request.form['building'] == 'farm':
        gold = random.randint(10, 20)
        session['available_gold'] += gold
        print(session['available_gold'])

    elif request.form['building'] == 'cave':
        gold = random.randint(5, 10)
        session['available_gold'] += gold
        print(session['available_gold'])

    elif request.form['building'] == 'house':
        gold = random.randint(2, 5)
        session['available_gold'] += gold
        print(session['available_gold'])

    elif request.form['building'] == 'casino':
        gold = random.randint(-50, 50)
        session['available_gold'] += gold
        print(session['available_gold'])
        
    return redirect('/')

@app.route('/reset_game', methods = ['POST', 'GET'])    
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)   
