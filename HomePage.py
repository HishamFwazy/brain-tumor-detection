from tkinter import *
import NewDetection
import webbrowser

from PIL import ImageTk
import tkinter.messagebox as mymessagebox

class HP():
    def __init__(self):
        # window
        newWindow = Tk()
        newWindow.geometry('1250x550')
        newWindow.resizable(False, False)
        newWindow.iconbitmap(r'D:\2NAAAAAA\gradution project\images\icons8-homepage-64.png')
        newWindow.title('Home Page')
        newWindow.configure(background='white')

        # Frame

        Frame_hp = Frame(newWindow,bg="#151C47")
        Frame_hp.place(x=20, y=20, height=500, width=1200)



        bg = ImageTk.PhotoImage(file=r"D:\2NAAAAAA\gradution project\images\Brain_Tumor_Classifier-logos.jpeg")
        bg_image = Label(Frame_hp, image=bg, border=0).place(x=-160, y=-500)


        # Text Label
        my_font = ('Lora-Regular', 13, 'bold')
        text = "\tTumors can grow from the brain tissue itself (primary),or cancer from elsewhere in the body can spread to the brain(metastasis).\n" \
               " \t\tTreatment options vary depending on the tumor type, size and location."

        label1 = Label(Frame_hp ,text="A brain tumor is an abnormal growth of cells inside the brain or skull",
                       font=('cambria', 25, 'bold'),bg="#151C47",fg="white",compound="center",
                       anchor="nw")
        label1.place(x=70, y=200)


        label2 = Label(Frame_hp, text=text, font=my_font,background="white",fg="white",border=1 ,bg="#151C47",justify=LEFT )
        label2.place(x=10, y=270)

        moreinfo = Label(Frame_hp, text='For more information', font=('cambria', 14, 'bold'),  fg="white",bg="#151C47")
        moreinfo.place(x=400, y=320)

        # Define a callback function
        def callback(url):
            webbrowser.open_new_tab(url)

        # Create a Label to display the link
        link = Label(Frame_hp, text="(www.Wikipedia.com)", font=('cambria', 14, 'bold'),  fg="blue",cursor="hand2",bg="#151C47")
        link.pack()
        link.bind("<Button-1>", lambda e:
        callback("https://en.wikipedia.org/wiki/Brain_tumor"))
        link.place(x=595, y=320)

        # menubar
        menubar = Menu(newWindow)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        # helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        newWindow.config(menu=menubar)

        # buttons
        N = NewDetection.ND

        ndetection_button = Button(Frame_hp, text="Click to Detect", width=27,height=2, border=0,
                                   command=lambda: [newWindow.destroy(), N()], bg="#282828", cursor="hand2",
                                   fg='#33A1C9', font=("cambria", 17, "bold"))
        ndetection_button.place(x=400, y=400)
        # newWindow.destroy()
        newWindow.mainloop()

    def exit(self):
        exit()
    def donothing(self):
        mymessagebox.showinfo("About","Brain Tumor Detection Application\n\t2022")
#HP1=HP()