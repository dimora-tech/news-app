from urllib import request
import customtkinter as ctk
from tkhtmlview import HTMLLabel
import requests
import time
from PIL import Image 
import os
import sys
from tkinter import PhotoImage, Label
import pywinstyles
#from newsapi import NewsApiClient
import sqlite3
#import pycountry

#api = NewsApiClient(api_key = 'ee8bf12415554b0f863fe566fce1afc0')
categories = ['entertainment', 'business', 'sports', 'science', 'general', 'health', 'technology']
news_text = "This endpoint returns the subset of news publishers that top headlines (/v2/top-headlines) are available from. It's mainly a convenience endpoint that you can use to keep track of the publishers available on the API, and you can pipe it straight through to your users."
ctk.set_appearance_mode('Light')

#Frames Default Settings
nav_frame = {'font': ('Georgia',20), 'fg_color': 'transparent', 'hover_color': 'dark red', 'text_color': 'black', 'padx': 10, 'width': 100}
news_frame = {'fontL': ('Georgia',15),'fontB': ('Georgia',18, 'bold', 'roman', 'underline'), 'fg_color': ('dark red','white'), 'hover_color': 'white', 'text_colorB': 'dark red','text_colorL': 'black'}
home_frame = {}
trend_frame = {}
newscard_frame = {}

x = -1

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('25News')
        self.width_ = self.winfo_screenwidth()
        self.height_ = self.winfo_screenheight()
        self.geometry(f"{self.width_}x{self.height_}")
        self.grid_rowconfigure(2, weight= 1)
        self.grid_columnconfigure(0, weight= 1)

        #Title Frame
        self.title_frame = ctk.CTkFrame(self, height= 100, fg_color = 'white', corner_radius= 0)
        self.title_frame.grid(row= 0, column= 0, sticky= 'nsew')
        self.title_frame.grid_rowconfigure(0, weight= 1)
        self.title_button = ctk.CTkButton(self.title_frame, text= '25News', height= 50, text_color= 'dark red',
                                        font= ('Helvetica',35, 'bold'), fg_color= 'transparent',
                                        hover_color= 'white', corner_radius= 0, command= self.home)
        self.title_button.grid(row= 0, column= 0, padx= 10, sticky= 'n')

        #Navigation Frame
        self.nav_frame = ctk.CTkFrame(self, height= 50, fg_color = 'white', corner_radius= 0)
        self.nav_frame.grid(row= 1, column= 0, sticky= 'nsew')
        self.nav_frame.grid_columnconfigure(0, weight= 1)
        self.nav_frame.grid_columnconfigure(1, weight= 1)
        self.nav_frame.grid_columnconfigure(2, weight= 1)
        self.nav_frame.grid_columnconfigure(3, weight= 1)
        self.nav_frame.grid_columnconfigure(4, weight= 1)
        self.nav_frame.grid_columnconfigure(5, weight= 1)
        self.nav_frame.grid_columnconfigure(6, weight= 1)

        self.entertainment = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Entertainment', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Entertainment'))
        self.business = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Business', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Business'))
        self.sports = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Sports', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Sports'))
        self.science = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Science', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Science'))
        self.general = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'General', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('General'))
        self.health = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Health', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Health'))
        self.technology = ctk.CTkButton(self.nav_frame, fg_color = nav_frame['fg_color'],
                                                         text= 'Technology', text_color= nav_frame['text_color'],
                                                         font= nav_frame['font'], hover_color= nav_frame['hover_color'],
                                                         corner_radius= 0, width= nav_frame['width'], command= lambda: self.news('Technology'))
        self.entertainment.grid(row= 0, column= 0, padx= nav_frame['padx'], sticky= 'nsew')
        self.business.grid(row= 0, column= 1, padx= nav_frame['padx'], sticky= 'nsew')
        self.sports.grid(row= 0, column= 2, padx= nav_frame['padx'], sticky= 'nsew')
        self.science.grid(row= 0, column= 3, padx= nav_frame['padx'], sticky= 'nsew')
        self.general.grid(row= 0, column= 4, padx= nav_frame['padx'], sticky= 'nsew')
        self.health.grid(row= 0, column= 5, padx= nav_frame['padx'], sticky= 'nsew')
        self.technology.grid(row= 0, column= 6, padx= nav_frame['padx'], sticky= 'nsew')

        #Search Bar
        self.search_bar = ctk.CTkEntry(self.nav_frame, placeholder_text= "It's only news if you dont know about it",
                                       corner_radius= 15, width= 450, height= 30, font= nav_frame['font'])
        self.search_bar.grid(row= 0, column= 7, padx = 10, sticky= 's')
        
        # Bind click event to the root window to defocus the entry widget
        self.bind("<Button-1>", lambda event: event.widget.master.focus_set())

        #Loading Images
        self.img_list = os.listdir('./gray')[:10]
        self.text_list = ['A representative of the restaurant "Chika\'s Eatery" approaches you \
to design a system that will handle the orders made in the restaurant.',
                          'As an additional requirement, they would like a system where customers can create an account, \
fund the account and make orders from their wallet.']

        self.home()
        self.move()

    def move(self):
        #Change Pictures and Captions
        global x
        x = x+1
        self.timed_label.configure(image= ctk.CTkImage(Image.open('./gray/'+self.img_list[x%7]), size= (1000,300)))
        self.timed_label_text.configure(text= self.text_list[x%2])
        
        self.after(3000, self.move)

    def home(self):
        #Default Nav Tabs
        self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])

        #Home Frame
        self.home_frame = ctk.CTkScrollableFrame(self, corner_radius= 0, fg_color= 'white',
                                                 border_width= 1, border_color= 'white')
        self.home_frame.grid(row= 2, column= 0, sticky= 'nsew')
        self.home_frame.grid_rowconfigure(2, weight= 1)
        self.home_frame.grid_columnconfigure(1, weight= 1)
        self.space = ctk.CTkLabel(self.home_frame, text= '', fg_color= 'white', height= 5)
        self.space.grid(row=0, column=0, sticky= 'nsew')
        self.prev_button = ctk.CTkButton(self.home_frame, fg_color= 'transparent',
        command= self.previous_)
        #self.prev_button.grid(row= 1, column= 0, sticky= 'nsew')

        #Image Headlines
        self.timed_label_p = ctk.CTkLabel(self.home_frame, text= 'Image Goes Here', text_color= 'dark red',
                                          width= 1000, height= 300, font= news_frame['fontL'])
        self.timed_label_p.grid(row= 1, column= 0, sticky= 'nsew')
        self.timed_label = ctk.CTkLabel(self.home_frame, text= '', compound= 'center')
        self.timed_label.grid(row= 1, column= 0, sticky= 'nsew')
        self.timed_label_text = ctk.CTkLabel(self.home_frame, bg_color= 'black', height= 200,
                                   font= nav_frame['font'], text_color= 'white',anchor= 'sw',
                                             wraplength= 950)
        pywinstyles.set_opacity(self.timed_label_text, color= 'black')
        self.timed_label_text.grid(row=1, column=0, sticky= 'sew')
        self.next_button = ctk.CTkButton(self.home_frame, fg_color= 'transparent',
        command= self.next_)
        #self.next_button.grid(row= 1, column= 2, sticky= 'nsew')

        #Trending News Frame
        self.trending_frame = ctk.CTkFrame(self.home_frame, fg_color= 'white', height= 300)
        self.trending_frame.grid(row= 1, column= 1, sticky= 'nsew')
        self.trending_frame.grid_rowconfigure(0, weight= 1)
        self.trending_frame.grid_columnconfigure(0, weight= 1)

        self.trending_label = ctk.CTkLabel(self.trending_frame, text= 'Trending Now', text_color= 'dark red',
                                           fg_color= 'transparent', corner_radius= 0,
                                           height= 30, font= ('Georgia',18, 'bold'))
        self.trending_label.grid(row= 0, column= 0, padx= 20, rowspan= 2, sticky= 'nw')
        sq = ctk.CTkImage(Image.new(size= (5,5), color= '#8b0000', mode= 'RGB'), size= (8,13))       
        self.trend1 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend2 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend3 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend4 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend5 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend6 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend7 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend8 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend9 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')
        self.trend10 = ctk.CTkButton(self.trending_frame, fg_color = news_frame['fg_color'][1],
                                                         corner_radius= 0, width= nav_frame['width'], height= 27,
                                                         text_color= 'black', font= news_frame['fontL'],
                                                         text= 'This is a trending news', hover_color= 'white',
                                                         image= sq, compound= 'left', anchor= 'nsw')

        self.trend1.grid(row= 1, column= 0, padx= 23, sticky= 'nsw')
        self.trend2.grid(row= 2, column= 0, padx= 23, sticky= 'nsw')
        self.trend3.grid(row= 3, column= 0, padx= 23, sticky= 'nsw')
        self.trend4.grid(row= 4, column= 0, padx= 23, sticky= 'nsw')
        self.trend5.grid(row= 5, column= 0, padx= 23, sticky= 'nsw')
        self.trend6.grid(row= 6, column= 0, padx= 23, sticky= 'nsw')
        self.trend7.grid(row= 7, column= 0, padx= 23, sticky= 'nsw')
        self.trend8.grid(row= 8, column= 0, padx= 23, sticky= 'nsw')
        self.trend9.grid(row= 9, column= 0, padx= 23, sticky= 'nsw')
        self.trend10.grid(row= 10, column= 0, padx= 23, sticky= 'nsw')
        self.trend1.bind(sequence= '<Enter>', command= lambda x:self.trend1.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend2.bind(sequence= '<Enter>', command= lambda x:self.trend2.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend3.bind(sequence= '<Enter>', command= lambda x:self.trend3.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend4.bind(sequence= '<Enter>', command= lambda x:self.trend4.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend5.bind(sequence= '<Enter>', command= lambda x:self.trend5.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend6.bind(sequence= '<Enter>', command= lambda x:self.trend6.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend7.bind(sequence= '<Enter>', command= lambda x:self.trend7.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend8.bind(sequence= '<Enter>', command= lambda x:self.trend8.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend9.bind(sequence= '<Enter>', command= lambda x:self.trend9.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend10.bind(sequence= '<Enter>', command= lambda x:self.trend10.configure(font= ('Georgia',15,'normal','roman','underline'), text_color= 'dark red'))
        self.trend1.bind(sequence= '<Leave>', command= lambda y:self.trend1.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend2.bind(sequence= '<Leave>', command= lambda y:self.trend2.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend3.bind(sequence= '<Leave>', command= lambda y:self.trend3.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend4.bind(sequence= '<Leave>', command= lambda y:self.trend4.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend5.bind(sequence= '<Leave>', command= lambda y:self.trend5.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend6.bind(sequence= '<Leave>', command= lambda y:self.trend6.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend7.bind(sequence= '<Leave>', command= lambda y:self.trend7.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend8.bind(sequence= '<Leave>', command= lambda y:self.trend8.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend9.bind(sequence= '<Leave>', command= lambda y:self.trend9.configure(font= news_frame['fontL'], text_color= 'black'))
        self.trend10.bind(sequence= '<Leave>', command= lambda y:self.trend10.configure(font= news_frame['fontL'], text_color= 'black'))

        #News Cards
        self.newscard_frame = ctk.CTkFrame(self.home_frame, corner_radius= 0, fg_color= news_frame['fg_color'][1])
        self.newscard_frame.grid(row= 2, column= 0, columnspan= 2, pady= 30, sticky= 'nsew')
        row_ = i = 0
        while True:
            try:
                self.trending_cate = ctk.CTkLabel(self.newscard_frame, text= f'Trending in {categories[i]}'.title(),
                                                    fg_color= 'white', font= nav_frame['font'], text_color= 'dark red')
                self.trending_cate.grid(row= row_, column= 0, padx= 10, columnspan= 3, sticky= 'nsw')
                row_  += 1
                i += 1
                for col_ in range(3):
                    locals()[f'self.news_card{row_}{col_}'] = ctk.CTkFrame(self.newscard_frame, corner_radius= 0,
                                                                            fg_color= news_frame['fg_color'][1])
                    locals()[f'self.news_card{row_}{col_}'].grid(row= row_, column= col_, padx= 10, pady= 10, sticky= 'nsew')

                    locals()[f'self.news_card{row_}{col_}'].grid_rowconfigure(1, weight= 1)
                    locals()[f'self.news_card{row_}{col_}'].grid_columnconfigure(0, weight= 1)
                    locals()[f'self.news_card{row_}{col_}B'] = ctk.CTkButton(locals()[f'self.news_card{row_}{col_}'], fg_color = news_frame['fg_color'][0],
                                                                            corner_radius= 15, width= self.width_/3 -30, height= self.width_/5.5, anchor= 's',
                                                                            hover_color= 'dark red')
                    locals()[f'self.news_card{row_}{col_}B'].grid(row= 0, column= 0, sticky= 'nsew')
                    locals()[f'self.news_card{row_}{col_}L'] = ctk.CTkLabel(locals()[f'self.news_card{row_}{col_}'], fg_color = news_frame['fg_color'][1],
                                                                            text= 'News', text_color= news_frame['text_colorB'], anchor= 'w',
                                                                            font= news_frame['fontB'], corner_radius= 0, wraplength= self.width_-200)
                    locals()[f'self.news_card{row_}{col_}L'].grid(row= 1, column= 0, sticky= 'nsew')
                row_ += 1
            except: break
    def read_news(self):
        self.read_news_frame = ctk.CTkScrollableFrame(self, corner_radius= 0, fg_color= 'white',
                                                 border_width= 1, border_color= 'white')
        self.read_news_frame.grid(row= 2, column= 0, sticky= 'nsew')
        browser = HTMLLabel(self.read_news_frame)
        browser.pack(fill="both", expand=True)
        browser.set_html(requests.get('https://news.google.com/rss/articles/CBMipAFBVV95cUxQR1FyZkppbWdmbktCSDJabmNfbWJEeFlXSlFfMDJpTkdvbE1NLWRBRUdhNWdjVmY2Mmt4OGptMXpkVXlFQjkwZ3FOeXBpQW5MRlhXRWlQZ01hMEVOWVhJZXAwZ2xIRUlzeFhTUm0tZXhMcG5vZEZ4SXBSSzhGZVhtdEhGTERTVG5lNEpFSjFmT0JyMDFrRGh2bGxiclVxSV92X1FNONIBqgFBVV95cUxNQkk5MVFrZ2NDdmxYbHNxd0hpVGVvTzFXTF9pcHhIc1Fva0VfSVNwOGlXWDlxLUhCd2M2aWNDLXhFMnR6OExET25IeXpHV1BhOUpRM1NvcS05QTFmbWxJT2JLNjh0c3RxLVUzb2JTbVJGLWd6bkd5NUFsSzJZRGdVdEUycHFuQjFrVnhYb3VzQWQxZ0FkbmNpVzRFY1BncE1kd21UcUtpUXVhZw?oc=5').text)

    def previous_(self):
        global x
        x -= 1
        self.timed_label.configure(image= ctk.CTkImage(Image.open('./gray/'+self.img_list[x%6]), size= (1000,300)))
        self.timed_label_text.configure(text= self.text_list[x%2])

    def next_(self):
        global x
        x += 1
        self.timed_label.configure(image= ctk.CTkImage(Image.open('./gray/'+self.img_list[x%6]), size= (1000,300)))
        self.timed_label_text.configure(text= self.text_list[x%2])

    def news(self, category):
        with sqlite3.connect('NewsDB.db') as conn:
                cur = conn.cursor()
                cur.execute('SELECT * FROM %s' %category)
                _news = cur.fetchall()

        if category.lower() == 'entertainment': 
            self.entertainment.configure(text_color= 'white', fg_color= 'dark red')
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])

        elif category.lower() == 'business':    
            self.business.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
       
        elif category.lower() == 'sports':      
            self.sports.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        
        elif category.lower() == 'science':
            self.science.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        
        elif category.lower() == 'general':     
            self.general.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        
        elif category.lower() == 'health':      
            self.health.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.technology.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        
        elif category.lower() == 'technology':  
            self.technology.configure(text_color= 'white', fg_color= 'dark red')
            self.entertainment.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.business.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.sports.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.science.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.general.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
            self.health.configure(text_color= nav_frame['text_color'], fg_color= nav_frame['fg_color'])
        
        self.news_frame = ctk.CTkScrollableFrame(self, corner_radius= 0, fg_color= 'white',
                                                 border_width= 1, border_color= 'white')
        self.news_frame.grid(row= 2, column= 0, sticky= 'nsew')
        self.news_frame.grid_rowconfigure(15, weight= 1)
        self.news_frame.grid_columnconfigure(0, weight= 1)
        for i in range(10):
            locals()[f'self.news{i+1}'] = ctk.CTkFrame(self.news_frame, height= 200, corner_radius= 0,
                                                       fg_color= news_frame['fg_color'][1])
            locals()[f'self.news{i+1}'].grid(row= i, column= 0, columnspan= 3, pady= 10, sticky= 'nsew')
            locals()[f'self.news{i+1}'].grid_rowconfigure(1, weight= 1)
            locals()[f'self.news{i+1}'].grid_columnconfigure(1, weight= 1)
            locals()[f'self.news{i+1}B'] = ctk.CTkButton(locals()[f'self.news{i+1}'], fg_color = news_frame['fg_color'][0],
                                                         corner_radius= 0, width= nav_frame['width'], height= nav_frame['width'], anchor= 's')
            locals()[f'self.news{i+1}B'].grid(row= 0, column= 0, rowspan= 2, sticky= 'nsew')
            locals()[f'self.news{i+1}L1'] = ctk.CTkLabel(locals()[f'self.news{i+1}'], fg_color = news_frame['fg_color'][1],
                                                        text= _news[i][2], text_color= news_frame['text_colorB'], anchor= 'w',
                                                        font= news_frame['fontB'], corner_radius= 0, wraplength= self.width_-200)
            locals()[f'self.news{i+1}L1'].grid(row= 0, column= 1, padx= 25, sticky= 'nsw')
            locals()[f'self.news{i+1}L2'] = ctk.CTkLabel(locals()[f'self.news{i+1}'], fg_color = news_frame['fg_color'][1],
                                                        text= _news[i][1], text_color= news_frame['text_colorL'], anchor= 'w',
                                                        font= news_frame['fontL'], corner_radius= 0, wraplength= self.width_-200)
            locals()[f'self.news{i+1}L2'].grid(row= 1, column= 1, padx= 25, sticky= 'nw')

newsApp = App()
newsApp.mainloop()

'''
def home(self):
        self.home_frame = ctk.CTkScrollableFrame(self, corner_radius= 0, fg_color= 'white',
                                                 border_width= 1, border_color= 'white')
        self.home_frame.grid(row= 3, column= 0, sticky= 'nsew')
        self.home_frame.grid_rowconfigure(15, weight= 1)
        self.previous_btn = ctk.CTkButton(self.home_frame, text = '<', font = ('Georgia', 100), fg_color= 'transparent',
                                          command = self.previous)
        self.previous_btn.grid(row= 0, column = 0, sticky= 'nsew')
        self.timed_label = ctk.CTkLabel(self.home_frame, height= 300, width= 1000, wraplength= self.width_-400,
                                        text= 'Image goes here', text_color= 'red', fg_color= 'green', compound= 'top')
        self.timed_label.grid(row= 0, column= 1, sticky= 'nsew')
        self.image_label = ctk.CTkLabel(self.home_frame, text= 'Image goes here', height= 200, bg_color= '#12af23',text_color= 'pink',
                                   font= ('Times New Roman',nav_frame['width']))
        pywinstyles.set_opacity(self.timed_label, color= 'green')
        self.image_label.grid(row= 0, column= 1, sticky= 's')
        self.timed_label.grid(row= 0, column= 1, sticky= 'nsew')
        #pywinstyles.set_opacity(self.titled, color= '#12af23')
        #self.titled.grid(row= 0, column= 1, sticky= 'nsew')
        
        self.next_btn = ctk.CTkButton(self.home_frame, text = '>', font = ('Georgia', 100), fg_color= 'transparent',
                                      command= self.next)
        self.next_btn.grid(row= 0, column = 2, sticky= 'nsew')
'''
