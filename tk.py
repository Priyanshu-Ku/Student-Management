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
        self.var_class=StringVar()
        self.var_stream=StringVar()
        self.var_session=StringVar()
        self.var_course=StringVar()
        self.var_admno=StringVar()
        self.var_std_name=StringVar()
        self.var_sec=StringVar()
        self.var_rollno=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_bloodgp=StringVar()
        self.var_category=StringVar()
        self.var_phoneno=StringVar() 
        self.var_address=StringVar()


        #1st
        img_1=Image.open(r'Top right and left.jpeg')
        img_1=img_1.resize((490,160),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        self.btn_1=Label(self.root,image=self.photoimg_1)
        self.btn_1.place(x=0,y=0,width=490,height=160)

         #2nd
        img_2=Image.open(r'Top middle.jpeg')
        img_2=img_2.resize((490,160),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Label(self.root,image=self.photoimg_2)
        self.btn_2.place(x=490,y=0,width=490,height=160)

         #3rd
        img_3=Image.open(r'Top right and left.jpeg')
        img_3=img_3.resize((550,160),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Label(self.root,image=self.photoimg_3)
        self.btn_3.place(x=980,y=0,width=550,height=160)

        #background image
        
        background_label=Label(self.root,bd=2,relief=RIDGE,bg="white")
        background_label.place(x=0,y=160,width=1530,height=710)

        label_title=Label(background_label,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="maroon",bg="white")
        label_title.place(x=0,y=0,width=1530,height=50)

        #manage frame  
        manage_frame=Frame(background_label,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=0,y=55,width=1530,height=560)

        #left frame 
        dataleftframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="maroon",bg="white")
        dataleftframe.place(x=10,y=10,width=660,height=540)

        #leftimg
        img_5=Image.open(r'Down Left.jpeg')
        img_5=img_5.resize((650,120),Image.Resampling.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        leftimg=Label(dataleftframe,image=self.photoimg_5,bd=2,relief=RIDGE)
        leftimg.place(x=0,y=0,width=650,height=120)

        #Student Class labelframe infromation
        stulblframe=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text="Student Class Information",font=("times new roman",12,"bold"),fg="maroon",bg="white")
        stulblframe.place(x=0,y=120,width=650,height=115)

        #Labels and Combo
        #Class
        lbl_class=Label(stulblframe,text="Class:",font=("helvetica",12,"bold"),bg="white")
        lbl_class.grid(row=0,column=0,padx=2,sticky=W)    

        combo_class=ttk.Combobox(stulblframe,textvariable=self.var_class,font=("helvetica",12,"bold"),width=17,state="readonly")
        combo_class["value"]=("Select Class","XI","XII")
        combo_class.current(0)
        combo_class.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Stream
        stream_std=Label(stulblframe,font=("helvetica",12,"bold"),text="Stream:",bg="white")
        stream_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txt_stream_std=ttk.Combobox(stulblframe,textvariable=self.var_stream,font=("helvetica",12,"bold"),width=30,state="readonly")
        com_txt_stream_std["value"]=("Select Stream","Science","Commerce")
        com_txt_stream_std.current(0)
        com_txt_stream_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        #Session
        session=Label(stulblframe,font=("helvetica",12,"bold"),text="Session:",bg="white")
        session.grid(row=1,column=0,sticky=W,padx=2)

        com_text_session=ttk.Combobox(stulblframe,textvariable=self.var_session,font=("helvetica",12,"bold"),width=17,state="readonly")
        com_text_session["value"]=("Select Session","2019-20","2020-21","2021-22","2022-23","2023-24")
        com_text_session.current(0)
        com_text_session.grid(row=1,column=1,sticky=W,padx=2)
        
        #Course
        lbl_course=Label(stulblframe,font=("helvetica",12,"bold"),text="Course:",bg="white")
        lbl_course.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        com_course=ttk.Combobox(stulblframe,textvariable=self.var_course,font=("helvetica",12,"bold"),width=30,state="readonly")
        com_course["value"]=("Select Course","English + Physics + Chemistry + Maths + Computer Sc.",
                             "English + Physics + Chemistry + Maths + Biology",
                             "English + Physics + Chemistry + Maths + Hindi",
                             "English + Physics + Chemistry + Biology + Hindi",
                             "English + Hindi + Business Studies + Accountancy + Economics",
                             "English + Maths + Business Studies + Accountancy + Economics"
                             )
        com_course.current(0)
        com_course.grid(row=1,column=3,sticky=W,padx=2,pady=10)
        
        #Student Details
        stuclass=LabelFrame(dataleftframe,bd=4,relief=RIDGE,padx=2,text="Student Details",font=("times new roman",12,"bold"),fg="maroon",bg="white")
        stuclass.place(x=0,y=235,width=650,height=235)

        #labels entry
        #Adm no
        lbl_admno=Label(stuclass,font=("helvetica",11,"bold"),text="Adm No:",bg="white")
        lbl_admno.grid(row=0,column=0,sticky=W,padx=2,pady=7)

        admno_entry=ttk.Entry(stuclass,textvariable=self.var_admno,font=("helvetica",11,"bold"),width=22)
        admno_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_name=Label(stuclass,font=("helvetica",11,"bold"),text="Student Name:",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(stuclass,textvariable=self.var_std_name,width=22,font=("helvetica",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Section
        lbl_sec=Label(stuclass,font=("helvetica",11,"bold"),text="Section:",bg="white")
        lbl_sec.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_sec=ttk.Combobox(stuclass,textvariable=self.var_sec,font=("helvetica",12,"bold"),width=18,state="readonly")
        com_txt_sec["value"]=("Select Section","A","B","C")
        com_txt_sec.current(0)
        com_txt_sec.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Roll no
        lbl_rollno=Label(stuclass,font=("helvetica",11,"bold"),text="Roll No:",bg="white")
        lbl_rollno.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_rollno=ttk.Entry(stuclass,textvariable=self.var_rollno,width=22,font=("helvetica",11,"bold"))
        txt_rollno.grid(row=1,column=3,padx=2,pady=7)

        #Gender
        lbl_gender=Label(stuclass,font=("helvetica",11,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(stuclass,textvariable=self.var_gender,font=("helvetica",12,"bold"),width=18,state="readonly")
        com_txt_gender["value"]=("Select Gender","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob=Label(stuclass,font=("helvetica",11,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(stuclass,textvariable=self.var_dob,width=22,font=("helvetica",11,"bold"))
        txt_dob.grid(row=2,column=3,padx=2,pady=7)
        
        #Blood group
        lbl_bloodgp=Label(stuclass,font=("helvetica",11,"bold"),text="Blood Group:",bg="white")
        lbl_bloodgp.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_bloodgp=ttk.Entry(stuclass,textvariable=self.var_bloodgp,width=22,font=("helvetica",11,"bold"))
        txt_bloodgp.grid(row=3,column=1,padx=2,pady=7)
        
        #Category
        lbl_category=Label(stuclass,font=("helvetica",11,"bold"),text="Category:",bg="white")
        lbl_category.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        com_txt_category=ttk.Combobox(stuclass,textvariable=self.var_category,font=("helvetica",12,"bold"),width=18,state="readonly")
        com_txt_category["value"]=("Select Category","General","OBC","SC","ST")
        com_txt_category.current(0)
        com_txt_category.grid(row=3,column=3,padx=2,pady=7)

        #Phone no
        lbl_phone=Label(stuclass,font=("helvetica",11,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(stuclass,textvariable=self.var_phoneno,width=22,font=("helvetica",11,"bold"))
        txt_phone.grid(row=4,column=1,padx=2,pady=7)

        #Address
        lbl_address=Label(stuclass,font=("helvetica",11,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(stuclass,textvariable=self.var_address,width=22,font=("helvetica",11,"bold"))
        txt_address.grid(row=4,column=3,padx=2,pady=7)

        #Button Frame
        btn_frame=Frame(dataleftframe,bd=2,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_save=Button(btn_frame,text="Save",command=self.add_data,font=("helvetica",10,"bold"),width=15,bg="maroon",fg="white")
        btn_save.grid(row=0,column=0,padx=10)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("helvetica",10,"bold"),width=15,bg="maroon",fg="white")
        btn_update.grid(row=0,column=1,padx=10)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("helvetica",10,"bold"),width=15,bg="maroon",fg="white")
        btn_delete.grid(row=0,column=2,padx=10)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("helvetica",10,"bold"),width=15,bg="maroon",fg="white")
        btn_reset.grid(row=0,column=3,padx=10)

        #right frame 
        datarightframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="maroon",bg="white")
        datarightframe.place(x=680,y=10,width=800,height=540)

        #rightimg
        img_6=Image.open(r'Bottom right.jpeg')
        img_6=img_6.resize((790,200),Image.Resampling.LANCZOS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        rightimg=Label(datarightframe,image=self.photoimg_6,bd=2,relief=RIDGE)
        rightimg.place(x=0,y=0,width=790,height=200)

        #search frame 
        search_frame=LabelFrame(datarightframe,bd=4,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="maroon",bg="white")
        search_frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(search_frame,font=("helvetica",11,"bold"),text="Search By:",bg="maroon",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #search  
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("helvetica",12,"bold"),width=18,state="readonly")
        com_txt_search["value"]=("Select Option","Roll_no","Phone_no","Adm_no")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()  
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("helvetica",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text="Search",font=("helvetica",11,"bold"),width=14,bg="maroon",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_show_all=Button(search_frame,command=self.fetch_data,text="Show All",font=("helvetica",11,"bold"),width=15,bg="maroon",fg="white")
        btn_show_all.grid(row=0,column=4,padx=5)

        #==========================STUDENT TABLE AND SCROLL BAR=================================
        table_frame=Frame(datarightframe,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)     
        self.student_table=ttk.Treeview(table_frame,column=("class","stream","session","course","adm_no","name","section","roll_no","gender","dob","blood_group","category","phone_no","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("class",text="Class")
        self.student_table.heading("stream",text="Stream")
        self.student_table.heading("session",text="Session")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("adm_no",text="Adm No")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("roll_no",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("blood_group",text="Blood Group")
        self.student_table.heading("category",text="Category")
        self.student_table.heading("phone_no",text="Phone No")
        self.student_table.heading("address",text="Address")

        self.student_table["show"]="headings"

        self.student_table.column("class",width=100)
        self.student_table.column("stream",width=100)
        self.student_table.column("session",width=100)
        self.student_table.column("course",width=350)
        self.student_table.column("adm_no",width=100)
        self.student_table.column("name",width=200)
        self.student_table.column("section",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("blood_group",width=100)
        self.student_table.column("category",width=100)
        self.student_table.column("phone_no",width=100)
        self.student_table.column("address",width=350)

        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.student_table.bind("<ButtonRelease>",self.get_cursor)


    def add_data(self):
        if(self.var_class.get()=="" or self.var_admno.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                mycon=mys.connect(host='localhost',username='root',passwd='Moonknight',database='school')
                mycursor=mycon.cursor()     
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                           self.var_class.get(),               
                                                                                                           self.var_stream.get(),
                                                                                                           self.var_session.get(),
                                                                                                           self.var_course.get(),
                                                                                                           self.var_admno.get(),
                                                                                                           self.var_std_name.get(),
                                                                                                           self.var_sec.get(),
                                                                                                           self.var_rollno.get(),                                                                                                                                 
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_bloodgp.get(),
                                                                                                           self.var_category.get(),
                                                                                                           self.var_phoneno.get(),
                                                                                                           self.var_address.get()
                                                                                                        
                                                                                                   ))
                mycon.commit()
                self.fetch_data()
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
        
    #Get Cursor            
    def get_cursor(self,event=""):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        data=content["values"]

        self.var_class.set(data[0])
        self.var_stream.set(data[1])
        self.var_session.set(data[2])
        self.var_course.set(data[3])
        self.var_admno.set(data[4])
        self.var_std_name.set(data[5])
        self.var_sec.set(data[6])
        self.var_rollno.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_bloodgp.set(data[10])
        self.var_category.set(data[11])
        self.var_phoneno.set(data[12])
        self.var_address.set(data[13])
        
    def update_data(self):
        if (self.var_class.get()=="" or self.var_admno.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                    mycursor=mycon.cursor()     
                    mycursor.execute("update student set Class=%s,Stream=%s,Session=%s,Course=%s,Adm_no=%s,Name=%s,Section=%s,Roll_no=%s,Gender=%s,DOB=%s,Blood_Group=%s,Category=%s,Phone_no=%s,Address=%s where Adm_no=%s",(
                                                                                                                                                            self.var_class.get(),               
                                                                                                                                                            self.var_stream.get(),
                                                                                                                                                            self.var_session.get(),
                                                                                                                                                            self.var_course.get(),
                                                                                                                                                            self.var_admno.get(),
                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                            self.var_rollno.get(),                                                                                                                                 
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                            self.var_bloodgp.get(),
                                                                                                                                                            self.var_category.get(),
                                                                                                                                                            self.var_phoneno.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_admno.get()       
                                                                                                                                                            
                                                                                                                                                        ))
                else:
                    if not update:
                        return
                mycon.commit()
                self.fetch_data() 
                messagebox.showinfo("Success","Student successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)})",parent=self.root)
                
    #Delete            
    def delete_data(self):
        if self.var_admno.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Del=messagebox.askyesno("Delete","Are sure delete this student",parent=self.root)
                if Del>0:
                    mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                    mycursor=mycon.cursor()
                    sql="delete from student where Adm_no=%s"
                    value=(self.var_admno.get(),)
                    mycursor.execute(sql,value)
                else:
                    if not Del:
                        return
                mycon.commit() 
                self.fetch_data()
                messagebox.showinfo("Delete","Your Student has been Deleted")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)})",parent=self.root)
                
    #reset
    def reset_data(self):
        self.var_class.set("Select Class")
        self.var_stream.set("Select Stream")
        self.var_session.set("Select Session")
        self.var_course.set("Select Course")
        self.var_admno.set("")
        self.var_std_name.set("")
        self.var_sec.set("Select Section")
        self.var_rollno.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_bloodgp.set("")
        self.var_category.set("Select Category")
        self.var_phoneno.set("")
        self.var_address.set("")
        
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please fill the details")
        else:
            try:
                mycon=mys.connect(host='localhost',username='root',password='Moonknight',database='school')
                mycursor=mycon.cursor()
                mycursor.execute("select * from student where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=mycursor.fetchall()
                
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                else:
                    if data!=self.student_table:
                        messagebox.showerror("Error","Student not found")
                mycon.commit()   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  


