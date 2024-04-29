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


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x830+0+0")
        self.root.title("Face Recognition System")

        # Variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_rollno=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()


        self.var_search_by = StringVar()
        self.var_search_by.set("Select")



        # Bg Image
        img3=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Bg Image.jpg")
        img3 = img3.resize((1530, 820), Image.BILINEAR)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=820)

        title_l=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman",35,"bold"),bg="white", fg="Blue")
        title_l.place(x=0, y=0, relwidth=1, height=110)

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10, y=120, width=1508, height=680)


        #Left label frame
        Left_frame = LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=635)

        img_left=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Image3.jpg")
        img_left = img_left.resize((720, 160), Image.BILINEAR)
        self.Photoimg_left=ImageTk.PhotoImage(img_left)

        f_l=Label(Left_frame,image=self.Photoimg_left)
        f_l.place(x=2, y=0, width=720, height=160)

        #Course Information
        Course_frame = LabelFrame(Left_frame,bd=4,bg="white",relief=RIDGE,text="Course Information",font=("times new roman",12,"bold"))
        Course_frame.place(x=1,y=165,width=720,height=125)


        def on_department_selected(event):
            selected_department = dep_combo.get()

            if selected_department == "ARTS":
                Course_combo["values"] = ("Select Course", "BA")
                Course_combo.current(0)
            elif selected_department == "COMMERCE":
                Course_combo["values"] = ("Select Course", "BCOM", "BMS", "BAF", "BBI", "BFM")
                Course_combo.current(0)
            elif selected_department == "SCIENCE":
                Course_combo["values"] = ("Select Course", "BSCIT", "BSCCS")
                Course_combo.current(0)
            else:
                Course_combo["values"] = ("Select Course",)
                Course_combo.current(0)


        #Department
        dep_label=Label(Course_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","ARTS","COMMERCE","SCIENCE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Bind the event when a selection is made in the department combo box
        dep_combo.bind("<<ComboboxSelected>>", on_department_selected)

        #Course
        Course_label=Label(Course_frame,text="Course",font=("times new roman",13,"bold"))
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo=ttk.Combobox(Course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        Course_combo["values"]=("Select Course","BA","BCOM","BMS","BAF","BBI","BFM","BSCIT","BSCCS")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        def on_year_selected(event):
            selected_year = Year_combo.get()

            if selected_year == "First Year":
                Semester_combo["values"] = ("Select Semester", "1 Semester", "2 Semester")
                Semester_combo.current(0)
            elif selected_year == "Second Year":
                Semester_combo["values"] = ("Select Semester", "3 Semester", "4 Semester")
                Semester_combo.current(0)
            elif selected_year == "Third Year":
                Semester_combo["values"] = ("Select Semester", "5 Semester", "6 Semester")
                Semester_combo.current(0)
            else:
                Semester_combo["values"] = ("Select Semester",)
                Semester_combo.current(0)


        # Year
        Year_label = ttk.Label(Course_frame, text="Year", font=("times new roman", 13, "bold"))
        Year_label.grid(row=1, column=0, padx=30, sticky=W)

        Year_combo = ttk.Combobox(Course_frame,textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        Year_combo["values"] = ("Select Year", "First Year", "Second Year", "Third Year")
        Year_combo.current(0)
        Year_combo.grid(row=1, column=1, padx=2, pady=17, sticky=W)

        # Bind the event when a selection is made in the Year combo box
        Year_combo.bind("<<ComboboxSelected>>", on_year_selected)

        # Semester
        Semester_label = ttk.Label(Course_frame, text="Semester", font=("times new roman", 13, "bold"))
        Semester_label.grid(row=1, column=2, padx=10, sticky=W)

        Semester_combo = ttk.Combobox(Course_frame,textvariable=self.var_sem, font=("times new roman", 13, "bold"), state="readonly", width=20)
        Semester_combo["values"] = ("Select Semester",)
        Semester_combo.current(0)
        Semester_combo.grid(row=1, column=3, padx=2, pady=17, sticky=W)


        #Student Information
        Student_frame = LabelFrame(Left_frame,bd=4,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Student_frame.place(x=1,y=300,width=720,height=300)


        #Student Id
        StudentID_label=Label(Student_frame,text="Student ID:",font=("times new roman",13,"bold"))
        StudentID_label.grid(row=0,column=0,padx=10,sticky=W)

        StudentID_entry=ttk.Entry(Student_frame,textvariable=self.var_id,width=19,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)


        #Student Name
        StudentName_label=Label(Student_frame,text="Student Name:",font=("times new roman",13,"bold"))
        StudentName_label.grid(row=0,column=2,padx=9,sticky=W)

        StudentName_entry=ttk.Entry(Student_frame,textvariable=self.var_name,width=19,font=("times new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)



        #Student Roll_No
        Student_RollNo_label=Label(Student_frame,text="Student RollNo:",font=("times new roman",13,"bold"))
        Student_RollNo_label.grid(row=1,column=0,padx=10,sticky=W)

        Student_RollNo_entry=ttk.Entry(Student_frame,textvariable=self.var_rollno,width=19,font=("times new roman",13,"bold"))
        Student_RollNo_entry.grid(row=1,column=1,padx=0,pady=5,sticky=W)



        #Student DOB
        Student_DOB_label=Label(Student_frame,text="DOB:",font=("times new roman",13,"bold"))
        Student_DOB_label.grid(row=1,column=2,padx=10,sticky=W)


        Student_DOB_cal = DateEntry(Student_frame,textvariable=self.var_dob, date_pattern="yyyy-mm-dd",width=17,calendar_position="bottom", font=("times new roman", 13, "bold"))
        Student_DOB_cal.grid(row=1, column=3, padx=0, pady=5, sticky=W)


        #Student Division
        Student_Division_label=Label(Student_frame,text="Student Div:",font=("times new roman",13,"bold"))
        Student_Division_label.grid(row=2,column=0,padx=10,sticky=W)

        Division_combo = ttk.Combobox(Student_frame,textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=17)
        Division_combo["values"] = ("Select Division", "A", "B", "C", "D")
        Division_combo.current(0)
        Division_combo.grid(row=2, column=1, padx=0, pady=5, sticky=W)


        #Student Gender
        Student_Gender_label=Label(Student_frame,text="Gender:",font=("times new roman",13,"bold"))
        Student_Gender_label.grid(row=2,column=2,padx=10,sticky=W)

        Gender_combo = ttk.Combobox(Student_frame,textvariable=self.var_gen, font=("times new roman", 13, "bold"), state="readonly", width=17)
        Gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=3, padx=2, pady=5, sticky=W)



        #Student Email
        Student_Email_label=Label(Student_frame,text="Email:",font=("times new roman",13,"bold"))
        Student_Email_label.grid(row=3,column=0,padx=10,sticky=W)

        Student_Email_entry=ttk.Entry(Student_frame,textvariable=self.var_email,width=19,font=("times new roman",13,"bold"))
        Student_Email_entry.grid(row=3,column=1,padx=0,pady=5,sticky=W)


        #Student Mobile
        Student_Mobile_label=Label(Student_frame,text="Mobile_No:",font=("times new roman",13,"bold"))
        Student_Mobile_label.grid(row=3,column=2,padx=10,sticky=W)

        Student_Mobile_entry=ttk.Entry(Student_frame,textvariable=self.var_mob,width=19,font=("times new roman",13,"bold"))
        Student_Mobile_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)


        #Radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=4,column=0)

        radiobutton2=ttk.Radiobutton(Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=4,column=1)


        #Button frame
        btn_frame=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=162,width=709,height=37)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #Delete button
        Delete_btn=Button(btn_frame,text="Delete",command=self.Delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Delete_btn.grid(row=0,column=2)

        #Reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.Reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=2,y=200,width=709,height=30)

        #Take photo
        Take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Collect Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Take_photo_btn.grid(row=0,column=0)

        #Update photo
        Update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Update_photo_btn.grid(row=0,column=1)










        #Right label frame
        RIGHT_frame = LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=745,y=10,width=745,height=635)


        img_Right=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Student.jpg")
        img_Right = img_Right.resize((734, 160), Image.BILINEAR)
        self.Photoimg_Right=ImageTk.PhotoImage(img_Right)

        f_l=Label(RIGHT_frame,image=self.Photoimg_Right)
        f_l.place(x=2, y=0, width=734, height=160)



        #Search System
        Search_frame = LabelFrame(RIGHT_frame,bd=4,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=1,y=165,width=734,height=80)

        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"))
        Search_label.grid(row=0,column=0,padx=10,sticky=W)

        self.Search_combo = ttk.Combobox(Search_frame, font=("times new roman", 15, "bold"), state="readonly", width=10)
        self.Search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        self.Search_combo.current(0)
        self.Search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        self.Search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        self.Search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        Search_btn=Button(Search_frame,text="Search",command=self.search_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        Show_All_btn=Button(Search_frame,text="Show All",command=self.show_all_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Show_All_btn.grid(row=0,column=4,padx=2)



        # Table Frame
        Table_frame = Frame(RIGHT_frame,bd=4,bg="white",relief=RIDGE)
        Table_frame.place(x=1,y=245,width=734,height=353)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.Student_table=ttk.Treeview(Table_frame,column=("dep","course","year","sem","id","name","div","rollno","gen","dob","email","mob","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("dep",text="Department")
        self.Student_table.heading("course",text="Course")
        self.Student_table.heading("year",text="Year")
        self.Student_table.heading("sem",text="Semester")
        self.Student_table.heading("id",text="Student ID")
        self.Student_table.heading("name",text="Student Name")
        self.Student_table.heading("div",text="Student Div")
        self.Student_table.heading("rollno",text="Student RollNo")
        self.Student_table.heading("gen",text="Gender")
        self.Student_table.heading("dob",text="DOB")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("mob",text="Mobile_No")
        self.Student_table.heading("photo",text="PhotoSample Status")
        self.Student_table["show"]="headings"

        self.Student_table.column("dep",width=100)
        self.Student_table.column("course",width=100)
        self.Student_table.column("year",width=100)
        self.Student_table.column("sem",width=100)
        self.Student_table.column("id",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("div",width=100)
        self.Student_table.column("rollno",width=100)
        self.Student_table.column("gen",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("mob",width=100)
        self.Student_table.column("photo",width=115)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease>",self.get_cursor)
        self.Fetch_data()


    # Function
    def add_data(self):
        if self.var_id.get()=="" or self.var_name.get()=="" or self.var_div.get()=="Select Division" or self.var_rollno.get()=="" or self.var_gen.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Akash@8806",database="face_recognition_system")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                        
                                                                                self.var_dep.get(),
                                                                                self.var_course.get(),
                                                                                self.var_year.get(),
                                                                                self.var_sem.get(),
                                                                                self.var_id.get(),
                                                                                self.var_name.get(),
                                                                                self.var_div.get(),
                                                                                self.var_rollno.get(),
                                                                                self.var_gen.get(),
                                                                                self.var_dob.get(),
                                                                                self.var_email.get(),
                                                                                self.var_mob.get(),
                                                                                self.var_radio1.get()
                                                                                                    ))
                conn.commit()
                self.Fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    # Fetch Data
    def Fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Akash@8806",database="face_recognition_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for i in data:
                self.Student_table.insert("",END,values=i)
            conn.commit()
        conn.close()




    # Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.Student_table.focus()
        content=self.Student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_rollno.set(data[7]),
        self.var_gen.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mob.set(data[11]),
        self.var_radio1.set(data[12])



# Update function
    def update_data(self):
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_div.get() == "Select Division" or self.var_rollno.get() == "" or self.var_gen.get() == "Select Gender" or self.var_dob.get() == "" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to Update this Student Details", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update Student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Mobile_No=%s,Photo_Sample=%s where Student_id=%s", (
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_rollno.get(),
                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_mob.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_id.get()
                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details Successfully Updated",parent=self.root)    
                conn.commit()
                self.Fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    # Delete Function
    def Delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be reqiured",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Data Delete","Do you want to delete this Student Details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
                    my_cursor = conn.cursor()
                    sql="Delete from student where Student_id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.Fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # Reset Function
    def Reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_rollno.set("")
        self.var_gen.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_mob.set("")
        self.var_radio1.set("")



    # Generate Dataset and Take photoSample
    def generate_dataset(self):
        if self.var_id.get() == "" or self.var_name.get() == "" or self.var_div.get() == "Select Division" or self.var_rollno.get() == "" or self.var_gen.get() == "Select Gender" or self.var_dob.get() == "" or self.var_email.get()=="" or self.var_mob.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                my_result=my_cursor.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cursor.execute("update Student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll_no=%s,Gender=%s,DOB=%s,Email=%s,Mobile_No=%s,Photo_Sample=%s where Student_id=%s", (
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_rollno.get(),
                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_mob.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_id.get()==id+1
                                                                                                                                                    ))
                conn.commit()
                self.Fetch_data()
                self.Reset_data()
                conn.close()


                # Face Frontals from opencv
                Face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    Faces=Face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum Neighbour=5

                    for (x,y,w,h) in Faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        print(f"Student ID: {id}")
                        file_path="Photo_data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==80:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)







    def search_data(self):
        if self.Search_entry.get() == "" or self.Search_combo.get() == "Select":
            messagebox.showerror("Error", "Please select both search criteria and enter search keyword", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
                my_cursor = conn.cursor()

                if self.Search_combo.get() == "Roll_No":
                    my_cursor.execute("select * from student where Roll_no LIKE %s", ('%' + self.Search_entry.get() + '%',))
                elif self.Search_combo.get() == "Phone_No":
                    my_cursor.execute("select * from student where Mobile_No LIKE %s", ('%' + self.Search_entry.get() + '%',))

                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.Student_table.delete(*self.Student_table.get_children())
                    for i in data:
                        self.Student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo("Info", "No record found", parent=self.root)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)





    def show_all_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Akash@8806", database="face_recognition_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for i in data:
                    self.Student_table.insert("", END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No records found", parent=self.root)

            conn.close()

        except Exception as es:
            messagebox.showerror("Error", f"Error: {str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()