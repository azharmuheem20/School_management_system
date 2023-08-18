import customtkinter
from datetime import datetime
from time import strftime
from PIL import Image
from tkinter import messagebox


class Mips:
    def __init__(self,root,center_frame, inner_frame):
        self.root = root
        self.center_frame = center_frame
        self.inner_frame = inner_frame
        
    def show(self):
        self.inner_frame.destroy()
        self.inner_frame = customtkinter.CTkFrame(self.root, corner_radius=10)
        self.time_label = customtkinter.CTkLabel(self.inner_frame,font=customtkinter.CTkFont(size=21, weight="bold"))
        self.time_label.grid(row=1, column=0, padx=15, pady=(20,10))

        self.time_update()
        return self.inner_frame
    def mips_center_frame(self):
        self.center_frame.destroy()
        self.center_frame = customtkinter.CTkFrame(self.root)
        self.center_frame.columnconfigure(1,weight=1)
        self.center_frame.grid(row=0, column=1, rowspan=15, sticky="nsew")
        name_label = customtkinter.CTkLabel(self.center_frame, text="Modern Islamic Public School",font=customtkinter.CTkFont(size=32, weight="bold"))
        name_label.grid(row=0, column=1)
        moto_label = customtkinter.CTkLabel(self.center_frame,text_color="Green",text="Educating the mind, without educating the Heart, is no education at all. \n(Aristotle)", font=('calibri',20))
        moto_label.grid(row=1, column=1)

        try:
            photo = customtkinter.CTkImage(light_image=Image.open("E:\Vivo Y91C\Pics\CamScanner\school logo.jpg"),size=(970,640)) #copy image path from file
            photo_label = customtkinter.CTkLabel(self.center_frame, image=photo) #grid image
            photo_label.grid(row=2, column=1)
        except Exception as err:
            messagebox.showerror("Error",f"{err}")
        
        return self.center_frame


    def time_update(self):
        time_string = strftime('%H:%M:%S %p \n %A \n %B %d,%Y')
        self.time_label.configure(text=time_string)
        self.time_label.after(1000, self.time_update)