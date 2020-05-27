from application import app, db
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nav_index="active")

class list_item(db.Document):
    li_id       =   db.IntField( unique=True )
    li_data     =   db.StringField()

class ListOne(db.Document):
    list_id     =   db.IntField( unique=True )
    item_one    =   db.StringField()
    li          =   db.ReferenceField(list_item)
    list_list   =   db.ListField()

@app.route("/list")
def list():
    x = list_item(li_id=1, li_data="fly")
    print(x.li_data)
    items = ListOne.objects.all()
    return render_template("list.html", items=items, nav_list="active")

#ListOne(list_id = 1, item_one="Red").save()
#ListOne(list_id = 2, item_one="Blue").save()
#ListOne(list_id = 3, item_one="Blue", list_list=[1,2]).save()
#ListOne.objects(list_id=3).update_one(list_list=[3])
#ListOne.objects(list_id=3).update_one(push__list_list=4)
#ListOne.objects(list_id=3).update(pull__list_list=3)