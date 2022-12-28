from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow in cmd 
import mysql.connector as mys
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.iconbitmap(r'kvs.ico')


        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phoneno=StringVar() 
        self.var_address=StringVar()


        #1st
        img_1=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_1=img_1.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        self.btn_1=Button(self.root,image=self.photoimg_1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

         #2nd
        img_2=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_2=img_2.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160)

         #3rd
        img_3=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_3=img_3.resize((540,160),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1080,y=0,width=540,height=160)

        #background image
        img_4=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_4=img_4.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        background_label=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        background_label.place(x=0,y=160,width=1530,height=710)

        label_title=Label(background_label,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="blue",bg="white")
        label_title.place(x=0,y=0,width=1530,height=50)

        #manage frame  
        manage_frame=Frame(background_label,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=55,width=1500,height=560)

        #left frame 
        dataleftframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        dataleftframe.place(x=10,y=10,width=660,height=540)

        #leftimg
        img_5=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_5=img_5.resize((650,120),Image.Resampling.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        leftimg=Label(dataleftframe,image=self.photoimg_5,bd=2,relief=RIDGE)
        leftimg.place(x=0,y=0,width=650,height=120)

        #Current course labelframe infromation
        stulblframe=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        stulblframe.place(x=0,y=120,width=650,height=115)

        #Labels and Combo
        #Department
        lbl_dep=Label(stulblframe,text="Department:",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)    

        combo_dep=ttk.Combobox(stulblframe,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_std=Label(stulblframe,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std=ttk.Combobox(stulblframe,textvariable=self.var_course,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        #Year
        current_year=Label(stulblframe,font=("arial",12,"bold"),text="Year:",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2)

        com_text_current_year=ttk.Combobox(stulblframe,textvariable=self.var_year,font=("arial",12,"bold"),width=17,state="readonly")
        com_text_current_year["value"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")
        com_text_current_year.current(0)
        com_text_current_year.grid(row=1,column=1,sticky=W,padx=2)

        #Semester
        label_semester=Label(stulblframe,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        com_semester=ttk.Combobox(stulblframe,textvariable=self.var_semester,font=("arial",12,"bold"),width=17,state="readonly")
        com_semester["value"]=("Select Semester","Semester-1","Semester-2")
        com_semester.current(0)
        com_semester.grid(row=1,column=3,sticky=W,pady=10)

        #Student class infromation
        stuclass=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        stuclass.place(x=0,y=235,width=650,height=235)

        #labels entry
        #ID
        lbl_id=Label(stuclass,font=("arial",11,"bold"),text="StudentID:",bg="white")
        lbl_id.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        id_entry=ttk.Entry(stuclass,textvariable=self.var_std_id,font=("arial",11,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_name=Label(stuclass,font=("arial",11,"bold"),text="Student Name:",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(stuclass,textvariable=self.var_std_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Division
        lbl_div=Label(stuclass,font=("arial",11,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(stuclass,textvariable=self.var_div,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Roll no
        lbl_rollno=Label(stuclass,font=("arial",11,"bold"),text="Roll No:",bg="white")
        lbl_rollno.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_rollno=ttk.Entry(stuclass,textvariable=self.var_rollno,width=22,font=("arial",11,"bold"))
        txt_rollno.grid(row=1,column=3,padx=2,pady=7)

        #Gender
        lbl_gender=Label(stuclass,font=("arial",11,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(stuclass,textvariable=self.var_gender,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_gender["value"]=("Select Gender","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob=Label(stuclass,font=("arial",11,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        lbl_dob=ttk.Entry(stuclass,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        lbl_dob.grid(row=2,column=3,padx=2,pady=7)

        #Phone no
        lbl_phone=Label(stuclass,font=("arial",11,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(stuclass,textvariable=self.var_phoneno,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        #Address
        lbl_address=Label(stuclass,font=("arial",11,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(stuclass,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #Button Frame
        btn_frame=Frame(dataleftframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_save=Button(btn_frame,text="Save",command=self.add_data,font=("arial",10,"bold"),width=15,bg="red",fg="white")
        btn_save.grid(row=0,column=0,padx=10)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",10,"bold"),width=15,bg="red",fg="white")
        btn_update.grid(row=0,column=1,padx=10)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",10,"bold"),width=15,bg="red",fg="white")
        btn_delete.grid(row=0,column=2,padx=10)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",10,"bold"),width=15,bg="red",fg="white")
        btn_reset.grid(row=0,column=3,padx=10)

        #right frame 
        datarightframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        datarightframe.place(x=680,y=10,width=800,height=540)

        #rightimg
        img_6=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_6=img_6.resize((790,200),Image.Resampling.LANCZOS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        rightimg=Label(datarightframe,image=self.photoimg_6,bd=2,relief=RIDGE)
        rightimg.place(x=0,y=0,width=790,height=200)

        #search frame 
        search_frame=LabelFrame(datarightframe,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        search_frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",fg="Blue",bg="yellow")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search  
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_search["value"]=("Select Option","Roll_no","Phone_no","Student_id")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()  
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=14,bg="red",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_show_all=Button(search_frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=15,bg="red",fg="white")
        btn_show_all.grid(row=0,column=4,padx=5)

        #==========================STUDENT TABLE AND SCROLL BAR=================================
        table_frame=Frame(datarightframe,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)     
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll_no","gender","dob","phone_no","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Class Division")
        self.student_table.heading("roll_no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)


    def add_data(self):
        if(self.var_dep.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                mycon=mys.connect(host='localhost',username='root',passwd='Moonknight',database='school')
                mycursor=mycon.cursor()     
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),               
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_div.get(),
                                                                                                    self.var_rollno.get(),                                                                                                                                 
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_phoneno.get(),
                                                                                                    self.var_address.get()
                                                                                                                                     
                                                                                            ))
                mycon.commit()
                self.fetch_data()
                mycon.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)})",parent=self.root)                                                                                    
 
    #Fetch function
    def fetch_data(self):
        mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
        mycursor=mycon.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            mycon.commit()
        mycon.close()
        
    ### Get Cursor            
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]


        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_rollno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_phoneno.set(data[10])
        self.var_address.set(data[11])
        
    def update_data(self):
        if (self.var_dep.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                    mycursor=mycon.cursor()     
                    mycursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_ID=%s,Name=%s,Division=%s,Rollno=%s,Gender=%s,DOB=%s,Phoneno=%s,Address=%s where Student_ID=%s",(
                                                                                                                                                            self.var_dep.get(),               
                                                                                                                                                            self.var_course.get(),
                                                                                                                                                            self.var_year.get(),
                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                            self.var_std_id.get(),
                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                            self.var_div.get(),
                                                                                                                                                            self.var_rollno.get(),                                                                                                                                 
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                            self.var_phoneno.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_std_id.get()       
                                                                                                                                                            
                                                                                                                                                        ))
                else:
                    if not update:
                        return
                mycon.commit()
                self.fetch_data() 
                mycon.close()
                messagebox.showinfo("Success","Student successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)})",parent=self.root)
                
    #Delete            
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Del=messagebox.askyesno("Delete","Are sure delete this student",parent=self.root)
                if Del>0:
                    mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                    mycursor=mycon.cursor()
                    sql="delete from student where Student_ID=%s"
                    value=(self.var_std_id.get(),)
                    mycursor.execute(sql,value)
                else:
                    if not Del:
                        return
                mycon.commit() 
                self.fetch_data()
                mycon.close()
                messagebox.showinfo("Delete","Your Student has been Deleted")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)})",parent=self.root)
                
    #reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_phoneno.set("")
        self.var_address.set("")
        
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                mycursor=mycon.cursor()
                mycursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=mycursor.fetchall()

                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)

                    mycon.commit()
                mycon.close()    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        
       































 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  


