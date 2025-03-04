import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
sid=int(input("enter student id which data you have to delete:"))
sql="delete from student where sid=%s"
val=(sid,) #","is mandatory where single value
cursor.execute(sql,val)
con.commit()