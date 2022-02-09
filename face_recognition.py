from tkinter import* 
import cv2
import mysql.connector
from datetime import datetime
from PIL import Image,ImageTk


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")
        
        # title
        title_lbl=Label(self.root,text="FACE  RECOGNITION  PAGE",font=("times new roman",32,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        back_btn2=Button(title_lbl,text="BACK",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="red",fg="black",activebackground="red")
        back_btn2.pack(side=RIGHT)

        img_top=Image.open(r"Images\man-g300e4640d_1920.jpg")
        img_top=img_top.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=80,width=1920,height=750)

        # button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",25,"bold"),bg="yellow",fg="red",activebackground="red")
        b1_1.place(x=500,y=100,width=500,height=80)

        # ===================================== Attendence ==============================================

    def mark_attendence(self,i,r,n,d):
        with open("Attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


        # ===================================== face recognition ========================================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0.255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select StudentID from student where StudentID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select Roll_No from student where StudentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)


                my_cursor.execute("select Name from student where StudentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

               
                my_cursor.execute("select Dep from student where StudentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

               



                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),2)
                    cv2.putText(img,f"Roll_No:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),2)
                    self.mark_attendence(i,r,n,d)
            
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),2)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()