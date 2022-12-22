from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow in cmd 
import mysql.connector as mys


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        

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

        combo_dep=ttk.Combobox(stulblframe,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_std=Label(stulblframe,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std=ttk.Combobox(stulblframe,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        #Year
        current_year=Label(stulblframe,font=("arial",12,"bold"),text="Year:",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2)

        com_text_current_year=ttk.Combobox(stulblframe,font=("arial",12,"bold"),width=17,state="readonly")
        com_text_current_year["value"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")
        com_text_current_year.current(0)
        com_text_current_year.grid(row=1,column=1,sticky=W,padx=2)

        #Semester
        label_semester=Label(stulblframe,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        com_semester=ttk.Combobox(stulblframe,font=("arial",12,"bold"),width=17,state="readonly")
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

        id_entry=ttk.Entry(stuclass,font=("arial",11,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_name=Label(stuclass,font=("arial",11,"bold"),text="Student Name:",bg="white")
        lbl_name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(stuclass,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #Division
        lbl_div=Label(stuclass,font=("arial",11,"bold"),text="Class Division:",bg="white")
        lbl_div.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        com_txt_div=ttk.Combobox(stuclass,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_div["value"]=("Select Division","A","B","C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Roll no
        lbl_rollno=Label(stuclass,font=("arial",11,"bold"),text="Roll No:",bg="white")
        lbl_rollno.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_rollno=ttk.Entry(stuclass,width=22,font=("arial",11,"bold"))
        txt_rollno.grid(row=1,column=3,padx=2,pady=7)

        #Gender
        lbl_gender=Label(stuclass,font=("arial",11,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(stuclass,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_gender["value"]=("Select Gender","Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob=Label(stuclass,font=("arial",11,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        lbl_dob=ttk.Entry(stuclass,width=22,font=("arial",11,"bold"))
        lbl_dob.grid(row=2,column=3,padx=2,pady=7)

        #Phone no
        lbl_phone=Label(stuclass,font=("arial",11,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(stuclass,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        #Address
        lbl_address=Label(stuclass,font=("arial",11,"bold"),text="Address:",bg="white")
        lbl_address.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(stuclass,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=3,column=1,padx=2,pady=7)

        #Button Frame
        btn_frame=Frame(dataleftframe,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_save=Button(btn_frame,text="Save",font=("arial",11,"bold"),width=17,bg="grey",fg="blue")
        btn_save.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",font=("arial",11,"bold"),width=17,bg="grey",fg="blue")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),width=17,bg="grey",fg="blue")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),width=17,bg="grey",fg="blue")
        btn_reset.grid(row=0,column=3,padx=1)

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

        com_txt_search=ttk.Combobox(search_frame,font=("arial",12,"bold"),width=18,state="readonly")
        com_txt_search["value"]=("Select Option","Roll No","Phone No","Student ID")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        txt_search=ttk.Entry(search_frame,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,text="Search",font=("arial",11,"bold"),width=14,bg="grey",fg="blue")
        btn_search.grid(row=0,column=3,padx=5)

        btn_show_all=Button(search_frame,text="Show All",font=("arial",11,"bold"),width=15,bg="grey",fg="blue")
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


 
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  


