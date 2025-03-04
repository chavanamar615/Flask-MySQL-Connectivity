import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915")
cursor=con.cursor()

sql="create database amar2_db"
cursor.execute(sql)
con.commit()