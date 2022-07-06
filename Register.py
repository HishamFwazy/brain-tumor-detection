from tkinter import*
import tkinter.messagebox as mymessagebox
import ast
import pyodbc
from PIL import ImageTk

class RG():

    def __init__(self):
        self.root =Tk()
        self.root.geometry('925x500+300+200')
        self.root.title("Registration Form")
        self.root.resizable(False,False)
        self.root.configure(background='white')



        img=PhotoImage(file='D:\login.png')
        Label(self.root,image=img,border=0,bg='white').place(x=470,y=90)



        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=400, height=550)
        label_0 = Label(frame, text="Register",fg="#57a1f8", font=("cambria", 35, "bold"),bg="white").place(x=110, y=30)





        #username label and text entry box
        lbl_user=Label(frame,text="Username",font=("cambria",15,"bold"),bg="white").place(x=30,y=130)
        self.username = StringVar()

        # usernameEntry = Entry(frame, textvariable=self.username,font=("times new roman",15),bg="gray100")
        # usernameEntry.place(x=30,y=170,width=350,height=35)
        def on_enter(e):
            usernameEntry.delete(0,'end')
        def on_leave(e):
            if usernameEntry.get()=='':
                usernameEntry.insert(0,'Username')
        usernameEntry = Entry(frame,fg='black',textvariable=self.username,border=0,font=("times new roman",15))
        usernameEntry.place(x=30,y=120,width=350,height=35)
        usernameEntry.insert(0,'Username')
        usernameEntry.bind("<FocusIn>",on_enter)
        usernameEntry.bind("<FocusOut>", on_leave)
        Frame(frame,width=330,height=2,bg='gray50').place(x=30,y=160)



        #password label and password entry box
        lbl_pass = Label(frame, text="", font=("cambria", 15, "bold"), bg="white").place(x=30, y=230)
        self.password = StringVar()




        # passwordEntry = Entry(frame, textvariable=self.password,  font=("times new roman", 15), bg="gray100",show='*')
        # passwordEntry.place(x=30, y=270, width=350, height=35)
        def oon_enter(e):
            passwordEntry.delete(0,'end')
        def oon_leave(e):
            if passwordEntry.get()=='':
                passwordEntry.insert(0,'Password')
        passwordEntry = Entry(frame,border=0,textvariable=self.password,  font=("times new roman", 15), bg="gray100")
        passwordEntry.place(x=30, y=200, width=350, height=35)
        passwordEntry.insert(0,'Password')
        passwordEntry.bind("<FocusIn>",oon_enter)
        passwordEntry.bind("<FocusOut>", oon_leave)
        Frame(frame,width=330,height=2,bg='gray50').place(x=30,y=240)



        #SignUP_button=Button(frame,text="Sign Up",bg="gray90",command=self.validateSignUP,font=("cambria",15,"bold")).place(x=30,y=350)


        SignUP_button=Button(frame,text="Sign Up",width=27,pady=7,bg="#57a1f8",fg='white',border=0,command=self.validateSignUP,font=("cambria",15,"bold")).place(x=30,y=300)

        Exit_button = Button(frame, text="Back", width=27, border=0, pady=7, bg="#595959", fg='white',
                             command=lambda: [self.exit(), self.Login()], font=("cambria", 15, "bold")).place(x=30,
                                                                                                              y=370)






        self.root.bind('<Return>',self.validateSignUP)

        self.root.mainloop()

    def validateSignUP(self,*event):
        if self.username.get()=="" or self.password.get()=="":
            mymessagebox.showinfo("Error","Please fill all the fields")

        else:
            try:
                conn = pyodbc.connect('Driver={SQL Server};'
                                      'Server=DESKTOP-DSFL6R9\SQLEXPRESS;'
                                      'Database=Login;'
                                      'Trusted_Connection=yes;')
                cursor=conn.cursor()
                cursor.execute("select * from Table_1 where username=? ", (self.username.get()))
                row=cursor.fetchone()

                if row != None:
                 mymessagebox.showerror("Error!", "The Username id is already exists, please try again with another one",)

                else:

                   cursor.execute("INSERT INTO Table_1 (username,password) VALUES (?,?)",
                       (self.username.get(),
                        self.password.get()
                        ))
                   cursor.commit()
                   cursor.close()
                   conn.close()

                   mymessagebox.showinfo("Success", "Sign UP Successfully")


                   self.root.destroy()
            except Exception as e:
                mymessagebox.showerror("Error!",f"Error due to {str(e)}",)

    def exit(self):
        self.root.destroy()

    def Login(self):
        import Login
        Login.Log()




#RG1=RG()


