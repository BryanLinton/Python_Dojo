from flask import Flask, render_template, request, redirect, session  
app = Flask(__name__) 
app.secret_key = 'goobly glop'   

@app.route('/', methods = ['GET', "POST"])
def hello_counter():  
    if "visits" in session:
        session['visits'] = session.get['visits'] + 1
        print('key exists!')
        return render_template("index.html")
    else:
        print("key 'goobly glop' does not exist")
        session['visits'] = 1
        return render_template("index.html")
 
@app.route('/counter')
def counter():
    return render_template("counter.html")

if __name__=="__main__":      
    app.run(debug=True)    
