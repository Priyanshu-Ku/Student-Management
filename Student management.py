import mysql.connector as mys
mycon=mys.connect(host="localhost",user="root",password="starboy@1602",database="yolo")
ans="y"
found=False
mycursor=mycon.cursor()
while ans=="y":
    print("1.show all records\n2.create a table\n3.insert records\n4.delete records\n5.updation records\n6.Drop table\n7.Truncate table")
    ch=int(input("enter choice:"))
    if ch==1: # block executed and working
        try:
             mycursor.execute("select * from emp")
             data=mycursor.fetchall()
             nrec=mycursor.rowcount
             print("Total number of records:",nrec)
             for row in data:
                 print(row)
             found=True
        except:
             print("Table doesn't exist")
             print("Total number of records:",0)                     
    if ch==2:     #block executed and working
        try:                     
             qquery="create table emp(Empid int Primary key,Name varchar(25),Department varchar(25),Salary int)"
             mycursor.execute(qquery)
             mycon.commit()
             print("table created")
             found=True
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
          queery='''insert into emp (Empid,Name,Department,Salary)values('int(id)','name','Dept','int(Sal)')''' #field not defined error in name and probability
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
    if ch==5:      #block "NOT" executing
        print("Updation of salary")
        e=int(input("enter Empid:"))
        queryy="select * from emp where Empid={}".format(e)
        mycursor.execute(queryy)
        data=mycursor.fetchone()
        if data!=None:
            quueryy="update emp set Salary=Salary+1000 where e={}".format(e)
            mycursor.execute(quueryy)  #query execution error
            mycon.commit()
        else:
            print("No such employee") 
    if ch==6:
        mycursor.execute("drop table emp")
        print("Table successfully deleted from databse")
    if ch==7:
        mycursor.execute("truncate table emp")  
        print("Table successfully emptied\ncontents of the table cannot be retrieved")  
    ans=input("do you want to continue:")
    
