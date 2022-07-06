from tkinter import *
from tkinter import filedialog
import PIL.Image
import PIL.Image
from PIL import ImageTk


class ND():
    def ImageProcessing(self):

        f_types = [('ALL Files ', '*.*'), ('Jpg Files', '*.jpg'), ('PNG Files', '*.png'),
                   ('JFIF Files', '*.jfif')]  # type of files to select
        filename = filedialog.askopenfilename(filetypes=f_types)
        self.path = filename
        print(self.path)
        img = PIL.Image.open(self.path)
        resized_image = img.resize((300, 420), PIL.Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resized_image)

        self.label.configure(image=img)
        self.label.image = img

    '''
        for f in filename:

            img = PIL.Image.open(f)  # read the image file
            img = img.resize((300, 300))  # new width & height
            img = ImageTk.PhotoImage(img)
            e1 = Label()
            e1.grid(row=row, column=col)
            e1.image = img
            e1['image'] = img  # garbage collection
            #if (col == 3):  # start new line after third column
                #row = row + 1  # start wtih next row
                #col = 1  # start with first column
            #else:  # within the same row
               # col = col + 1  # increase to next column

            originalImage = cv2.imread(f)

            # Convert the image to grayscale, and blur it slightly
            grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
            grayImage = cv2.GaussianBlur(grayImage, (5, 5), 0)

            # Convert to black and white
            (thresh, blackAndWhiteImage) = cv2.threshold(originalImage, 127, 255, cv2.THRESH_BINARY)

            # Threshold the image, then perform a series of erosions +
            # dilations to remove any small regions of noise
            thresh = cv2.threshold(grayImage, 45, 255, cv2.THRESH_BINARY)[1]
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=2)

            # Find contours in thresholded image, then grab the largest one
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            c = max(cnts, key=cv2.contourArea)

            # Find the extreme points
            extLeft = tuple(c[c[:, :, 0].argmin()][0])
            extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            extBot = tuple(c[c[:, :, 1].argmax()][0])

            # crop new image out of the original image using the four extreme points (left, right, top, bottom)
            new_image = blackAndWhiteImage[extTop[1]:extBot[1], extLeft[0]:extRight[0]]

            #Output Image
            cv2.imshow('Original image', originalImage)
            # cv2.imshow('Black&White image', blackAndWhiteImage)
            # cv2.imshow('Cropped image', new_image)

    '''

    def __init__(self):

        # window
        self.newWindow = Tk()
        self.newWindow.geometry('1100x680')  # 310x100+200+50
        self.newWindow.resizable(False, False)

        self.newWindow.iconbitmap(
            r'D:\2NAAAAAA\gradution project\images/media_istockphoto_com-brain-cancer-malignant-tumor-oncology-line-icon-vector-id1141445213.ico')
        # newWindow.iconbitmap(r'E:\SSD\Uni\Graduation Project\GUI\icons8-homepage-64.ico')
        self.newWindow.title('Tumor Detection')
        self.newWindow.configure(background='black')
        my_font1 = ('cambria', 18, 'bold')

        bg = ImageTk.PhotoImage(
            file=r"""D:\2NAAAAAA\gradution project\images/1fe2c7_5e8b033ede7f4c3eb3187b2b0dd12ddb_mv2.gif""")
        bg_image = Label(self.newWindow, image=bg, border=0).place(x=200, y=0)

        U_b1 = Button(self.newWindow, text='Upload Image to Detect', font=my_font1, height=3, width=22,
                      fg='#33A1C9', bg="#282828", cursor="hand2",
                      command=lambda: [self.ImageProcessing(), self.Detection()])
        U_b1.grid(row=200, column=5, columnspan=4)
        U_b1.place(x=570, y=550)

        self.frame = Frame(self.newWindow, width=600, height=400, bg="gray90")
        self.frame.place(x=70, y=50)

        # Create a Label Widget to display the text or Image
        self.label = Label(self.frame)
        self.label.place(x=0, y=400)
        self.label.pack()

        self.frame2 = Frame(self.newWindow, width=200, height=100, bg="gray90")
        self.frame2.place(x=120, y=490)

        self.label2 = Label(self.frame2, text="", font=my_font1, bg="black", fg="white")
        self.label2.place(x=0, y=0)
        self.label2.pack()

        self.frame3 = Frame(self.newWindow, width=200, height=100, bg="gray90")
        self.frame3.place(x=60, y=530)

        self.label3 = Label(self.frame3, text="", font=my_font1, bg="black", fg="white")
        self.label3.place(x=0, y=0)
        self.label3.pack()
        self.newWindow.mainloop()

    def Detection(self):
        import os

        import numpy as np
        from keras.models import load_model
        from keras.preprocessing import image

        best_model = load_model(filepath=r'D:\2NAAAAAA\gradution project\effiecientNET/cnn-parameters-improvement-05-1.00.model')

        import pandas as pd
        df = pd.read_csv(r"D:\New folder/submission.csv")
        path1 = self.path
        img = image.load_img(os.path.join(path1), target_size=(224, 224))
        # crop_brain_contour(img)
        img = np.asarray(img)
        img = np.expand_dims(img, axis=0)
        output = best_model.predict(img)
        if output[0][0] > output[0][1]:
            print("no")
            f = output[0][0] * 100
            self.label2.configure(text="No Tumor Detected", font='cambria', fg='white')
            self.label3.configure(text="Probability of Tumor: " + str(f), font='cambria')
        else:
            print('yes')
            f = output[0][1] * 100
            self.label2.configure(text="Tumor Detected", fg="red", font='cambria', anchor="nw")
            self.label3.configure(text="Probability of Tumor: " + str(f), font='cambria')
# ND1=ND()







# from tkinter import *
#
# from tkinter import filedialog
# import PIL.Image
# import PIL.Image
#
# from PIL import ImageTk
#
#
# class ND():
#     def ImageProcessing(self):
#
#         f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]  # type of files to select
#         filename = filedialog.askopenfilename(filetypes=f_types)
#         self.path = filename
#         print(self.path)
#         img = PIL.Image.open(self.path)
#         resized_image = img.resize((300, 420), PIL.Image.ANTIALIAS)
#         img = ImageTk.PhotoImage(resized_image)
#
#         self.label.configure(image=img)
#         self.label.image = img
#
#     '''
#         for f in filename:
#             img = PIL.Image.open(f)  # read the image file
#             img = img.resize((300, 300))  # new width & height
#             img = ImageTk.PhotoImage(img)
#             e1 = Label()
#             e1.grid(row=row, column=col)
#             e1.image = img
#             e1['image'] = img  # garbage collection
#             #if (col == 3):  # start new line after third column
#                 #row = row + 1  # start wtih next row
#                 #col = 1  # start with first column
#             #else:  # within the same row
#                # col = col + 1  # increase to next column
#
#             originalImage = cv2.imread(f)
#             # Convert the image to grayscale, and blur it slightly
#             grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#             grayImage = cv2.GaussianBlur(grayImage, (5, 5), 0)
#             # Convert to black and white
#             (thresh, blackAndWhiteImage) = cv2.threshold(originalImage, 127, 255, cv2.THRESH_BINARY)
#             # Threshold the image, then perform a series of erosions +
#             # dilations to remove any small regions of noise
#             thresh = cv2.threshold(grayImage, 45, 255, cv2.THRESH_BINARY)[1]
#             thresh = cv2.erode(thresh, None, iterations=2)
#             thresh = cv2.dilate(thresh, None, iterations=2)
#             # Find contours in thresholded image, then grab the largest one
#             cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#             cnts = imutils.grab_contours(cnts)
#             c = max(cnts, key=cv2.contourArea)
#             # Find the extreme points
#             extLeft = tuple(c[c[:, :, 0].argmin()][0])
#             extRight = tuple(c[c[:, :, 0].argmax()][0])
#             extTop = tuple(c[c[:, :, 1].argmin()][0])
#             extBot = tuple(c[c[:, :, 1].argmax()][0])
#             # crop new image out of the original image using the four extreme points (left, right, top, bottom)
#             new_image = blackAndWhiteImage[extTop[1]:extBot[1], extLeft[0]:extRight[0]]
#             #Output Image
#             cv2.imshow('Original image', originalImage)
#             # cv2.imshow('Black&White image', blackAndWhiteImage)
#             # cv2.imshow('Cropped image', new_image)
#     '''
#
#     def __init__(self):
#
#         # window
#         self.newWindow = Tk()
#         self.newWindow.geometry('1100x680')  # 310x100+200+50
#         self.newWindow.resizable(False, False)
#
#         self.newWindow.iconbitmap(
#             r'D:\2NAAAAAA\gradution project\images/media_istockphoto_com-brain-cancer-malignant-tumor-oncology-line-icon-vector-id1141445213.ico')
#         # newWindow.iconbitmap(r'E:\SSD\Uni\Graduation Project\GUI\icons8-homepage-64.ico')
#         self.newWindow.title('Tumor Detection')
#         self.newWindow.configure(background='black')
#         my_font1 = ('cambria', 18, 'bold')
#
#         bg = ImageTk.PhotoImage(
#             file=r"""D:\2NAAAAAA\gradution project\images/1fe2c7_5e8b033ede7f4c3eb3187b2b0dd12ddb_mv2.gif""")
#         bg_image = Label(self.newWindow, image=bg, border=0).place(x=200, y=0)
#
#         U_b1 = Button(self.newWindow, text='Upload Image to Detect', font=my_font1, height=3, width=22,
#                       fg='#33A1C9', bg="#282828", cursor="hand2",
#                       command=lambda: [self.ImageProcessing(), self.Detection()])
#         U_b1.grid(row=200, column=5, columnspan=4)
#         U_b1.place(x=570, y=550)
#
#         self.frame = Frame(self.newWindow, width=600, height=400, bg="gray90")
#         self.frame.place(x=70, y=50)
#         self.frame3 = Frame(self.newWindow, width=200, height=100, bg="gray90")
#         self.frame3.place(x=60, y=530)
#
#         # Create a Label Widget to display the text or Image
#         self.label = Label(self.frame)
#         self.label.place(x=0, y=400)
#         self.label.pack()
#
#         self.frame2 = Frame(self.newWindow, width=200, height=100, bg="gray90")
#         self.frame2.place(x=120, y=490)
#
#         self.label2 = Label(self.frame2, text="", font=my_font1, bg="black", fg="white")
#         self.label2.place(x=0, y=0)
#         self.label2.pack()
#
#
#         self.label3 = Label(self.frame3, text="", font=my_font1, bg="black", fg="white")
#         self.label3.place(x=0, y=0)
#         self.label3.pack()
#
#
#
#
#
#
#         self.newWindow.mainloop()
#
#     def Detection(self):
#         import os
#
#         import numpy as np
#         from keras.models import Model, load_model
#         from keras.preprocessing import image
#
#         best_model = load_model(r'D:\2NAAAAAA\gradution project\effiecientNET/cnn-parameters-improvement-05-1.00.model')
#
#         import pandas as pd
#         df = pd.read_csv(r"D:\New folder/submission.csv")
#         path1 = self.path
#         img = image.load_img(os.path.join(path1), target_size=(224, 224))
#         # crop_brain_contour(img)
#         img = np.asarray(img)
#         img = np.expand_dims(img, axis=0)
#         output = best_model.predict(img)
#         if output[0][0] > output[0][1]:
#             print("no")
#             f = output[0][0] * 100
#             self.label2.configure(text="No Tumor Detected")
#             self.label3.configure(text="Probability of Tumor: " + str(f), font='cambria')
#
#
#         else:
#             print('yes')
#             f = output[0][1] * 100
#             self.label2.configure(text="Tumor Detected", fg="red", anchor="nw")
#             self.label3.configure(text="Probability of Tumor: " + str(f), font='cambria')
#
# # ND1=ND()