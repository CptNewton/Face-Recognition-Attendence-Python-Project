from time import strftime, time
from tkinter import*
from PIL import Image,ImageTk
from matplotlib.pyplot import text, title
from student import Student
import os
from tkinter import messagebox
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
from time import strftime
from developer import Developer


class Face_Recognition_Attendence_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")


        # 1st image
        img=Image.open(r"Images\gettyimages-1199766600-612x612.jpg")
        img=img.resize((550,120),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=550,height=120)

         # 2nd image
        img1=Image.open(r"Images\gettyimages-1300313012-612x612.jpg")
        img1=img1.resize((550,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=120)

        # 3rd image
        img2=Image.open(r"Images\gettyimages-1088377404-612x612.jpg")
        img2=img2.resize((550,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=120)

         # bg image
        img3=Image.open(r"Images\philipp-katzenberger-iIJrUoeRoCQ-unsplash.jpg")
        img3=img3.resize((1920,950),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1920,height=950)

        # project title
        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDENCE  SYSTEM",font=("times new roman",32,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        # =================== Time ====================

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("times new roman",16,"bold"),bg="darkblue",fg="yellow")
        lbl.place(x=0,y=0,width=150,height=50)
        time()


        # student details button
        img4=Image.open(r"Images\login.png")
        img4=img4.resize((200,150),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # detect face button
        img5=Image.open(r"Images\istockphoto-1255199117-612x612.jpg")
        img5=img5.resize((300,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        # attendence button
        img6=Image.open(r"Images\download.png")
        img6=img6.resize((300,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendence_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendence",command=self.attendence_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)

        # help button
        img7=Image.open(r"Images\need-help.jpg")
        img7=img7.resize((260,250),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_desk,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        # train data button
        img8=Image.open(r"Images\download.jfif")
        img8=img8.resize((300,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

    
        # photos button
        img9=Image.open(r"Images\images (1).jfif")
        img9=img9.resize((250,230),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

         # developer button
        img10=Image.open(r"Images\dev.png")
        img10=img10.resize((250,250),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.dev_data,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",command=self.dev_data,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)

        # exit button
        img11=Image.open(r"Images\exit-button.jpg")
        img11=img11.resize((300,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")


        # ======================================function button================================================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)


    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure to exit this project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
      



if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_Attendence_System(root)
    root.mainloop()
