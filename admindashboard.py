import customtkinter
import tkinter
from datetime import datetime
from time import strftime

from PIL import Image, ImageTk

from mips import Mips
from manage_teachers import ManageTeachers
from students import Students
from course import CourseScheme
from non_tching_staff import Non_Teaching_Staff



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")

class SchoolManagement(customtkinter.CTk):
    def __init__(self,root):
      self.root = root  
      #self.root.resizable(width=1, height=1)
      self.root.title("Modern Islamic Public School")
      self.root.geometry(f"{1300}x{880}")
      self.root.grid_rowconfigure(0, weight=1)
      self.theme = "green"
     
      self.center_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
      self.root.grid_columnconfigure(0, weight=0)
      self.sidebar_right_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
      self.root.grid_columnconfigure(0, weight=0)
      self.inner_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
      self.root.grid_columnconfigure(1, weight=1)
   

      self.inner_frame.grid(row=0, column=3, rowspan=4, sticky="nsew")

      self.sidebar_right_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
      self.sidebar_right_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

      self.sidebar_right_frame.rowconfigure(6, weight=1) # configure row row.no=6, weight=1
#============================sidebar widgets================================================
      label = customtkinter.CTkLabel(self.sidebar_right_frame, text="Admin Dashboard",font=customtkinter.CTkFont(size=18, weight="bold"))
      label.grid(row=0, column=0, padx=20, pady=(20,10))
      self.button_one = customtkinter.CTkButton(self.sidebar_right_frame, text="M.I.P.S", command=self.button_event_zero)
      self.button_one.grid(row=1, column=0, padx=20, pady=(20,10))
      self.button_one = customtkinter.CTkButton(self.sidebar_right_frame, text="Manaege Teachers", command=self.button_event_one)
      self.button_one.grid(row=2, column=0, padx=20, pady=(20,10))
      self.button_two = customtkinter.CTkButton(self.sidebar_right_frame, text="Manage Students", command=self.button_event_two)
      self.button_two.grid(row=3, column=0, padx=20, pady=(20,10))
      self.button_three = customtkinter.CTkButton(self.sidebar_right_frame, text="Course Scheme", command=self.button_event_three)
      self.button_three.grid(row=4, column=0, padx=20, pady=(20,10))
      '''self.button_four = customtkinter.CTkButton(self.sidebar_right_frame, text="Manage Classes", command=self.button_event_four)
      self.button_four.grid(row=5, column=0, padx=20, pady=(20,10))'''
      self.button_six = customtkinter.CTkButton(self.sidebar_right_frame, text="Non-Teaching staff", command=self.button_event_six)
      self.button_six.grid(row=5, column=0, padx=20, pady=(20,10))
      appearance_mode = customtkinter.CTkOptionMenu(self.sidebar_right_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
      appearance_mode.grid(row=6, column=0,padx=20, pady=(20,10))
      appearance_mode.set("Change Theme")
      


      mip = Mips(self.root, self.center_frame, self.inner_frame)
      self.center_frame = mip.mips_center_frame()
      self.center_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
      self.inner_frame = mip.show()
      self.inner_frame.grid(row=0, column=3,sticky="nsew")


    def button_event_zero(self):
      mip = Mips(self.root, self.center_frame, self.inner_frame)
      self.center_frame = mip.mips_center_frame()
      self.center_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
      self.inner_frame = mip.show()
      self.inner_frame.grid(row=0, column=3,sticky="nsew")
      print("Button 0 clicked")

    def button_event_one(self):
       mt = ManageTeachers(self.root, self.inner_frame, self.center_frame)
       self.inner_frame = mt.teacher_sidebar_frame()
       self.inner_frame.grid(row=0,column=2, rowspan=4, sticky='nsew')
       self.center_frame = mt.view_teachers()
       self.center_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')

    def button_event_two(self):
       stds = Students(self.root,self.center_frame, self.inner_frame)
       self.inner_frame = stds.view_options()
       self.inner_frame.grid(row=0, column=2, rowspan=4, sticky='nsew')
       self.center_frame = stds.view_students()
       self.center_frame.grid(row=0, column=1, rowspan=4, sticky='nsew')
       print("Button 2 clicked") 

    def button_event_three(self):
       course = CourseScheme(self.root, self.center_frame, self.inner_frame)
       self.inner_frame = course.course_scheme_sidebar_frame()
       self.inner_frame.grid(row=0, column=2, rowspan=4, sticky='nsew')
       self.center_frame = course.view_course_center_frame()
       self.center_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
       print("Button 3 clicked")

    '''def button_event_four(self):
       print("Button 4 clicked")'''

    def button_event_six(self):
       nts = Non_Teaching_Staff(self.root, self.center_frame, self.inner_frame)
       self.inner_frame = nts.view_options()
       self.inner_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
       self.center_frame = nts.view_employees()
       self.center_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
       print("Button 5 clicked")

    def change_appearance_mode_event(self, new_appearance_mode : str):
       customtkinter.set_appearance_mode(new_appearance_mode)
       self.theme = new_appearance_mode
       print("Button 7 clicked")


    def date_time(self):
       now = datetime.now()
       self.date_format = now.strftime("%D-%M-%Y")
       self.time_format = now.strftime("%H-%M-%S")
       

       self.date_label.configure(text=""+self.date_format)
       self.time_label.configure(text=""+self.time_format)

       self.after(1000, self.date_time)



'''if __name__=='__main__':
    root = customtkinter.CTk()
    app = SchoolManagement(root)
    root.mainloop()'''