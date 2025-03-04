import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sql="create table student(sid int primary key auto_increment,sname varchar(20),percentage float,age int)"
cursor.execute(sql)
con.commit()