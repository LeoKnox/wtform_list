from application import app, db
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", nav_index="active")

class ListOne(db.Document):
    list_id     =   db.IntField( unique=True )
    item_one    =   db.StringField()

@app.route("/list")
def list():
    #ListOne(list_id = 1, item_one="Red").save()
    #ListOne(list_id = 2, item_one="Blue").save()
    items = ListOne.objects.all()
    return render_template("list.html", items=items, nav_list="active")
