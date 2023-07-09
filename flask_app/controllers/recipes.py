from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import user, recipe
from flask import jsonify



@app.route('/recipes/dashboard')
def dashboard():

    return render_template('dashboard.html')


@app.route('/recipes')
def recipes():

    return jsonify( recipe.Recipe.get_all_recipes() )



@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    print (request.form)
    # save the information of recipe
    recipe.Recipe.save_recipe(request.form)
    return jsonify({'status' : 201})