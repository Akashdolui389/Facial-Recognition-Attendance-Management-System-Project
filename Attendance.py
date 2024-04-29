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
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #variables
        self.var_attendance_id = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_dep = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_status = StringVar()


        # Bg Image
        img3=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Bg Image.jpg")
        img3 = img3.resize((1530, 790), Image.BILINEAR)
        self.Photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.Photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_l=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Times New Roman",35,"bold"),bg="white", fg="Blue")
        title_l.place(x=0,y=0,width=1365,height=110)

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=10, y=120, width=1340, height=570)


        #Left label frame
        Left_frame = LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="STUDENT INFORMATION",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=550)

        img_left=Image.open(r"C:\Users\Akash Dolui\OneDrive\Desktop\Attendance management system project\Images\Image3.jpg")
        img_left = img_left.resize((640, 130), Image.BILINEAR)
        self.Photoimg_left=ImageTk.PhotoImage(img_left)

        f_l=Label(Left_frame,image=self.Photoimg_left)
        f_l.place(x=2, y=0, width=640, height=130)


        #Student information frame
        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=1, y=135, width=640, height=380)

        
        # Labels and Entry
        #Attendance Id
        AttendanceID_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"))
        AttendanceID_label.grid(row=0,column=0,padx=10,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_id,font=("times new roman",13,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)


        #Roll No
        RollNo_label=Label(left_inside_frame,text="RollNo:",font=("times new roman",13,"bold"))
        RollNo_label.grid(row=0,column=2,padx=25,sticky=W)

        RollNo_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_roll,font=("times new roman",13,"bold"))
        RollNo_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)


        #Name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"))
        name_label.grid(row=1,column=0,padx=25,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_name,font=("times new roman",13,"bold"))
        name_entry.grid(row=1,column=1,padx=0,pady=8,sticky=W)


        #Department
        Department_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"))
        Department_label.grid(row=1,column=2,padx=10,sticky=W)

        Department_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_dep,font=("times new roman",13,"bold"))
        Department_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)


        #Time
        Time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"))
        Time_label.grid(row=2,column=0,padx=25,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_time,font=("times new roman",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=0,pady=5,sticky=W)


        #Date
        Date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"))
        Date_label.grid(row=2,column=2,padx=34,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=19,textvariable=self.var_attendance_date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)


        #Attendance Status
        Attendance_status_label=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",13,"bold"))
        Attendance_status_label.grid(row=3,column=0,padx=10,sticky=W)

        self.attendance_Status = ttk.Combobox(left_inside_frame,textvariable=self.var_attendance_status, font=("times new roman", 13, "bold"), state="readonly", width=17)
        self.attendance_Status["values"] = ("Status", "Present", "Absent")
        self.attendance_Status.current(0)
        self.attendance_Status.grid(row=3, column=1, padx=0, pady=5, sticky=W)


        #Button Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=2,y=320,width=630,height=37)

        #Import button

        import_btn=Button(btn_frame,text="Import CSV",command=self.importCSV,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        #Export button
        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        #Reset button
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Reset_btn.grid(row=0,column=3)





        #Right label frame
        RIGHT_frame = LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=670,y=10,width=650,height=550)


        table_frame = Frame(RIGHT_frame, bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=3, y=3, width=637, height=512)


        # Scroll Bar Table
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(table_frame,columns=("ID","RollNo","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)
        

        self.attendanceReportTable.heading("ID",text="Attendance ID")
        self.attendanceReportTable.heading("RollNo",text="Roll No")
        self.attendanceReportTable.heading("Name",text="Name")
        self.attendanceReportTable.heading("Department",text="Department")
        self.attendanceReportTable.heading("Time",text="Time")
        self.attendanceReportTable.heading("Date",text="Date")
        self.attendanceReportTable.heading("Attendance",text="Attendance")

        self.attendanceReportTable["show"]="headings"
        self.attendanceReportTable.column("ID",width=100)
        self.attendanceReportTable.column("RollNo",width=100)
        self.attendanceReportTable.column("Name",width=100)
        self.attendanceReportTable.column("Department",width=100)
        self.attendanceReportTable.column("Time",width=100)
        self.attendanceReportTable.column("Date",width=100)
        self.attendanceReportTable.column("Attendance",width=100)


        self.attendanceReportTable.pack(fill=BOTH,expand=1)

        self.attendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# fetch data
    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())
        for i in rows:
            self.attendanceReportTable.insert("",END,values=i)


    # Import CSV
    def importCSV(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)



    #Export CSV
    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data found to Export",parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                export_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                    messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(file_name)+" Successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)



    # Update Function
    # Update Function
    def update_data(self):
        # Get the index of the selected row
        selected_row = self.attendanceReportTable.focus()
        if selected_row:
            # Get the values from the entry fields
            attendance_id = self.var_attendance_id.get()
            roll_no = self.var_attendance_roll.get()
            name = self.var_attendance_name.get()
            department = self.var_attendance_dep.get()
            time = self.var_attendance_time.get()
            date = self.var_attendance_date.get()
            status = self.var_attendance_status.get()

            # Update the data in the table
            self.attendanceReportTable.item(selected_row, values=(attendance_id, roll_no, name, department, time, date, status))

            # Update the data in mydata list
            index = int(selected_row[1:]) - 1  # Extract row number from selected row id
            mydata[index] = [attendance_id, roll_no, name, department, time, date, status]

            # Update the CSV file
            file_name = "attendance.csv"  # Provide the name of your CSV file
            with open(file_name, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                export_write.writerows(mydata)

            # Show a message indicating that the data has been updated
            messagebox.showinfo("Update", "Data Updated Successfully")
        else:
            # If no row is selected, show an error message
            messagebox.showerror("Error", "Please select a record to update")

    


    def get_cursor(self,event=""):
        cursor_row = self.attendanceReportTable.focus()
        content = self.attendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_dep.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_status.set(rows[6])




    # Reset Function
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_name.set("")
        self.var_attendance_dep.set("")
        self.var_attendance_time.set("")
        self.var_attendance_date.set("")
        self.var_attendance_status.set("")











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()