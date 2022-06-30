from app.model.user import User
from app import response, app, db
from flask import request
import datetime
from flask_jwt_extended import create_access_token, create_refresh_token

def index():
    try:
        user = User.query.all()
        data = listObject(user)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def listObject(data):
    datas = [singleObject(i) for i in data]
    return datas

def singleObject(data):
    datas = {
        'username': data.username, 
        'email': data.email,
        'phone': data.phone,
        'address':data.address,
        'city': data.city,
        'country': data.country,
        'name': data.name,
        'postcode': data.postcode
    }
    return datas

def detail(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], "Tidak ada data")
        else:
            data = singleObject(user)
            return response.success(data, "success")

    except Exception as e:
        print(e)

def signup():
    try:
        users = User(   
            username    = request.form.get('username'), 
            email       = request.form.get('email'),
            phone       = request.form.get('phone'),
            address     = request.form.get('address'),
            city        = request.form.get('city'),
            country     = request.form.get('country'),
            name        = request.form.get('name'),
            postcode    = request.form.get('postcode'))
        users.setPassword(
            encrypted_password = request.form.get('encrypted_password'))

        data = singleObject(users)
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        db.session.add(users)
        db.session.commit()

        return response.success({
            "email": users.email,
            "access_token": access_token,
            "username": users.username,
            "refresh_token": refresh_token
        }, "Sukses menambahkan data")

    except Exception as e:
        print(e)

def login():
    try:
        email = request.form.get('email')
        encrypted_password = request.form.get('encrypted_password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Email tidak terdaftar')
        
        if not user.checkPassword(encrypted_password):
            return response.badRequest([], 'Kombinasi password salah')
        
        data = singleObject(user)
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        
        return response.success({
            "email": data['email'],
            "access_token": access_token,
            "refresh_token": refresh_token
        }, "Sukses login")
    
    except Exception as e:
        print(e)
