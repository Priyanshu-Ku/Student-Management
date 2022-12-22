from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow in cmd 
import mysql.connector as mys


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        

        #1st
        img_1=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_1=img_1.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        self.btn_1=Button(self.root,image=self.photoimg_1,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=500,height=160)

         #2nd
        img_2=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_2=img_2.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=500,height=160)

         #3rd
        img_3=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_3=img_3.resize((500,160),Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1080,y=0,width=500,height=160)

        #background image
        img_4=Image.open("C:\\Users\\Priyanshu\\Desktop\\BOARDS\\Investigatory projects\\CS\\college_images\\student.jpg")
        img_4=img_4.resize((1920,710),Image.Resampling.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        background_label=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        background_label.place(x=0,y=160,width=1920,height=710)

        label_title=Label(background_label,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="blue",bg="white")
        label_title.place(x=-100,y=0,width=1920,height=50)

        #manage frame  
        manage_frame=Frame(background_label,bd=2,relief=RIDGE,bg="white")
        manage_frame.place(x=15,y=55,width=1900,height=560)

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
        lbl_dep=Label(stulblframe,text="Department:",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)    

        combo_dep=ttk.Combobox(stulblframe,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer","IT","Civil")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_std=Label(stulblframe,font=("arial",12,"bold"),text="Courses:",bg="white")
        course_std.grid(row=0,column=2,sticky=W,padx=2,pady=10)
        
        com_txtcourse_std=ttk.Combobox(stulblframe,state="readonly",font=("arial",12,"bold"),width=17)
        com_txtcourse_std["value"]=("Select Course","FE","SE","TE","BE")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,sticky=W,padx=2,pady=10)
        
        #year
        current_year=Label(stulblframe,font=("arial",12,"bold"),text="Year:",bg="white")
        current_year.grid(row=1,column=0,sticky=W,padx=2)

        com_text_current_year=ttk.Combobox(stulblframe,state="readonly",font=("arial",12,"bold"),width=17)
        com_text_current_year["value"]=("Select Year","2019-2020","2020-2021","2021-2022","2022-2023")
        com_text_current_year.current(0)
        com_text_current_year.grid(row=1,column=1,sticky=W,padx=2)

        #semester
        label_semester=Label(stulblframe,font=("arial",12,"bold"),text="Semester:",bg="white")
        label_semester.grid(row=1,column=2,sticky=W,padx=2,pady=10)

        com_semester=ttk.Combobox(stulblframe,state="readonly",font=("arial",12,"bold"),width=17)
        com_semester["value"]=("Select Semester","Semester-1","Semester-2")
        com_semester.current(0)
        com_semester.grid(row=1,column=3,sticky=W,pady=10)




        #right frame 
        datarightframe=LabelFrame(manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        datarightframe.place(x=680,y=10,width=820,height=540)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()  


