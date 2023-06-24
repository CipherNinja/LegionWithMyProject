import mysql.connector

database = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = '9069076975',

)

cursor = database.cursor()

# create database 

cursor.execute("CREATE DATABASE mydatabase")
print("ALL DONE !")