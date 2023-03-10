from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninjas_model import Ninja


@app.route('/add/ninja', methods=['post'])
def ninja():
    print(request.form)
    Ninja.new_ninja(request.form)
    return redirect('/')