from flask import Flask , render_template, request, redirect ,session
app = Flask(__name__)
app.secret_key = ' keep it secret , keep it safe'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def process():
    # print("Request Object",request.form,"-"*25)
    # ! NEVER EVER EVER RENDER ON POST REQUEST 
    session['username'] = request.form['username']
    session['age'] = request.form['user_age']
    session['food'] = request.form['fav_food']
    return redirect('/display')
    # return render_template("display.html",name = request.form['username'], age = request.form['user_age'], food = request.form['fav_food'])

@app.route('/display')
def display():
    print("Session Object === ",session,"-"*25)
    return render_template("display.html")

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/display')

if __name__ == '__main__':
    app.run(debug = True, port=5002)