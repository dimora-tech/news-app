import customtkinter as ctk
#from customtkinter import *
from time import sleep

def submit_func():
    notif_label.configure(text= 'Submitted Successfully')

ctk.set_appearance_mode('Light')
ctk.set_default_color_theme('blue')

root = ctk.CTk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('500x700')
#root.icon_bitmap()
#root.grid_columnconfigure(1, weight= 1)
root.grid_columnconfigure(1, weight= 1)
image_label = ctk.CTkLabel(root, text= 'Image goes here', height= 300, fg_color= 'dark blue', text_color= 'white',
                           font= ('Times New Roman',50))
image_label.grid(row= 0, column= 0, columnspan= 2, sticky= 'nsew')
name_label = ctk.CTkLabel(root, text= 'Name:', fg_color= 'transparent', text_color= 'dark blue',
                          font= ('Times New Roman',25), height = 30, corner_radius= 10)
name_label.grid(row= 1, column= 0, padx= 20, pady= 30, sticky= 'nw')
name_entry = ctk.CTkEntry(root, placeholder_text= 'Enter Name')
name_entry.grid(row= 1, column= 1, padx= 20, pady= 30, sticky= 'ew')
email_label = ctk.CTkLabel(root, text= 'Email:', fg_color= 'transparent', text_color= 'dark blue',
                          font= ('Times New Roman',25), height = 30, corner_radius= 10)
email_label.grid(row= 2, column= 0, padx= 20, pady= 10, sticky= 'nw')
email_entry = ctk.CTkEntry(root, placeholder_text= 'Enter Name')
email_entry.grid(row= 2, column= 1, padx= 20, pady= 10, sticky= 'ew')
submit_btn = ctk.CTkButton(root, text= 'Submit', font= ('Times New Roman',25), fg_color= 'dark blue',
                           command= submit_func)
submit_btn.grid(row= 3, column= 1, pady= 50, sticky= 'ns')
notif_label = ctk.CTkLabel(root, text= '', fg_color= 'transparent', text_color= 'dark blue',
                          font= ('Times New Roman',25), height = 30)
notif_label.grid(row= 4, column= 1, sticky= 'ns')

class FormApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('500x700')
        self.submit_btn = ctk.CTkButton(self, text= 'Submit', font= ('Times New Roman',25), fg_color= 'dark blue',
                           command= self.submit_func)
        self.submit_btn.grid(row= 3, column= 1, pady= 50, sticky= 'ns')

    def submit_func(self):
        self.notif_label.configure(text= 'Submitted Successfully')

app = FormApp()
app.mainloop()
