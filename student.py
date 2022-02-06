from optparse import Values
from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector
import cv2 

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

        # ======================================== variables ================================================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()



        # project title
        title_lbl=Label(root,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",32,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        # left label frame
        Left_frame=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"),fg="red")
        Left_frame.place(x=60,y=100,width=690,height=650)

        # current course info
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"),fg="blue")
        current_course_frame.place(x=7,y=130,width=670,height=150)

        # department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("times new roman",14,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Physics","Chemistry","Mathematics","Botani","Zoology","BPT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",14,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman",14,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BSc","MSc","General")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=1,pady=10,sticky=W)

        # year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",14,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman",14,"bold"),state="readonly")
        year_combo["values"]=("Select year","2019-20","2020-21","2021-22")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=1,pady=10,sticky=W)

        # semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",14,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman",14,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=1,pady=10,sticky=W)

        # class student info
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",14,"bold"),fg="blue")
        class_student_frame.place(x=7,y=300,width=670,height=316)

        # student Id
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",14,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",14,"bold"))
        studentID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        # student name
        studentName_label=Label(class_student_frame,text="Name:",font=("times new roman",14,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=15,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=22,font=("times new roman",14,"bold"))
        studentName_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        # student roll no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",14,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=5,sticky=W)

        roll_no_label=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",14,"bold"))
        roll_no_label.grid(row=1,column=1,padx=0,pady=5,sticky=W)

        # gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",14,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=15,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender, font=("times new roman",14,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=1,pady=10,sticky=W)
        


        # date of birth
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",14,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        dob_label=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",14,"bold"))
        dob_label.grid(row=2,column=1,padx=0,pady=5,sticky=W)

        # email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",14,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=15,pady=5,sticky=W)

        email_label=ttk.Entry(class_student_frame,textvariable=self.var_email,width=22,font=("times new roman",14,"bold"))
        email_label.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        # phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",14,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        phone_label=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",14,"bold"))
        phone_label.grid(row=3,column=1,padx=0,pady=5,sticky=W)

        # address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",14,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=15,pady=5,sticky=W)

        address_label=ttk.Entry(class_student_frame,textvariable=self.var_address,width=22,font=("times new roman",14,"bold"))
        address_label.grid(row=3,column=3,padx=0,pady=5,sticky=W)



        # radio button
        self.var_radio1=StringVar()
        radio_bt_1=ttk.Radiobutton(class_student_frame,text="Take photo sample",variable=self.var_radio1,value="Yes")
        radio_bt_1.grid(row=15,column=1)

        radio_bt_2=ttk.Radiobutton(class_student_frame,text="No photo sample",variable=self.var_radio1,value="No")
        radio_bt_2.grid(row=15,column=2)

        # button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=180,width=656,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",14,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=14,font=("times new roman",14,"bold"),bg="yellow",fg="black")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",14,"bold"),bg="red",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=14,font=("times new roman",14,"bold"),bg="darkred",fg="white")
        reset_btn.grid(row=0,column=3)

        # button frame 2
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=215,width=656,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=29,font=("times new roman",14,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=29,font=("times new roman",14,"bold"),bg="navyblue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        # right label frame

        right_frame=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Student Detilas",font=("times new roman",14,"bold"),fg="green")
        right_frame.place(x=760,y=100,width=720,height=650)


        # =======================================================search system====================================================
        
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",14,"bold"),fg="blue")
        search_frame.place(x=7,y=130,width=702,height=70)

        search=Label(search_frame,text="Search By:",font=("times new roman",14,"bold"),bg="white",fg="red")
        search.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        # search

        self.var_combo_seach=StringVar()

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_combo_seach,font=("times new roman",14,"bold"),state="readonly",width=12)
        search_combo["values"]=("Select","Roll_No","Phone_No","email_ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=1,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=18,font=("times new roman",14,"bold"))
        search_entry.grid(row=0,column=2,padx=4,pady=5,sticky=W)


        search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",12,"bold"),bg="darkblue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=3)

        # ====================================================table frame=======================================================

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=7,y=210,width=702,height=405)

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","roll","gender","dob","email","phone","address","photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.student_table.xview)
        Scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text='Department')
        self.student_table.heading("course",text='Course')
        self.student_table.heading("year",text='Year')
        self.student_table.heading("sem",text='Semester')
        self.student_table.heading("id",text='StudentID')
        self.student_table.heading("name",text='Name')
        self.student_table.heading("roll",text='Roll_No')
        self.student_table.heading("gender",text='Gender')
        self.student_table.heading("dob",text='DOB')
        self.student_table.heading("email",text='Email')
        self.student_table.heading("phone",text='Phone')
        self.student_table.heading("address",text='Address')
        self.student_table.heading("photo",text='PhotoSample')
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=150)
        self.student_table.column("course",width=150)
        self.student_table.column("year",width=150)
        self.student_table.column("sem",width=150)
        self.student_table.column("id",width=150)
        self.student_table.column("name",width=150)
        self.student_table.column("roll",width=150)
        self.student_table.column("gender",width=150)
        self.student_table.column("dob",width=150)
        self.student_table.column("email",width=150)
        self.student_table.column("phone",width=150)
        self.student_table.column("address",width=150)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # ===========================================function declaration===================================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_id.get(),
                                                                                                        self.var_name.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_radio1.get()
                                                                                                        
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # ==================================== fetch data =======================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()        

    # ==================================== get cursor ===========================================

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12]),

    # update function

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()  
                    my_cursor.execute("update student set  Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where StudentID=%s",(                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                              
                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),                                                                                                                                               
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_id.get()
                                                                                                                                                        
                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details update successfully completed!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # delete function 

    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    
    # Reset function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    # Search data Function

    def search_data(self):
        if self.var_combo_seach.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_combo_seach.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # =============================== generate data set or take photo sample =======================================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set  Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where StudentID=%s",(                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                              
                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),                                                                                                                                               
                                                                                                                                                        self.var_name.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_address.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_id.get()==id+1
                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==================================== load predefined data on face frontals from opencv =======================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scanning factor=1.3
                    # Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)                                                                                                                                                                                                                                      
                                                                                        



if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()