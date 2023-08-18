from tkinter import *
import customtkinter
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class ManageTeachers(customtkinter.CTk):
    def __init__(self, root, center_frame,inner_frame):
        self.root = root
        self.center_frame = center_frame
        self.inner_frame = inner_frame

        

    def teacher_sidebar_frame(self):
        self.inner_frame.destroy()
        self.inner_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.inner_frame.columnconfigure(0, weight=1)
        label = customtkinter.CTkLabel(self.inner_frame, text="Teaching Staff",font=customtkinter.CTkFont(size=18, weight="bold"))
        label.grid(row=1, column=0, padx=15, pady=(20,10))
        view_button = customtkinter.CTkButton(self.inner_frame, text="View Staff",command=self.view_teachers,cursor="hand2")
        view_button.grid(row=2, column=0, padx=15, pady=(20,10))
        add_button = customtkinter.CTkButton(self.inner_frame,cursor="hand2",command=self.add_teachers_frame, text="Add Teacher")
        add_button.grid(row=3, column=0, padx=15, pady=(20,10))
        up_del_button = customtkinter.CTkButton(self.inner_frame,cursor="hand2",command=self.update_delete_frame, text="Update / Delete")
        up_del_button.grid(row=4, column=0, padx=15, pady=(20,10))
        print("manage teachers clicked")
        return self.inner_frame




    def view_teachers(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root,corner_radius=10)
        self.center_frame.columnconfigure(0, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=15,sticky="nsew")
        label = customtkinter.CTkLabel(self.center_frame, text="View staff details",font=customtkinter.CTkFont(size=32, weight="bold"))
        label.grid(row=0, column=0)

        conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        style = ttk.Style()
        style.theme_use('winnative')
        style.configure("mystyle.Treeview",highlightthickness=0, bd=0, font=("calibari",13, "bold"))
        style.configure("mystyle.Treeview", font=("calibari",13,"bold"))
        style.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':"nsew"})])
        style.configure("mystyle.Treeview", rowheight=20)

        self.treeview = ttk.Treeview(self.center_frame,column=["ID","Name","Father's Name","CNIC","Gender","Education","Subject","Contact"],show="headings",style="mystyle.Treeview",height=30, selectmode="browse")
        self.treeview.grid(row=1, column=0, columnspan=2, sticky="nsew")
        columns = ["ID","Name","Father's Name","CNIC","Gender","Education","Subject","Contact"]
        col_width = [40,130,130,120,60,100,80,100]
        
        for col, column_width in zip (columns, col_width):
            self.treeview.column(col, width=column_width, anchor='w')
            self.treeview.heading(col,text=col)
        for row in rows:
            self.treeview.insert("","end",values=row)

        return self.center_frame

    
        

    def update_db(self):
        id = self.teacher_id_entry.get()
        name = self.name_entry.get()
        f_name = self.f_name_entry.get()
        cnic = self.cnic_entry.get()
        gender = self.gender_combo.get()
        education = self.qualification_combo.get()
        subject = self.subject_entry.get()
        contact = self.contact_entry.get()
        
        conn = mysql.connector.connect(host="localhost", username="root", password="Azhar123@", database="mips_sms")
        cursor = conn.cursor()
        query = "UPDATE teachers SET teacher_name=%s,tf_name=%s, cnic =%s, gender=%s, qualification=%s,subject=%s, contact=%s WHERE teacher_id =%s"
        values = (name, f_name, cnic,gender,education,subject,contact,id)
        try:
            cursor.execute(query, values)
            conn.commit()
            print("Database update successful")
        except mysql.connector.Error as e:
            print("Database error:", e)
            conn.rollback()
            conn.close()
        messagebox.showinfo("Success", "Data updated successfully")
        self.teacher_id_entry.delete(0,"end")
        self.name_entry.delete(0,"end")
        self.cnic_entry.delete(0,"end")
        self.subject_entry.delete(0,"end")
        self.contact_entry.delete(0,"end")


    def ask_que(self):
        select_item = self.treeview.selection()
        if select_item:
            confrim = messagebox.askquestion("Confrimition","Are you sure you want to delete this record ?")
            if confrim=="yes":
                selected_record = self.treeview.item(select_item)['values']
                self.treeview.delete(select_item)

                self.delete(selected_record[0])

    def delete(self, record_id):
        conn = mysql.connector.connect(host="localhost", username="root",password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM teachers WHERE teacher_id = {record_id}")
        conn.commit()   
        messagebox.showinfo("success","Record deleted successfully")
        cursor.close()
        conn.close()



    def add(self):
        id = self.teacher_id_entry.get()
        name = self.name_entry.get()
        f_name = self.f_name_entry.get()
        cnic = self.cnic_entry.get()
        gender = self.gender_combo.get()
        quilification = self.qualification_combo.get()
        subject = self.subject_entry.get()
        contact = self.contact_entry.get()

        if self.teacher_id_entry.get()=="" or self.name_entry.get()=="" or self.f_name_entry.get()=="" or self.cnic_entry.get()=="" or self.gender_combo.get()=="" or self.qualification_combo.get()=="" or self.subject_entry.get()=="" or self.contact_entry.get()=="" :
            messagebox.showerror("ERROR !", "Don't leave any field empty !")
        try:
            connection = mysql.connector.connect(host="localhost",username="root", password="Azhar123@", database="mips_sms")
            cursor = connection.cursor()
            query = "INSERT INTO teachers (teacher_id, teacher_name,tf_name,cnic, gender, qualification, subject, contact) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (id, name, f_name, cnic,gender,quilification,subject,contact)
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Message", "Reacord added successfully")
        except Exception as error:
            messagebox.showerror("Error",f"Error {error}")
            self.teacher_id_entry.delete(0, 'end')
            self.name_entry.delete(0, 'end')
            self.f_name_entry.delete(0,'end')
            self.cnic_entry.delete(0,'end')
            self.subject_entry.delete(0,'end')
            self.contact_entry.delete(0, 'end')
            self.name_entry.focus_set()
        finally:
            if connection:
                connection.close()
    
    
    def select_record(self, event):
        self.teacher_id_entry.delete(0,'end')
        self.name_entry.delete(0,'end')
        self.f_name_entry.delete(0,'end')
        self.cnic_entry.delete(0,'end')
        self.subject_entry.delete(0,'end')
        self.contact_entry.delete(0,'end')
        self.gender_combo.set('--Select gender--')
        self.qualification_combo.set('--Select Qualification--')
        selected_item = self.treeview.focus()
        values = self.treeview.item(selected_item,'values')
        self.teacher_id_entry.insert(0,values[0])
        self.name_entry.insert(0,values[1])
        self.f_name_entry.insert(0,values[2])
        self.cnic_entry.insert(0,values[3])
        ops = ['Male','Female']
        self.gender_combo['values'] = ops
        ed_ops = ['Intermediate','BS/B.Sc/B.A','MS/M.Sc/M.Phil','Ph.D']
        self.qualification_combo['values'] = ed_ops
        self.subject_entry.insert(0,values[6])
        self.contact_entry.insert(0,values[7])

        self.treeview.bind("<<ButtonRelease-1>>",selected_item)

    
    def add_teachers_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.center_frame.grid(row=0,column=1, rowspan=15,sticky="nsew")
        self.center_frame.columnconfigure(1, weight=1)
        label = customtkinter.CTkLabel(self.center_frame, text="Add new teacher",font=customtkinter.CTkFont(size=32, weight="bold"))
        label.grid(row=0, column=1, columnspan=2)
        label1 = customtkinter.CTkLabel(self.center_frame, text="Teacher's_ID",font=customtkinter.CTkFont(size=18, weight="bold"))
        label1.grid(row=1, column=0, sticky="w", padx=20, pady=(10,5))
        self.teacher_id = random.randint(1000, 9999)
        self.teacher_id_entry = customtkinter.CTkEntry(self.center_frame, height=40, font=('calibari',15))
        self.teacher_id_entry.grid(row=1, column=1, sticky="nsew", padx=20, pady=(10,5))
        self.teacher_id_entry.delete(0, 'end')
        self.teacher_id_entry.insert(0, self.teacher_id)
        label1 = customtkinter.CTkLabel(self.center_frame, text="Name",font=customtkinter.CTkFont(size=18, weight="bold"))
        label1.grid(row=2, column=0, sticky="w",  padx=20, pady=(10,5))
        self.name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Name here", height=40, font=('calibari',15))
        self.name_entry.grid(row=2, column=1, sticky="nsew", padx=20, pady=(10,5))
        label2 = customtkinter.CTkLabel(self.center_frame, text="Father's/Husband's Name",font=customtkinter.CTkFont(size=18, weight="bold"))
        label2.grid(row=3, column=0, sticky="w", padx=20, pady=(10,5))
        self.f_name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Father's/Husband's Name here", height=40, font=('calibari',15))
        self.f_name_entry.grid(row=3, column=1, sticky="nsew", padx=20, pady=(10,5))
        label3 = customtkinter.CTkLabel(self.center_frame, text="CNIC",font=customtkinter.CTkFont(size=18, weight="bold"))
        label3.grid(row=4, column=0, sticky="w", padx=20, pady=(10,5))
        self.cnic_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Enter CNIC", height=40, font=('calibari',15))
        self.cnic_entry.grid(row=4, column=1, sticky="nsew", padx=20, pady=(10,5))
        label4 = customtkinter.CTkLabel(self.center_frame, text="Gender",font=customtkinter.CTkFont(size=18, weight="bold"))
        label4.grid(row=5, column=0, sticky="w", padx=20, pady=(10,5))
        value = ['Male','Female']
        self.gender_combo = customtkinter.CTkComboBox(self.center_frame,values=value, height=40, font=('calibari',15))
        self.gender_combo.grid(row=5, column=1, sticky="nsew", padx=20, pady=(10,5))
        self.gender_combo.set('--Select gender--')
        label5 = customtkinter.CTkLabel(self.center_frame, text="Qualification",font=customtkinter.CTkFont(size=18, weight="bold"))
        label5.grid(row=6, column=0, sticky="w", padx=20, pady=(10,5))
        value = ['Intermediate','BS/B.Sc/B.A','MS/M.Sc/M.Phil','Ph.D']
        self.qualification_combo = customtkinter.CTkComboBox(self.center_frame,values=value, height=40, font=('calibari',15))
        self.qualification_combo.set('--Select Qualification--')
        self.qualification_combo.grid(row=6, column=1, sticky="nsew", padx=20, pady=(10,5))
        label6 = customtkinter.CTkLabel(self.center_frame, text="Subject",font=customtkinter.CTkFont(size=18, weight="bold"))
        label6.grid(row=7, column=0, sticky="w", padx=20, pady=(10,5))
        self.subject_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Enter Subject", height=40, font=('calibari',15))
        self.subject_entry.grid(row=7, column=1, sticky="nsew", padx=20, pady=(10,5))
        label8 = customtkinter.CTkLabel(self.center_frame, text="Contact",font=customtkinter.CTkFont(size=18, weight="bold"))
        label8.grid(row=8, column=0, sticky="w", padx=20, pady=(10,5))
        self.contact_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Contact", height=40, font=('calibari',15))
        self.contact_entry.grid(row=8, column=1, sticky="nsew", padx=20, pady=(10,5))
        add_button = customtkinter.CTkButton(self.center_frame, text="Submit", command=self.add, height=40)
        add_button.grid(row=9, column=1, padx=20, pady=(10,5), sticky="nsew")

        return self.center_frame
    

    def update_delete_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.center_frame.grid(row=0, column=1, rowspan=15,columnspan=1, sticky="nsew")
        self.center_frame.columnconfigure(0, weight=1)
        label = customtkinter.CTkLabel(self.center_frame, text="Update / Delete Staff",font=customtkinter.CTkFont(size=32, weight="bold"))
        label.grid(row=0, column=0)
        self.teacher_id_entry = customtkinter.CTkEntry(self.center_frame,width=500, placeholder_text="Teacher ID")
        self.teacher_id_entry.grid(row=1, column=0, pady=4)
        self.name_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Name", width=500)
        self.name_entry.grid(row=2, column=0, pady=4)
        self.f_name_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text="Father's/Husband's Name", width=500)
        self.f_name_entry.grid(row=3, column=0, pady=4)
        self.cnic_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="CNIC", width=500)
        self.cnic_entry.grid(row=4, column=0, pady=4)
        value = ['Male','Female']
        self.gender_combo = customtkinter.CTkComboBox(self.center_frame,width=500,values=value)
        self.gender_combo.grid(row=5, column=0, pady=4)
        self.gender_combo.set('--Select gender--')
        value = ['Intermediate','BS/B.Sc/B.A','MS/M.Sc/M.Phil','Ph.D']
        self.qualification_combo = customtkinter.CTkComboBox(self.center_frame,width=500,values=value)
        self.qualification_combo.set('--Select Qualification--')
        self.qualification_combo.grid(row=6, column=0, pady=4)
        self.subject_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Subject", width=500)
        self.subject_entry.grid(row=7, column=0, pady=4)
        self.contact_entry = customtkinter.CTkEntry(self.center_frame,placeholder_text="Contact", width=500)
        self.contact_entry.grid(row=8, column=0, pady=4)
        add_button = customtkinter.CTkButton(self.center_frame, text="Update",width=500, command=self.update_db)
        add_button.grid(row=9, column=0, pady=4)
        delete_button = customtkinter.CTkButton(self.center_frame, command=self.ask_que, text="Delete",width=500)
        delete_button.grid(row=10, column=0, pady=4)
        conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        style = ttk.Style()
        style.theme_use('winnative')
        style.configure("mystyle.Treeview",highlightthickness=0, bd=0, font=("calibari",14, "bold"))
        style.configure("mystyle.Treeview", font=("calibari",14,'bold'))
        style.layout("mystyle.Treeview",[("mystyle.Treeview.treearea",{'sticky':"nswe"})])
        style.configure("mystyle.Treeview", rowheight=25)

        self.treeview = ttk.Treeview(self.center_frame, column=["ID","Name","Father's Name","CNIC","Gender","Education","Subject","Contact"],show="headings",style="mystyle.Treeview",height=13, selectmode="browse")
        self.treeview.grid(row=11, column=0, columnspan=2,sticky='nsew')
        columns = ["ID","Name","Father's Name","CNIC","Gender","Education","Subject","Contact"]
        col_width = [40,130,130,120,60,100,80,100]
        
        for col, column_width in zip (columns, col_width):
            self.treeview.column(col, width=column_width, anchor='center')
            self.treeview.heading(col,text=col, anchor='center')

        for row in rows:
            self.treeview.insert("","end",values=row)

        self.treeview.bind("<<TreeviewSelect>>", self.select_record)
        return self.center_frame