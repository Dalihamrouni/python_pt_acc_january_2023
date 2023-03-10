from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojos_model import Dojo

@app.route('/')
def home():
    dojo=Dojo.get_all()
    return render_template('index.html',dojos =dojo)

@app.route('/create_dojos', methods=['post'])
def new_dojo():
    print(request.form)
    Dojo.create(request.form)
    return redirect('/')

@app.route('/add_ninja')
def new_ninja():
    return render_template('ninja.html')

@app.route('/show/<int:id>')
def get_by_id(id):
    dojo=Dojo.get_by_id({'id':id})
    return render_template('dojo.html', dojo=dojo)