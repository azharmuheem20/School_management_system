import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import random


class Students:
    def __init__(self,root, inner_frame, center_rame):
        self.root = root
        self.center_frame = center_rame
        self.inner_frame = inner_frame


    def view_options(self):
        self.inner_frame.destroy()
        self.inner_frame = customtkinter.CTkFrame(self.root,corner_radius=10)
        self.inner_frame.columnconfigure(0,weight=1)
        label = customtkinter.CTkLabel(self.inner_frame,font=customtkinter.CTkFont(size=16, weight="bold"), text="Manage Studants")
        label.grid(row=1, column=0,padx=20, pady=(20,10))
        view_button = customtkinter.CTkButton(self.inner_frame, text="View Students", command=self.view_students)
        view_button.grid(row=2, column=0,padx=20, pady=(20,10))
        add_button = customtkinter.CTkButton(self.inner_frame, text="Add Students", command=self.add_students_frame)
        add_button.grid(row=3, column=0,padx=20, pady=(20,10))
        del_up_button = customtkinter.CTkButton(self.inner_frame, text="Update/Delete", command=self.update_students_frame)
        del_up_button.grid(row=4, column=0,padx=20, pady=(20,10))

        return self.inner_frame

    def view_students(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.grid(row=0, column=1,rowspan=15, sticky="nsew")
        view_label = customtkinter.CTkLabel(self.center_frame,font=customtkinter.CTkFont(size=30, weight="bold"), text="Enrolled Students")
        view_label.grid(row=1, column=0)

        conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@", database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        style = ttk.Style()
        style.theme_use('winnative')
        style.configure("mystyle.Treeview",highlightthickness=0, bd=0, font=("calibari",14, "bold"))
        style.configure("mystyle.Treeview", font=("calibari",14,'bold'))
        style.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':"nswe"})])
        style.configure("mystyle.Treeview", rowheight=25)

        self.treeview = ttk.Treeview(self.center_frame, show='headings', columns=['Roll',"Name","Father's name","Surname","Age","Class","Gender","Contact"], height=35)
        self.treeview.grid(row=2,column=0, columnspan=2, sticky='nsew')
        col_names = ['Roll',"Name","Father's name","Surname","Age","Class","Gender","Contact"]
        col_width = [50,100,100,100,30,30,50,100]
        for col, col_width in zip(col_names,col_width):
            self.treeview.column(col, width=col_width, anchor='center')
            self.treeview.heading(col, text=col, anchor='center')

        for row in data:
            self.treeview.insert("",'end',values=row)

        return self.center_frame
    
    def add_student(self):
        roll = self.std_roll_entry.get()
        name = self.name_entry.get()
        f_name = self.f_name_entry.get()
        surname = self.surname_entry.get()
        age = self.age_entry.get()
        clss = self.class_entry.get()
        gender = self.gender_combo.get()
        contact = self.contact_entry.get()
        if self.std_roll_entry.get()=="" or self.name_entry.get()=="" or self.f_name_entry.get()=="" or self.surname_entry.get()=="" or self.age_entry.get()=="" or self.class_entry.get()=="" or self.gender_combo.get()=="" or self.contact_entry.get()=="":
            messagebox.showerror("ERROR","Do not leave any field empty !")
        try:
            connection = mysql.connector.connect(host="localhost",username="root", password="Azhar123@", database="mips_sms")
            cursor = connection.cursor()
            query = "INSERT INTO students (roll, student_name,sf_name,surname,age,class, gender, contact) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (roll, name, f_name, surname,age,clss,gender,contact)
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Message", "Reacord added successfully")
        except Exception as err:
            messagebox.showerror("Error",f"Oops ! {err}")
        finally:
            if connection:
                connection.close()

            self.std_roll_entry.delete(0, 'end')
            self.name_entry.delete(0,'end')
            self.f_name_entry.delete(0,'end')
            self.surname_entry.delete(0,'end')
            self.age_entry.delete(0,'end')
            self.class_entry.set('--Enter Class--')
            self.gender_combo.set('--Select Gender--')
            self.contact_entry.delete(0,'end')
            self.name_entry.focus_set()

    def add_students_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root,corner_radius=10)
        self.center_frame.grid(row=0, column=1,sticky='nsew', rowspan=15)
        self.center_frame.columnconfigure(1,weight=1)
        label1 = customtkinter.CTkLabel(self.center_frame, text="Add Students",font=customtkinter.CTkFont(size=18, weight="bold"))
        label1.grid(row=0, column=1)
        label1 = customtkinter.CTkLabel(self.center_frame, text="Students's_Roll No",font=customtkinter.CTkFont(size=18, weight="bold"))
        label1.grid(row=1, column=0, sticky="w", padx=20, pady=(10,5))
        self.std_roll = random.randint(10000,99999)
        self.std_roll_entry = customtkinter.CTkEntry(self.center_frame)
        self.std_roll_entry.grid(row=1, column=1, sticky="nsew", padx=20, pady=(10,5))
        self.std_roll_entry.delete(0, 'end')
        self.std_roll_entry.insert(0,self.std_roll)
        label1 = customtkinter.CTkLabel(self.center_frame, text="Student's Name",font=customtkinter.CTkFont(size=18, weight="bold"))
        label1.grid(row=2, column=0, sticky="w", padx=20, pady=(10,5))
        self.name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Name here")
        self.name_entry.grid(row=2, column=1, sticky="nsew", padx=20, pady=(10,5))
        label2 = customtkinter.CTkLabel(self.center_frame, text="Father's Name",font=customtkinter.CTkFont(size=18, weight="bold"))
        label2.grid(row=3, column=0, sticky="w", padx=20, pady=(10,5))
        self.f_name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Father's Name here")
        self.f_name_entry.grid(row=3, column=1, sticky="nsew", padx=20, pady=(10,5))
        label3 = customtkinter.CTkLabel(self.center_frame, text="Surname",font=customtkinter.CTkFont(size=18, weight="bold"))
        label3.grid(row=4, column=0, sticky="w", padx=20, pady=(10,5))
        self.surname_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Student Surname")
        self.surname_entry.grid(row=4, column=1, sticky="nsew", padx=20, pady=(10,5))
        age_label = customtkinter.CTkLabel(self.center_frame, text="Age",font=customtkinter.CTkFont(size=18, weight="bold"))
        age_label.grid(row=5, column=0, sticky="w", padx=20, pady=(10,5))
        self.age_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Age")
        self.age_entry.grid(row=5, column=1, sticky="nsew", padx=20, pady=(10,5))
        class_label = customtkinter.CTkLabel(self.center_frame, text="Class",font=customtkinter.CTkFont(size=18, weight="bold"))
        class_label.grid(row=6, column=0, sticky="w", padx=20, pady=(10,5))
        self.class_entry = customtkinter.CTkComboBox(self.center_frame,state="readonly",values=['Nursery','K.G','One','Two','Three','Four','Five','Six','Seven','Eight','Ninth','Matric','Eleventh','Intermediate'])
        self.class_entry.grid(row=6, column=1, sticky="nsew", padx=20, pady=(10,5))
        self.class_entry.set('--Enter Class--')
        label4 = customtkinter.CTkLabel(self.center_frame, text="Gender",font=customtkinter.CTkFont(size=18, weight="bold"))
        label4.grid(row=7, column=0, sticky="w", padx=20, pady=(10,5))
        self.gender_combo = customtkinter.CTkComboBox(self.center_frame,state="readonly", values=["Male","Female"])
        self.gender_combo.set("---Select gender---")
        self.gender_combo.grid(row=7, column=1, sticky="nsew", padx=20, pady=(10,5))
        label8 = customtkinter.CTkLabel(self.center_frame, text="Contact",font=customtkinter.CTkFont(size=18, weight="bold"))
        label8.grid(row=8, column=0, sticky="w", padx=20, pady=(10,5))
        self.contact_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Contact")
        self.contact_entry.grid(row=8, column=1, sticky="nsew", padx=20, pady=(10,5))
        add_button = customtkinter.CTkButton(self.center_frame, text="Add Student", command=self.add_student)
        add_button.grid(row=9, column=1, padx=20, pady=(10,5), sticky="nsew")

        return self.center_frame
    

    def update_students_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root,corner_radius=12)
        self.center_frame.grid(row=0,column=1, columnspan=1, sticky="nsew")
        self.center_frame.columnconfigure(0,weight=1)
        label = customtkinter.CTkLabel(self.center_frame,text="Update / Delete Students", font=('calibari',30,'bold'))
        label.grid(row=0, column=0)

        self.std_roll_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Student ID", width=500)
        self.std_roll_entry.grid(row=1, column=0, pady=4)
        self.name_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Name", width=500)
        self.name_entry.grid(row=2, column=0, pady=4)
        self.f_name_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Father's Name", width=500)
        self.f_name_entry.grid(row=3, column=0, pady=4)
        self.surname_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Surname", width=500)
        self.surname_entry.grid(row=4, column=0, pady=4)
        self.age_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Age", width=500)
        self.age_entry.grid(row=5, column=0, pady=4)
        values = ['Nursery','K.G','One','Two','Three','Four','Five','Six','Seven','Eight','Ninth','Matric','Eleventh','Intermediate']
        self.class_entry = customtkinter.CTkComboBox(self.center_frame,values=values, width=500)
        self.class_entry.grid(row=6, column=0, pady=4)
        self.class_entry.set('--Enter Class--')
        self.gender_combo = customtkinter.CTkComboBox(self.center_frame,width=500, values=['Male','Female'])
        self.gender_combo.grid(row=7, column=0, pady=4)
        self.gender_combo.set('--select Gender--')
        self.contact_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Contact", width=500)
        self.contact_entry.grid(row=8, column=0, pady=4)
        update_button = customtkinter.CTkButton(self.center_frame,width=500, command=self.update_student, text="Update Record")
        update_button.grid(row=9, column=0, pady=4)
        delete_button = customtkinter.CTkButton(self.center_frame, width=500,command=self.delete_permission, text="Delete Record")
        delete_button.grid(row=10, column=0, pady=4)

        conn = mysql.connector.connect(host="localhost",username="root", password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        conn.close()


        style = ttk.Style()
        style.theme_use('winnative')
        style.configure("mystyle.Treeview",highlightthickness=0, bd=0, font=("calibari",14, "bold"))
        style.configure("mystyle.Treeview", font=("calibari",14,'bold'))
        style.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':"nswe"})])
        style.configure("mystyle.Treeview", rowheight=25)


        self.treeview = ttk.Treeview(self.center_frame, columns=['Roll',"Name","Father's name","Surname","Age","Class","Gender","Contact"], show='headings', height=13)
        self.treeview.grid(row=11, column=0, sticky='nsew')

        col_names = ['Roll',"Name","Father's name","Surname","Age","Class","Gender","Contact"]
        col_width = [50,100,100,100,30,30,50,100]
        for col, col_width in zip(col_names,col_width):
            self.treeview.column(col, width=col_width, anchor='center')
            self.treeview.heading(col, text=col, anchor='center')

        for row in data:
            self.treeview.insert("",'end',values=row)


        self.treeview.bind("<<TreeviewSelect>>", self.select_record)
        return self.center_frame
    
    def select_record(self, event):
        self.gender_combo.set('--Select Gender--')
        self.class_entry.set('--Enter Class--')
        self.std_roll_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.f_name_entry.delete(0, 'end')
        self.surname_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.contact_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')

        selected_record = self.treeview.focus()
        value = self.treeview.item(selected_record, "values")

        self.std_roll_entry.insert(0,value[0])
        self.name_entry.insert(0, value[1])
        self.f_name_entry.insert(0, value[2])
        self.surname_entry.insert(0,value[3])
        self.age_entry.insert(0, value[4])
        cls = ['Nursery','K.G','One','Two','Three','Four','Five','Six','Seven','Eight','Ninth','Matric','Eleventh','Intermediate']
        self.class_entry['value'] = cls
        ops = ["Male", "Female"]
        self.gender_combo['value'] = ops
        self.contact_entry.insert(0,value[7])

        self.treeview.bind("<<ButtonRelease-1>>",selected_record)

    def update_student(self):
        id = self.std_roll_entry.get()
        name = self.name_entry.get()
        fname = self.f_name_entry.get()
        surname= self.surname_entry.get()
        age = self.age_entry.get()
        clss = self.class_entry.get()
        gender = self.gender_combo.get()
        contact = self.contact_entry.get()
        conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        try:
            query = "UPDATE students SET student_name=%s, sf_name= %s, surname=%s, age=%s,class=%s,gender=%s,contact=%s WHERE roll=%s"
            values = (name, fname,surname,age, clss,gender,contact, id)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success","Record has been updated successfully")
        except Exception as err:
            messagebox.showerror("Error",f"There is database error {err}")
            cursor.close()
        finally:
            if conn:
               conn.close()
        
        self.std_roll_entry.delete(0, 'end')
        self.name_entry.delete(0,'end')
        self.f_name_entry.delete(0,'end')
        self.surname_entry.delete(0,'end')
        self.age_entry.delete(0,'end')
        self.class_entry.set('--Enter Class--')
        self.gender_combo.set('--Select Gender--')
        self.contact_entry.delete(0, 'end')
    
    
    def delete_permission(self):
        selected_item = self.treeview.selection()
        if selected_item:
            confrim = messagebox.askquestion("Confirmtion","Are you sure you want to delete this record ?")
            if confrim=="yes":
                selected_record = self.treeview.item(selected_item)['values']
                self.treeview.delete(selected_item)
                self.delete(selected_record[0])

    def delete(self, record_id):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database="mips_sms")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM students WHERE roll={record_id}")
            conn.commit()
            messagebox.showinfo("Success","Record Deleted successfully")
        except Exception as err:
            cursor.close()
            messagebox.showerror("Database error",f"{err}")
        finally:
            if conn:
               conn.close()
