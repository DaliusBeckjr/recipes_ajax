from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import user
from flask import jsonify


@app.route('/')
def root():
    return render_template('register_login.html')

@app.route('/users/login', methods = ['POST'])
def login():
    pass 

@app.route('/users/login_validation', methods = ['POST'])
def validate_login():
    valid_user = user.User.validate_login(request.form)
    if not valid_user:
        return jsonify( {'error' : valid_user} )

    return jsonify( {'message' : 'route is successful'} )

@app.route('/users/reg_validation', methods = ['POST'])
def validate_reg():
    valid_user = user.User.validate_register(request.form)

    if valid_user:
        return jsonify( {'error' : valid_user } )

    return jsonify( {'status' : 201 } )


@app.route('/users/registration', methods = ['POST'])
def register():
    user_id = user.User.save(request.form)
    session['user_id'] = user_id

    return jsonify( {'status' : 201 } )

