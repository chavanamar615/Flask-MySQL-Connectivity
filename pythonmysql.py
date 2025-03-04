from flask import Flask,render_template,request,redirect,url_for
import mysql.connector

app=Flask(__name__)
con=mysql.connector.connect(host="localhost",user="root",password="Amar@2915",database="amar2_db")
cursor=con.cursor()
@app.route("/addstud",methods=["GET","POST"])
def addstud():
    if(request.method=="GET"):
        return render_template("connect.html")
    else:
        sname=request.form["sname"]
        percentage=request.form["percentage"]
        age=request.form["age"]
        sql="insert into student(sname,percentage,age) values(%s,%s,%s)"
        val=(sname,percentage,age)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showallstud"))
    
@app.route("/showallstudent")
def showallstud():
    sql="select * from student"
    cursor.execute(sql)
    students=cursor.fetchall()
    return render_template("showallstudent.html",students=students) 

@app.route("/deleteStudent/<sid>",methods=["GET","POST"])
def deletestud(sid):
    if(request.method=="GET"):
        return render_template("deleteconfirm.html")
    else:
        action=request.form["action"]
        if(action=="Yes"):
            sql="delete from student where sid=%s"
            val=(sid,)
            cursor.execute(sql,val)
            con.commit()
        return redirect(url_for("showallstud"))

@app.route("/editStudent/<sid>",methods=["GET","POST"]) #editStudent==anchor tag
def editstudent(sid):
    if(request.method=="GET"):
        sql="select * from student where sid=%s"
        val=(sid,)
        cursor.execute(sql,val)
        student=cursor.fetchone()
        return render_template("editstudent.html",stud=student)
    else:
        sname=request.form["sname"]
        percentage=request.form["percentage"]
        age=request.form["age"]
        sql="update student set sname=%s,percentage=%s,age=%s where sid=%s"
        val=(sname,percentage,age,sid)
        cursor.execute(sql,val)
        return redirect(url_for("showallstud"))
                
if(__name__)=="__main__":
    app.run(debug=True)      
        