from flask import Flask, render_template, redirect, request, session  
app = Flask(__name__)
app.secret_key = 'I is secret'
import random

@app.route('/')          
def game_home():
    if 'rando' not in session:
        session['rando'] = random.randint(1, 100)
    return render_template('/index.html')

@app.route('/counter', methods = ['POST'])     
def counting():
    session['guess'] = request.form['number']
    print(session['rando'])
    if session['rando'] > int(session['guess']):
        print('Too Low')
        session['result'] = "Too Low!"
    elif session['rando'] < int(session['guess']):
        print('Too High')
        session['result'] = "Too High!"    
    else:
        print("That's Right!")
        session['result'] = "Correct!"
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def nuke_it():
    session.clear()
    return redirect('/')

if __name__=="__main__":       
    app.run(debug=True)    
