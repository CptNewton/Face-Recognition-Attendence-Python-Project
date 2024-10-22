from tkinter import* 
from PIL import Image,ImageTk

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

        title_lbl=Label(self.root,text="HELP  DESK",font=("times new roman",32,"bold"),bg="darkblue",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        back_btn2=Button(title_lbl,text="BACK",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="white",fg="black",activebackground="white")
        back_btn2.pack(side=RIGHT)

        img_top=Image.open(r"Images\call-centre-gbd2720819_1920.jpg")
        img_top=img_top.resize((1920,950),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=1920,height=750)

        dev_lbl=Label(f_lbl,text=("Email: nayanjadhikary4@gmail.com\nTelegram: @Capt_Newton"),font=25,fg="blue",bg="white")
        dev_lbl.place(x=728,y=360,width=550,height=80)

        



if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()