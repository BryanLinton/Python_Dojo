from flask import Flask, render_template, request, redirect, session  
app = Flask(__name__) 
app.secret_key = 'goobly glop'   

@app.route('/')
def hello_counter():  
    if "visits" in session:
        session['visits'] = int(session['visits']) + 1
        print('key exists!')
        return render_template("index.html")
    else:
        print("key doesnt exist")
        session['visits'] = 1
        return render_template("index.html")

@app.route('/destroy_session')
def nuke_it():
    print('boom!!')
    session.clear()
    return redirect('/')

if __name__=="__main__":      
    app.run(debug=True)    
