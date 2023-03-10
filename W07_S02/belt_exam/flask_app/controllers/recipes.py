from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("new_recipe.html")

@app.route('/recipes/create', methods=['post'])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect('/recipes/new')
    data = {
        **request.form,
        'user_id':session['user_id']
    }
    Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    recipe = Recipe.get_by_id({'id':recipe_id})
    return render_template("edit_recipe.html" ,recipe = recipe)

@app.route('/recipes/update', methods=['post'])
def update():
    if not Recipe.validate(request.form):
        return redirect('/recipes/edit'+request.form['id'])
    Recipe.update_recipe(request.form)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:recipe_id>')
def remove(recipe_id):
    Recipe.delete({'id':recipe_id})
    return redirect('/dashboard')

@app.route('/recipes/<int:recipe_id>')
def view_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    one_recipe = Recipe.get_by_id({'id':recipe_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template("one_recipe.html", recipe = one_recipe, user = user)