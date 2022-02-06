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

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",32,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        img_top=Image.open(r"Images\digital-face-recognition-biometrical-data-taken-surveillance-camera-105135145.jpg")
        img_top=img_top.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=1920,height=750)

        b1_1=Button(f_lbl,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="lightblue",fg="blue")
        b1_1.place(x=490,y=200,width=500,height=80)

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