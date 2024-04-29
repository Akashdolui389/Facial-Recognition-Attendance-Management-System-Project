from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x830+0+0")
        self.root.title("Face Recognition System")

        title_l=Label(self.root, text="Face Recognizer", font=("Times New Roman",35,"bold"),bg="white", fg="Blue")
        title_l.place(x=0, y=0, relwidth=1, height=110)

        #First Image
        img_top=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Image1.png")
        img_top = img_top.resize((700, 700), Image.BILINEAR)
        self.Photoimg_top=ImageTk.PhotoImage(img_top)

        f_l=Label(self.root,image=self.Photoimg_top)
        f_l.place(x=2, y=115, width=700, height=700)

        #Second Image
        img_bottom=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Train Data.jpg")
        img_bottom = img_bottom.resize((821, 700), Image.BILINEAR)
        self.Photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_l=Label(self.root,image=self.Photoimg_bottom)
        f_l.place(x=704, y=115, width=821, height=700)

        #Face Recognizer Button
        b1_1=Button(f_l,text="FACE RECOGNIZER",command=self.face_recognizer, cursor="hand2",font=("Times New Roman",20,"bold"),bg="Red", fg="white")
        b1_1.place(x=24,y=468,width=400,height=110)


    # Attendance
    def mark_attendance(self,i,r,n,c):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list)):
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1},present")




        #Face Recognizer Function
    def face_recognizer(self):
        def draw_boundray(img,classifier,scaleFactor,min_neighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,min_neighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll_no from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Course from student where Student_id="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)



                if confidence>85:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll_no:{r}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
                    cv2.putText(img,"Unknown Face",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
            
        def recognizer(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret, img=video_cap.read()
            img=recognizer(img,clf,face_cascade)
            cv2.imshow("Face Recognizer",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognizer(root)
    root.mainloop()