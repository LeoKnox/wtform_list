from application import app, mydb
from flask import render_template

mycursor = mydb.cursor()

@app.route("/")
@app.route("/index")
def index():
    mycursor = mydb.cursor()
    #sql = "DELETE FROM user WHERE email = %s"
    #adr = ("Stormbringer", )
    #mycursor.execute(sql, adr)
    #mydb.commit()
    #sql = "DROP TABLE IF EXISTS flaskhtmldb"
    sql = "UPDATE user SET email = %s WHERE email = %s"
    val = ("Sword", "Longsword")
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"{mycursor.rowcount}, record(s) affected")
    #print(mycursor.rowcount, "record(s) deleted")
    return render_template("index.html", nav_index="active")

@app.route("/index2")
def index2():
    #mycursor.execute("ALTER TABLE flaskhtmldb ADD COLUMN char_id INT")
    #mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")
    #sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
    #val = ("Ynzon", "Axe")
    #mycursor.execute(sql, val)
    '''val = [
        ('Red Sonya', "Sword"),
        ('Wulfgar', "Hammer")
    ]'''
    #mycursor.executemany(sql, val)
    #mydb.commit()
    #mycursor = mydb.cursor()
    #sql = "DELETE FROM user WHERE email = 'Axe'"
    #sql = "SELECT * FROM user WHERE email LIKE '%or%'"
    #sql = "SELECT * FROM user ORDER BY email"
    #mycursor.execute(sql)
    #mydb.commit()
    #print (f"{mycursor.rowcount}, record(s) deleted")
    #myresult = mycursor.fetchall()
    #for x in myresult:
    #    print(x)
    #mycursor.execute("SELECT name, email FROM user")
    #myresult = mycursor.fetchall()
    #myresult = mycursor.fetchone()
    #print(f"----> {myresult}")
    #print (f"record inserted ID:{mycursor.lastrowid}")
    return render_template("index.html", nav_index="active")