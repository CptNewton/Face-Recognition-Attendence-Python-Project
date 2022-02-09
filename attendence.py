from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from PIL import Image,ImageTk
from matplotlib import image

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


        title_lbl=Label(root,text="ATTENDENCE  MANAGEMENT  SYSTEM",font=("times new roman",28,"bold"),bg="lightblue",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=80)

        back_btn2=Button(title_lbl,text="BACK",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="white",fg="red",activebackground="white")
        back_btn2.pack(side=RIGHT)

        # left label frame
        Left_frame=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Student Attendence Information",font=("times new roman",14,"bold"),fg="red")
        Left_frame.place(x=60,y=100,width=690,height=650)


        Left_inside_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,bg="white")
        Left_inside_frame.place(x=2,y=200,width=682,height=400)

        left_img=Image.open(r"images\1_XknCwHJ88MvR0RznnHP47Q.png")
        left_img=left_img.resize((720,210),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(left_img)

        left_lbl=Label(Left_frame,image=self.photoimg_left)
        left_lbl.place(x=0,y=0,width=720,height=195)


        # ========================================================labels and en Id================================================

        # attendence id
        attendenceID_label=Label(Left_inside_frame,text="AttendenceID:",font=("times new roman",14,"bold"),bg="white")
        attendenceID_label.grid(row=0,column=0,padx=5,pady=20,sticky=W)

        attendenceID_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",14,"bold"))
        attendenceID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)

        # roll no
        roll_no_label=Label(Left_inside_frame,text="Roll No:",font=("times new roman",14,"bold"),bg="white")
        roll_no_label.grid(row=0,column=2,padx=0,pady=20,sticky=W)

        roll_no_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",14,"bold"))
        roll_no_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        # name
        name_label=Label(Left_inside_frame,text="Name:",font=("times new roman",14,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=5,pady=20,sticky=W)

        name_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",14,"bold"))
        name_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)

        # department
        dep_label=Label(Left_inside_frame,text="Department:",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=0,pady=20,sticky=W)

        dep_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",14,"bold"))
        dep_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)

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
        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=360,width=678,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCSV,width=15,font=("times new roman",14,"bold"),bg="darkblue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCSV,width=14,font=("times new roman",14,"bold"),bg="yellow",fg="black")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",14,"bold"),bg="lightgreen",fg="black")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",14,"bold"),bg="red",fg="black")
        reset_btn.grid(row=0,column=3)

        

        # right label frame

        right_inside_frame=LabelFrame(root,bd=2,bg="white", relief=RIDGE,text="Attendence Details",font=("times new roman",14,"bold"),fg="green")
        right_inside_frame.place(x=760,y=100,width=720,height=650)

        table_frame=Frame(right_inside_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=2,y=200,width=710,height=400)

        right_img=Image.open(r"images\national-cancer-institute-N_aihp118p8-unsplash.jpg")
        right_img=right_img.resize((720,200),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(right_img)

        right_lbl=Label(right_inside_frame,image=self.photoimg_right)
        right_lbl.place(x=0,y=0,width=720,height=195)

        # ======================================================== Scroll bar ==================================================================

        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.AttendenceReportTable.xview)
        Scroll_y.config(command=self.AttendenceReportTable.yview)

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

    # def update(self):
    #     fln =["Atten_ID","Roll","name","dept","time","date","attend"]
    #     data=[] # Create temp copy of the csv file

    #     with open("Attendence.csv", "r", newline="") as file_read:
    #         csv_reader = csv.DictReader(file_read, fln=fln)
    #         header = next(csv_reader)

    #     for line in csv_reader: # Reading the CSV file and storing it in temp_list
    #         if line["Attendence_ID"] == Atten_ID and line["Roll_No"] != Roll_No:
    #             line["Roll_No"] = Atten_ID
    #             data.append(line)

    #     with open("Attendence.csv", "w", newline="") as file_write: 
    #         csv_writer = csv.DictWriter(file_write, fieldnames=fln)
    #         csv_writer.writeheader()
    #         csv_writer.writerows(data)

    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_status.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("Status")
        

        

# update function

   
        







if __name__== "__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()