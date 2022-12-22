import mysql.connector as mys
mycon=mys.connect(host="localhost",user="root",password="starboy@1602",database="yolo")
ans="y"
mycursor=mycon.cursor()
while ans=="y":
    print("1.show all records\n2.create a table\n3.insert records\n4.delete records\n5.updation records\n6.Drop table\n7.Truncate table\n8.Conditional selection of records")
    ch=int(input("enter choice:"))
    if ch==1: # block executed and working
        try:
             mycursor.execute("select * from emp")
             data=mycursor.fetchall()
             nrec=mycursor.rowcount
             print("Total number of records:",nrec)
             for row in data:
                 print(row)
        except:
             print("Table doesn't exist")
             print("Total number of records:",0)                     
    if ch==2:     #block executed and working
        try:                     
             qquery="create table emp(Empid int Primary key,Name varchar(25),Department varchar(25),Salary int)"
             mycursor.execute(qquery)
             mycon.commit()
             print("Table Successfully created")
        except:
             print("Table already exist")
             nrec=mycursor.rowcount
             print("Total number of records:",nrec) 
    if ch==3:      #block "NOT" executing
        print('Insertion of data')      
        amag='yes'
        while amag=='yes':
          id=int(input("enter empid:"))
          name=input("enter name:")
          Dept=input("enter department:")
          Sal=int(input("enter salary:"))
          queery="insert into emp (Empid,Name,Department,Salary)values(id,name,Dept,Sal)" #field not defined error in name and probability
          mycursor.execute(queery) #query execution error
          mycon.commit()
          print("records saved")
          amag=input("Add more Records:")      
    if ch==4:      #block "NOT" executing
        print("Deletion of Records")
        e=int(input("Enter Empid:"))
        qqqquery="select * from emp where Empid=%s"%(e,)
        mycursor.execute(qqqquery) #query execution error
        data=mycursor.fetchone()
        if data!=None:
            querry="delete from emp where Empid={}".format(e)
            mycursor.execute(querry) #query execution error
            mycon.commit()
            print("records deleted successfully")
        else:
            print("No such employee")     
    if ch==5:      #block execited and working
        print("Updation of salary")
        e=int(input("enter Empid:"))
        queryy="select * from emp where Empid={}".format(e)
        mycursor.execute(queryy)
        data=mycursor.fetchone()
        try:
             if data!=None:
                 quueryy="update emp set Salary=Salary+1000 where Empid=%s"%(e,)
                 mycursor.execute(quueryy)  #query execution error
                 mycon.commit()
             else:
                 print("No such employee") 
        except:
            print("No such Record")         
    if ch==6:
        try:
             mycursor.execute("drop table emp")
             print("Table successfully deleted from databse")
        except:
            print("No such tables exist")     
    if ch==7:
        try:
             mycursor.execute("truncate table emp")  
             print("Table successfully emptied\ncontents of the table cannot be retrieved")
        except:
            print("The tables is already empty")     
    if ch==8:
        print("coditional selection")      
    ans=input("do you want to continue:")
    
def create_database_and_table():
    query="CREATE DATABASE IF NOT EXISTS Student Management System"
    mycursor=mycon.cursor()
    mycursor.execute(query)

    query="USE Student Management System"
    mycursor.execute(query)

    query="""CREATE TABLE IF NOT EXISTS Student_details( 
        Sid INT NOT NULL PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Father's_name VARCHAR(50) NOT NULL,
        Mother's_name VARCHAR(50) NOT NULL,
        Father's_occupation VARCHAR(30) NOT NULL,
        Mother's_occupation VARCHAR(30) NOT NULL,
        D.O.B DATE NOT NULL,
        Age INT NOT NULL,
        Gender VARCHAR(20) NOT NULL,
        Contact INT NOT NULL,
        Address VARCHAR(99) NOT NULL,
        Blood_group VARCHAR(20) NOT NULL)"""
    mycursor.execute(query)

    query="""CREATE TABLE IF NOT EXISTS Attendance(
        Total_days INT NOT NULL,
        No_of_presentdays INT NOT NULL,
        No_of_absentdays INT NOT NULL,
        Attendance% INT NOT NULL)"""
    mycursor.execute(query)

    query="""CREATE TABLE IF NOT EXISTS Academic performance(
        Examination VARCHAR(40) NOT NULL,
        English INT NOT NULL,
        Maths INT NOT NULL,
        Chemistry INT NOT NULL,
        Physics INT NOT NULL,
        Computer_Science INT NOT NULL
        Total_marks INT NOT NULL,
        Percentage_scored INT NOT NULL)"""
    mycursor.execute(query)
    