from app import app
from app.controller import shoppingController, userController
from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route('/')
def index():
    return 'HomePage'
    
@app.route('/api/daftar', methods=['GET', 'POST'])
def daftar():
    if request.method == 'GET':
        return 'signup'
    elif request.method == 'POST':
        return userController.signup()

@app.route('/api/masuk', methods=['GET', 'POST'])
def masuk():
    if request.method == 'GET':
        return 'login'
    elif request.method == 'POST':
        return userController.login()

@app.route('/api/users', methods=['GET'])
@jwt_required()
def users():
    return userController.index()


@app.route('/api/shoppings', methods=['GET', 'POST'])
@jwt_required()
def shoppings():
    if request.method == 'GET':
        return shoppingController.index()
    elif request.method == 'POST':
        return shoppingController.add()


@app.route('/api/shopping/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def shopping(id):
    if request.method == 'GET':
        return shoppingController.detail(id)
    elif request.method == 'PUT':
        return shoppingController.update(id)
    elif request.method == 'DELETE':
        return shoppingController.delete(id)