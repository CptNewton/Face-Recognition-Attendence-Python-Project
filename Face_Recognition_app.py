from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_Attendence_System

def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1920x1080+0+0")
        self.root.wm_iconbitmap("face.ico")



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
        img3=Image.open(r"Images\damian-zalesk.jpg")
        img3=img3.resize((1920,950),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=120,width=1920,height=950)

        # project title
        title_lbl=Label(bg_img,text="ADMIN  LOGIN  PAGE",font=("times new roman",32,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        back_btn=Button(title_lbl,text="EXIT",command=self.iExit,font=("arial",12,"bold"),width=17,bg="red",fg="black")
        back_btn.pack(side=RIGHT)

        # login frame
        frame=Frame(bg_img,bg="white")
        frame.place(x=590,y=62,width=340,height=450)

        img7=Image.open(r"C:\Users\Mitali Barman\OneDrive\Desktop\Python Project\Images\images (6).jfif")
        img7=img7.resize((150,80),Image.ANTIALIAS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        lbl_img7=Label(frame,image=self.photoimage7,bg="white")
        lbl_img7.place(x=92,y=10,width=150,height=75)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=100,y=80)

        # label 
        username=Label(frame,text="Username:",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=70,y=155)

        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=70,y=225)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"))
        txtpass.place(x=40,y=250,width=270)

        # ======================================= icon images ===================================================
        img2=Image.open(r"C:\Users\Mitali Barman\OneDrive\Desktop\Python Project\Images\images (2).png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(frame,image=self.photoimage2,bg="black",borderwidth=0)
        lbl_img2.place(x=45,y=155,width=25,height=25)

        img3=Image.open(r"C:\Users\Mitali Barman\OneDrive\Desktop\Python Project\Images\images (1).jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(frame,image=self.photoimage3,bg="black",borderwidth=0)
        lbl_img3.place(x=45,y=225,width=25,height=25)

        # ===================================================button==============================================

        # login button
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="black",bg="yellow",activeforeground="black",activebackground="yellow")
        login_btn.place(x=125,y=300,width=100,height=35)

        # registere button
        register_btn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        register_btn.place(x=16,y=350,width=160)

        # forgot password button
        forgot_btn=Button(frame,text="Forgot Password",command=self.forgot_pswd_window,font=("times new roman",10),borderwidth=0,relief=RIDGE,fg="black",bg="white",activeforeground="black",activebackground="white")
        forgot_btn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window1=Toplevel(self.root)
        self.app=Register(self.new_window1)



# ===================================================== login class =================================================================

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Admin only")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_Attendence_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()

    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")

     # =============================================== reset password ====================================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="Select" or self.txt_security.get()=="" or self.txt_new_pswd.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the correct security answer",parent=self.root2)
                else:
                    query=("update register set Password=%s where Email=%s")
                    value=(self.txt_new_pswd.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your password has been reset successfully",parent=self.root2)
                    self.root2.destroy()
                    self.txtuser.focus()

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root2)
    

    # ================================================ forget password window =============================================

    def forgot_pswd_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter email to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")


                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)

                self.security_Q=Label(self.root2,text="Select Security Questions:",font=("times new roman",15,"bold"),fg="black",bg="white")
                self.security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your birth place","Your childhood nick name","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="white")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.txt_security.place(x=50,y=180,width=250)


                new_pswd=Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
                new_pswd.place(x=50,y=220)

                self.txt_new_pswd=ttk.Entry(self.root2,font=("times new roman",16,"bold"))
                self.txt_new_pswd.place(x=50,y=250,width=250)

                # reset button
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="black",bg="green")
                btn.place(x=145,y=300)


    def iExit(self):
        self.iExit=messagebox.askyesno("Login System","Are you sure to exit this project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
    
   
#===================================================== register class ================================================================        

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1920x1080+0+0")



        
        title_lbl=Label(root,text="ADMIN  REGISTER  PAGE",font=("times new roman",32,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=60)

        back_btn2=Button(title_lbl,text="EXIT",command=self.root.destroy,font=("arial",12,"bold"),width=17,bg="white",fg="red")
        back_btn2.pack(side=RIGHT)

        # ================================ variables ===================================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


         # bg image
        img=Image.open(r"Images\1159285.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=60,width=1920,height=1080)

         # left image
        img1=Image.open(r"Images\andras-vas-Bd7gNnWJBkU-unsplash.jpg")
        img1=img1.resize((550,550),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        left_img=Label(root,image=self.photoimg1)
        left_img.place(x=150,y=110,width=470,height=550)

        # ================================= main frame ===============================================
        frame=Frame(self.root,bg="white")
        frame.place(x=620,y=110,width=670,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=210,y=20)

        # ============================================== label and entry =================================================

        # -------------------- row 1
        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="white")
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        # --------------------- row 2
        contact=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",16,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email_lbl=Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="white")
        email_lbl.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        # ---------------------- row 3
        security_Q=Label(frame,text="Select Security Questions:",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","Your childhood nick name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",16,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        # ---------------------- row 4
        passwd=Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        passwd.place(x=50,y=310)

        self.txt_passwd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",16,"bold"))
        self.txt_passwd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #======check button =====================================================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I agree to the Terms & Conditions",font=("times new roman",12),fg="black",bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        # ========= buttons =====================================================
        img=Image.open(r"C:\Users\Mitali Barman\OneDrive\Desktop\Python Project\Images\images (8).jfif")
        img=img.resize((200,60),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",activebackground="white")
        b1.place(x=50,y=420,width=200)


        img1=Image.open(r"C:\Users\Mitali Barman\OneDrive\Desktop\Python Project\Images\login (1).jfif")
        img1=img1.resize((200,48),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white",activebackground="white")
        b2.place(x=350,y=422,width=200)


        # ========================================== function declare ========================================================


    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same !!")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where Email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                     
                                                                                     ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration Successfull")


    def return_login(self):
        self.root.destroy()


if __name__== "__main__":
    main()
    