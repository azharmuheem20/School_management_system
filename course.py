import tkinter
import customtkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


class CourseScheme:
    def __init__(self, root, center_frame, innser_frame):
        self.root = root
        self.center_frame = center_frame
        self.inner_frame = innser_frame


    def course_scheme_sidebar_frame(self):
        self.inner_frame.destroy()
        self.inner_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.inner_frame.grid(row=0, column=2)

        label = customtkinter.CTkLabel(self.inner_frame, text="Manage Course Scheme",font=('calibari',15,'bold'))
        label.grid(row=0, column=0, padx=20, pady=(10, 5))
        button = customtkinter.CTkButton(self.inner_frame,text="View Course", command=self.view_course_center_frame)
        button.grid(row=1, column=0, padx=20, pady=(10, 5))
        button2 = customtkinter.CTkButton(self.inner_frame,text="Add Course", command=self.add_course)
        button2.grid(row=2, column=0, padx=20, pady=(10, 5))
        button3 = customtkinter.CTkButton(self.inner_frame,text="Update/Delete", command=self.update_delete_frame)
        button3.grid(row=3, column=0, padx=20, pady=(10, 5))


        return self.inner_frame
    
    def view_course_center_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=15, sticky='nsew')

        label = customtkinter.CTkLabel(self.center_frame,text="View Course Scheme", font=('calibari', 30,'bold'))
        label.grid(row=0, column=1)

        conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        self.treeview = ttk.Treeview(self.center_frame,columns=["Subject_ID","Subject","Class","Teacher"], show="headings", height=35)
        self.treeview.grid(row=1, column=1, sticky="nsew")
        col_names = ["Subject_ID","Subject","Class","Teacher"]
        col_width = [70,100,70,100]

        for col, col_width in zip(col_names,col_width):
            self.treeview.column(col, width=col_width, anchor='center')
            self.treeview.heading(col, text=col, anchor='center')

        for row in data:
            self.treeview.insert("",'end', values=row)

        return self.center_frame
    
    def add_course(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root,corner_radius=10)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=15, sticky='nsew')
        label = customtkinter.CTkLabel(self.center_frame, text="Add new Course Scheme", font=('calibari',30, 'bold'))
        label.grid(row=0, column=1)
        sub_id_label = customtkinter.CTkLabel(self.center_frame, text="Subject ID")
        sub_id_label.grid(row=1, column=0, sticky="w")
        self.subject_id_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Subject ID')
        self.subject_id_entry.grid(row=1, column=1, sticky='nsew', padx=20, pady=(10, 5))
        sub_label = customtkinter.CTkLabel(self.center_frame, text="Subject")
        sub_label.grid(row=2, column=0, sticky="w")
        self.subject_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Subject')
        self.subject_entry.grid(row=2, column=1, sticky='nsew', padx=20, pady=(10, 5))
        class_label = customtkinter.CTkLabel(self.center_frame, text="Class")
        class_label.grid(row=3, column=0, sticky="w")
        self.class_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Class')
        self.class_entry.grid(row=3, column=1, sticky='nsew', padx=20, pady=(10, 5))
        teacher_label = customtkinter.CTkLabel(self.center_frame, text="Teacher name")
        teacher_label.grid(row=4, column=0, sticky='w')
        self.teacher_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Teacher name')
        self.teacher_entry.grid(row=4, column=1, sticky='nsew', padx=20, pady=(10, 5))
        button = customtkinter.CTkButton(self.center_frame, text="Submit", command=self.add_course_db)
        button.grid(row=5, column=1, sticky='nsew', padx=20, pady=(10, 5))

    def add_course_db(self):
        id = self.subject_id_entry.get()
        subject = self.subject_entry.get()
        cls = self.class_entry.get()
        teacher = self.teacher_entry.get()
        
        if self.subject_id_entry.get()=="" or self.subject_entry.get()=="" or self.class_entry.get()=="" or self.teacher_entry.get()=="":
            messagebox.showerror("ERROR", "Do not leave any field empty")
        try:
            conn = mysql.connector.connect(host="localhost", username="root",password="Azhar123@",database="mips_sms")
            cursor = conn.cursor()
            query = "INSERT INTO course (subject_id, subject, class, teacher) VALUES (%s,%s,%s,%s)"
            values = (id,subject, cls,teacher)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Information","Data added successfully")
        except Exception as err:
            messagebox.showerror("Error",f"Oops! there is an error: {err}")
            cursor.close()
        finally:
            if conn:
               conn.close()

    def update_delete_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.center_frame.columnconfigure(1, weight=1)
        self.center_frame.grid(row=0, column=1,rowspan=15, sticky='nsew')
        label = customtkinter.CTkLabel(self.center_frame, text="Update / Delete Course Scheme", font=('calibari',30, 'bold'))
        label.grid(row=0, column=1)
        self.subject_id_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Subject ID')
        self.subject_id_entry.grid(row=1, column=1, sticky='nsew', padx=20, pady=(10, 5))
        self.subject_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Subject')
        self.subject_entry.grid(row=2, column=1, sticky='nsew', padx=20, pady=(10, 5))
        self.class_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Class')
        self.class_entry.grid(row=3, column=1, sticky='nsew', padx=20, pady=(10, 5))
        self.teacher_entry = customtkinter.CTkEntry(self.center_frame, placeholder_text='Teacher')
        self.teacher_entry.grid(row=4, column=1, sticky='nsew', padx=20, pady=(10, 5))
        update_button = customtkinter.CTkButton(self.center_frame,text="Update record", command=self.update_course_db)
        update_button.grid(row=5, column=1, sticky='nsew', padx=20, pady=(10, 5))
        delete_button = customtkinter.CTkButton(self.center_frame,text="Delete record",command=self.ask_for_delete)
        delete_button.grid(row=6, column=1, sticky='nsew', padx=20, pady=(10, 5))
        conn = mysql.connector.connect(host="localhost",username='root',password="Azhar123@",database="mips_sms")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM course")
        data  = cursor.fetchall()
        cursor.close()
        conn.close()

        self.treeview = ttk.Treeview(self.center_frame,columns=["Subject_ID","Subject","Class","Teacher"], show='headings')
        self.treeview.grid(row=7, column=1, sticky='nsew')

        col_names = ["Subject_ID","Subject","Class","Teacher"]
        col_width = [70, 100,70, 100]

        for col, col_width in zip(col_names, col_width):
            self.treeview.column(col,width=col_width, anchor='center')
            self.treeview.heading(col, text=col, anchor='center')

        for row in data:
            self.treeview.insert("",'end',values=row)

            self.treeview.bind("<<TreeviewSelect>>", self.select)
    def select(self, event):
        self.subject_id_entry.delete(0, 'end')
        self.subject_entry.delete(0,'end')
        self.class_entry.delete(0,'end')
        self.teacher_entry.delete(0,'end')

        selected_record = self.treeview.focus()
        value = self.treeview.item(selected_record,'values')

        self.subject_id_entry.insert(0, value[0])
        self.subject_entry.insert(0,value[1])
        self.class_entry.insert(0,value[2])
        self.teacher_entry.insert(0,value[3])

        self.treeview.bind("<<ButtonRelease-1>>",selected_record)

    def ask_for_delete(self):
        selected_record = self.treeview.selection()
        if selected_record:
            confirm = messagebox.askquestion("Confirmtion","Are you sure you want to delete this record ?")
            if confirm=='yes':
                selected_item = self.treeview.item(selected_record)['values']
                self.treeview.delete(selected_record)
                self.delete_record(selected_item[0])

    def delete_record(self, record_id):
        try:
            conn = mysql.connector.connect(host="localhost",username="root",password="Azhar123@",database='mips_sms')
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM course WHERE subject_id={record_id}")
            conn.commit()
            messagebox.showinfo("Success","Record deleted successfully")
        except Exception as err:
            cursor.close()
            messagebox.showerror("Error",f"Oops! there is an error {err}")
        finally:
            if conn:
                conn.close()

    def update_course_db(self):
        subject_id = self.subject_id_entry.get()
        subject = self.subject_entry.get()
        cls = self.class_entry.get()
        teacher = self.teacher_entry.get()
        try:
            conn = mysql.connector.connect(host="localhost", username="root",password="Azhar123@",database="mips_sms")
            cursor = conn.cursor()
            values = (subject,cls,teacher,subject_id)
            query = "UPDATE course SET subject=%s, class=%s,teacher=%s WHERE subject_id=%s"
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success","Record updated successfully")
        except Exception as err:
            messagebox.showerror("Error",f"Oops! there is an error: {err}")
            cursor.close()
        finally:
            if conn:
                conn.close()
        
        
