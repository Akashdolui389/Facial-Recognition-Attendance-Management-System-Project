from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from Student import Student
import os
from train import Train
from face_recognizer import Face_Recognizer
from Attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x830+0+0")
        self.root.title("Face Recognition System")

        # Bg Image
        img3=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Bg Image.jpg")
        img3 = img3.resize((1530, 790), Image.BILINEAR)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_l = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("Times New Roman", 35, "bold"), bg="white", fg="red")
        title_l.place(x=0, y=0, relwidth=1, height=110)

        # Student Button
        img4=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Student.jpg")
        img4 = img4.resize((270,220), Image.BILINEAR)
        self.Photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.Photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=100,y=130,width=270,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=100,y=350,width=270,height=40)

        #Face Detect Button
        img5=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Face detector.jpg")
        img5 = img5.resize((270,220), Image.BILINEAR)
        self.Photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.Photoimg5,command=self.Face_data, cursor="hand2")
        b1.place(x=540,y=130,width=270,height=220)

        b1_1=Button(bg_img,text="Face Detector",command=self.Face_data, cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=540,y=350,width=270,height=40)

        #Attendance Button
        img6=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Attendance.jpg")
        img6 = img6.resize((270,220), Image.BILINEAR)
        self.Photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.Photoimg6, cursor="hand2",command=self.attendance)
        b1.place(x=980,y=130,width=270,height=220)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance,font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=980,y=350,width=270,height=40)

        #Train Data Button
        img7=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Train Data.jpg")
        img7 = img7.resize((270,220), Image.BILINEAR)
        self.Photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.Photoimg7,command=self.train_data, cursor="hand2")
        b1.place(x=100,y=425,width=270,height=220)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data, cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=100,y=635,width=270,height=40)

        #Photo Button
        img8=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Photos.jpg")
        img8 = img8.resize((270,220), Image.BILINEAR)
        self.Photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.Photoimg8,command=self.open_img, cursor="hand2")
        b1.place(x=540,y=425,width=270,height=220)

        b1_1=Button(bg_img,text="Photos",command=self.open_img, cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=540,y=635,width=270,height=40)

        #Exit Button
        img9=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Exit.jpg")
        img9 = img9.resize((270,220), Image.BILINEAR)
        self.Photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.Photoimg9,command=self.Exit, cursor="hand2")
        b1.place(x=980,y=425,width=270,height=220)

        b1_1=Button(bg_img,text="EXIT",command=self.Exit, cursor="hand2",font=("Times New Roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=980,y=635,width=270,height=40)




    def Exit(self):
        self.Exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this Window",parent=self.root)
        if self.Exit > 0:
            self.root.destroy()
        else:
            return


    # Function Button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def open_img(self):
        os.startfile("Photo_data")

    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognizer(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()



