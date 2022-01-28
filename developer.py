from tkinter import* 
from PIL import Image,ImageTk

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",32,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        img_top=Image.open(r"Images\call-centre-gbd2720819_1920.jpg")
        img_top=img_top.resize((1920,950),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=1920,height=750)



if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()