import customtkinter as ctk
import pywinstyles
from PIL import Image
'''
root = ctk.CTk()
root.grid_columnconfigure(0, weight= 1)
frame = ctk.CTkFrame(root)
frame.grid(row=0, column=0, sticky= 'nsew')
image_label = ctk.CTkLabel(frame, text= 'Image goes here', height= 300, fg_color= 'dark blue', text_color= 'red',
                           font= ('Times New Roman',50))
image_label.grid(row= 0, column= 0, columnspan= 2, sticky= 's')
image_label2 = ctk.CTkLabel(frame, text= 'Image goes here', height= 200, bg_color= '#12af23',text_color= 'pink',
                           font= ('Times New Roman',50))
pywinstyles.set_opacity(image_label2, color= '#12af23')
image_label2.grid(row= 0, column= 0, columnspan= 2, sticky= 's')

root.mainloop()'''

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight= 1)
        self.home()
    def home(self):
        self.frame = ctk.CTkFrame(self, fg_color= 'white', corner_radius= 20)
        self.frame.grid(row=0, column=0, sticky= 'nsew')
        self.frame.grid_rowconfigure(0, weight= 1)
        self.frame.grid_columnconfigure(0, weight= 1)
        self.image_label = ctk.CTkLabel(self.frame, text= 'Image goes here', height= 300, fg_color= 'dark blue', text_color= 'red',
                                   font= ('Times New Roman',50), compound= 'center',
                                        image= ctk.CTkImage(Image.open('./gray/1.jpg'), size= (300,300)))
        self.image_label.grid(row= 0, column= 0, columnspan= 2, sticky= 's')
        self.img = ctk.CTkImage(Image.new(size= (2,2), color= '#123456', mode= 'RGB'), size= (2,2))
        self.image_label2 = ctk.CTkLabel(self.frame, text= 'Image goes here', height= 200, bg_color= '#12af23',text_color= 'pink',
                                   font= ('Times New Roman',50), anchor= 's', image= self.img, compound= 'left')
        pywinstyles.set_opacity(self.image_label2, color= '#12af23')
        self.image_label2.grid(row= 0, column= 0, columnspan= 2, sticky= 's')

test = App()
test.mainloop()











