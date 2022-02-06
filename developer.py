from tkinter import* 
from PIL import Image,ImageTk

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

        # bg image
        img_top=Image.open(r"Images\jefferson-santos-9SoCnyQmkzI-unsplash.jpg")
        img_top=img_top.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1920,height=950)

        # title
        title_lbl=Label(f_lbl,text="DEVELOPERS",font=("times new roman",32,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=85)


        # frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=1010,y=120,width=700,height=600)

        # image 1
        img_top1=Image.open(r"Images\PXL_20211221_054835324~3.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img_top1)

        f_lbl1=Label(main_frame,image=self.photoimg1)
        f_lbl1.place(x=10,y=50,width=200,height=200)

        # developer 1 info
        dev_lbl=Label(main_frame,text="Nayan Jyoti Adhikary\n\nStudent of B.Sc IT\n\nScience College,Kokrajhar",font=("times new roman",18,"bold"),bg="black",fg="lightgreen")
        dev_lbl.place(x=220,y=80)

        #image 2
        img_top2=Image.open(r"Images\IMG-20200110-WA0088__01.jpg")
        img_top2=img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img_top2)

        f_lbl2=Label(main_frame,image=self.photoimg2)
        f_lbl2.place(x=10,y=330,width=200,height=200)

        # developer 2 info
        dev_lbl=Label(main_frame,text="Mitali Barman\n\nStudent of B.Sc IT\n\nScience College,Kokrajhar",font=("times new roman",18,"bold"),bg="black",fg="lightpink")
        dev_lbl.place(x=220,y=350)


        title_lbl2=Label(f_lbl,bg="black")
        title_lbl2.place(x=0,y=750,width=1530,height=85)



if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()