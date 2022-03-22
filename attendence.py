from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from PIL import Image,ImageTk

mydata=[]
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition Attendence System")

    # ========================================== variables ============================================

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()


        title_lbl1=Label(root,text="ATTENDENCE  MANAGEMENT  SYSTEM",font=("times new roman",28,"bold"),bg="lightblue",fg="blue")
        title_lbl1.place(x=0,y=0,width=1530,height=80)

        back_btn3=Button(title_lbl1,text="BACK",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="white",fg="red",activebackground="white")
        back_btn3.pack(side=RIGHT)

        # left label frame
        Left_frame2=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Student Attendence Information",font=("times new roman",14,"bold"),fg="red")
        Left_frame2.place(x=60,y=100,width=690,height=650)


        Left_inside_frame=LabelFrame(Left_frame2,bd=2,relief=RIDGE,bg="white")
        Left_inside_frame.place(x=2,y=200,width=682,height=400)

        left_img2=Image.open(r"images\1_XknCwHJ88MvR0RznnHP47Q.png")
        left_img2=left_img2.resize((720,210),Image.ANTIALIAS)
        self.photoimg_left2=ImageTk.PhotoImage(left_img2)

        left_lbl2=Label(Left_frame2,image=self.photoimg_left2)
        left_lbl2.place(x=0,y=0,width=720,height=195)


        # ========================================================labels and en Id================================================

        # attendence id
        attendenceID_label=Label(Left_inside_frame,text="AttendenceID:",font=("times new roman",14,"bold"),bg="white")
        attendenceID_label.grid(row=0,column=0,padx=5,pady=20,sticky=W)

        attendenceID_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",14,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        # roll no
        roll_no_label2=Label(Left_inside_frame,text="Roll No:",font=("times new roman",14,"bold"),bg="white")
        roll_no_label2.grid(row=0,column=2,padx=0,pady=20,sticky=W)

        roll_no_entry2=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",14,"bold"))
        roll_no_entry2.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        # name
        name_label2=Label(Left_inside_frame,text="Name:",font=("times new roman",14,"bold"),bg="white")
        name_label2.grid(row=1,column=0,padx=5,pady=20,sticky=W)

        name_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",14,"bold"))
        name_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)

        # department
        dep_label2=Label(Left_inside_frame,text="Department:",font=("times new roman",14,"bold"),bg="white")
        dep_label2.grid(row=1,column=2,padx=0,pady=20,sticky=W)

        dep_entry2=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",14,"bold"))
        dep_entry2.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        # time
        time_label=Label(Left_inside_frame,text="Time:",font=("times new roman",14,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=20,sticky=W)

        time_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",14,"bold"))
        time_entry.grid(row=2,column=1,padx=0,pady=5,sticky=W)

        # date
        date_label=Label(Left_inside_frame,text="Date:",font=("times new roman",14,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=0,pady=20,sticky=W)

        date_entry=ttk.Entry(Left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",14,"bold"))
        date_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        # Attendence
        attendence_label=Label(Left_inside_frame,text="Attendence:",font=("times new roman",14,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=5,pady=20,sticky=W)

        self.attend_status=ttk.Combobox(Left_inside_frame,textvariable=self.var_atten_status,font=("times new roman",14,"bold"),state="readonly")
        self.attend_status["values"]=("Status","Present","Absent")
        self.attend_status.current(0)
        self.attend_status.grid(row=3,column=1,padx=0,pady=5,sticky=W)

        # button frame
        btn_frame2=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=360,width=678,height=35)

        import_btn=Button(btn_frame2,text="Import csv",command=self.importCSV,width=15,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame2,text="Export csv",command=self.exportCSV,width=14,font=("times new roman",14,"bold"),bg="yellow",fg="black")
        export_btn.grid(row=0,column=1)

        update_btn2=Button(btn_frame2,text="Update",width=14,font=("times new roman",14,"bold"),bg="lightgreen",fg="black")
        update_btn2.grid(row=0,column=2)

        reset_btn2=Button(btn_frame2,text="Reset",command=self.reset_data,width=15,font=("times new roman",14,"bold"),bg="red",fg="black")
        reset_btn2.grid(row=0,column=3)

        

        # right label frame

        right_inside_frame=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Attendence Details",font=("times new roman",14,"bold"),fg="green")
        right_inside_frame.place(x=760,y=100,width=720,height=650)

        table_frame=Frame(right_inside_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=200,width=710,height=400)

        right_img2=Image.open(r"images\national-cancer-institute-N_aihp118p8-unsplash.jpg")
        right_img2=right_img2.resize((720,200),Image.ANTIALIAS)
        self.photoimg_right2=ImageTk.PhotoImage(right_img2)

        right_lbl2=Label(right_inside_frame,image=self.photoimg_right2)
        right_lbl2.place(x=0,y=0,width=720,height=195)

        # ======================================================== Scroll bar ==================================================================

        Scroll_x2=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y2=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=Scroll_x2.set,yscrollcommand=Scroll_y2.set)
        
        Scroll_x2.pack(side=BOTTOM,fill=X)
        Scroll_y2.pack(side=RIGHT,fill=Y)
        Scroll_x2.config(command=self.AttendenceReportTable.xview)
        Scroll_y2.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence_ID")
        self.AttendenceReportTable.heading("roll",text="Roll_No")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Department")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")

        self.AttendenceReportTable["show"]="headings"


        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=80)
        self.AttendenceReportTable.column("name",width=150)
        self.AttendenceReportTable.column("department",width=120)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)

        self.AttendenceReportTable.pack(fill=BOTH,expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)



# ================================================ fetch data =========================================================

    def fetchData(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    # =========================== import csv ================================================

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # =========================== export csv =================================================

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to "+os.path.basename(fln)+" Succesfully.")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    #============================= update csv ========================================================

    # def update(atten_id,roll,name,dept,time,date,attend):
    #     filename = 'Attendence.csv'
    #     tempfile = NamedTemporaryFile(mode='w', delete=False)

    #     fields = ['Attendence_ID', 'Name', 'Course', 'Year']

    #     with open(filename, 'r') as csvfile, tempfile:
    #         reader = csv.DictReader(csvfile, fieldnames=fields)
    #         writer = csv.DictWriter(tempfile, fieldnames=fields)
    #         for row in reader:
    #             if row['Attendence_ID'] == str(atten_id):
    #                 print('updating row', row['Attendence_ID'])
    #                 row['Roll_No'], row['Name'], row['Department'], row["Time"], row["Date"], row["Attendence"] = roll, name, dept, time, date, attend
    #             row = {'Attendence_ID': row['atten_id'], 'Roll_No': row['roll'], 'Name': row['name'], 'Department': row['dept'], 'Time': row['time'], 'Date': row['date'], 'Attendence': row["attend"]}
    #             writer.writerow(row)

    #     shutil.move(tempfile.name, filename)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']

        self.var_atten_id.set(rows[0]),
        self.var_atten_roll.set(rows[1]),
        self.var_atten_name.set(rows[2]),
        self.var_atten_dep.set(rows[3]),
        self.var_atten_time.set(rows[4]),
        self.var_atten_date.set(rows[5]),
        self.var_atten_status.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("Status")





if __name__== "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()