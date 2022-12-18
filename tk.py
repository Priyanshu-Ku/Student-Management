from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow in cmd 

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
        manage_frame.place(x=15,y=55,width=1500,height=560)














if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()


