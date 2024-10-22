from tkinter import* 
from PIL import Image
import os
import numpy as np
import cv2
from tkinter import messagebox
from PIL import Image,ImageTk


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

        title_lbl4=Label(self.root,text="TRAIN  DATA  SET",font=("times new roman",32,"bold"),bg="black",fg="lightgreen")
        title_lbl4.place(x=0,y=0,width=1530,height=80)

        back_btn2=Button(title_lbl4,text="BACK",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="white",fg="black",activebackground="white")
        back_btn2.pack(side=RIGHT)

        img_top=Image.open(r"Images\markus-spiske-iar-afB0QQw-unsplash.jpg")
        img_top=img_top.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl4=Label(self.root,image=self.photoimg)
        f_lbl4.place(x=0,y=80,width=1920,height=750)

        b1_4=Button(f_lbl4,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="lightgreen",fg="black")
        b1_4.place(x=520,y=200,width=500,height=80)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    # ========================================== train classifier and save ============================================

        
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")





if __name__== "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()