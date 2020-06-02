from flask import Flask
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="flaskhtmldb"
)

from application import routes