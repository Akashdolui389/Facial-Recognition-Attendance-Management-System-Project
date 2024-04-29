from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_l=Label(self.root, text="TRAIN DATASET", font=("Times New Roman",35,"bold"),bg="white", fg="Blue")
        title_l.place(x=0,y=0,width=1530,height=50)

        img_top=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Train Data.jpg")
        img_top = img_top.resize((1530, 290), Image.BILINEAR)
        self.Photoimg_top=ImageTk.PhotoImage(img_top)

        f_l=Label(self.root,image=self.Photoimg_top)
        f_l.place(x=0, y=56, width=1530, height=290)


        #Train Button
        b1_1=Button(self.root,text="TRAIN PHOTO SAMPLE",command=self.train_classifier, cursor="hand2",font=("Times New Roman",30,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=0,y=345,width=1530,height=54)

        img_bottom=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Train Data.jpg")
        img_bottom = img_bottom.resize((1530, 290), Image.BILINEAR)
        self.Photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_l=Label(self.root,image=self.Photoimg_bottom)
        f_l.place(x=0, y=400, width=1530, height=290)


    def train_classifier(self):
        data_dir=("Photo_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')      #Gray scale image
            image_np= np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training",image_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Photo sample Completed!!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()