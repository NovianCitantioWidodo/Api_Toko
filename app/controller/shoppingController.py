from app.model.shopping import Shopping
from app import response, app, db
from flask import request

def index():
    try:
        shopping = Shopping.query.all()
        data = listObject(shopping)
        return response.success(data, "success")
    
    except Exception as e:
        print(e)

def listObject(data):
    datas = [singleObject(i) for i in data]
    return datas

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name, 
        'createddate': data.createddate
    }
    return data

def detail(id):
    try:
        shopping = Shopping.query.filter_by(id=id).first()
        if not shopping:
            return response.badRequest([], "Tidak ada data")

        data = singleObject(shopping)
        return response.success(data, "success")

    except Exception as e:
        print(e)


def add():
    try :
        shopping = Shopping(
            name=request.form.get('name'))
        
        data = singleObject(shopping)
        db.session.add(shopping)
        db.session.commit()
        return response.success(data, 'Sukses menambahkan data')
    
    except Exception as e:
        print(e)

def update(id):
    try:
        shopping = Shopping.query.filter_by(id=id).first()
        shopping.name = request.form.get('name')
        data = singleObject(shopping)
        db.session.commit()
        return response.success(data, 'Sukses merubah data')
    
    except Exception as e:
        print(e)

def delete(id):
    try:
        shopping = Shopping.query.filter_by(id=id).first()
        data = singleObject(shopping)
        db.session.delete(shopping)
        db.session.commit()
        return response.success(data, 'Data telah dihapus')
    
    except Exception as e:
        print(e)