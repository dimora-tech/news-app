import customtkinter as ctk
import os
from PIL import Image

font = ('Helvetica', 20, 'normal', 'roman', 'underline')
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}")

        # set grid layout 1x2
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        '''
        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "ctk_logo_single.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
        '''
        self.title_frame = ctk.CTkFrame(self, corner_radius=0, fg_color= 'grey', height= 40)
        self.title_frame.grid(row=0, column= 0,sticky= 'nsew')
        self.title = ctk.CTkLabel(self.title_frame, text= "360News")
        self.title.grid(row= 0, column= 0, sticky= 'nsew')
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0, fg_color= 'grey')
        self.navigation_frame.grid(row=1, column=0, sticky="new")
        #self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Image Example", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color= 'dark red', command=self.home_button_event)
        self.home_button.grid(row=0, column=1, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Business",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color='dark red', command=self.frame_2_button_event)
        self.frame_2_button.grid(row=0, column=2, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Entertainment",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color='dark red', command=self.frame_3_button_event)
        self.frame_3_button.grid(row=0, column=3, sticky="ew")


        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame, values=["System", "Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        #self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="360News")
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = ctk.CTkButton(self.home_frame, text="CTkButton",  compound="right")
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = ctk.CTkButton(self.home_frame, text="CTkButton",  compound="top")
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = ctk.CTkButton(self.home_frame, text="CTkButton",  compound="bottom")
        self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = ctk.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(font=('Helvetica', 20, 'normal', 'roman', 'underline') if name == "home" else ('Helvetica', 20))
        self.frame_2_button.configure(font=('Helvetica', 20, 'normal', 'roman', 'underline') if name == "frame_2" else ('Helvetica', 20))
        self.frame_3_button.configure(font=('Helvetica', 20, 'normal', 'roman', 'underline') if name == "frame_3" else ('Helvetica', 20))

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=2, column=0, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
