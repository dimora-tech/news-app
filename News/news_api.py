from newsapi import NewsApiClient
import sqlite3

api = NewsApiClient(api_key = 'ee8bf12415554b0f863fe566fce1afc0')
categories = ('Entertainment', 'Business', 'Sports', 'Science', 'General', 'Health', 'Technology')
news = {}

test = api.get_top_headlines(category= 'entertainment', page_size= 5, page= 1)
print(test['articles'])

for category in categories:
    head = api.get_top_headlines(category= category.lower(), page_size= 20)
    articles = head['articles']
    with sqlite3.connect('NewsDB.db') as conn:
        cur = conn.cursor()
        cur.execute(('''CREATE TABLE IF NOT EXISTS %s
                    (%s TEXT,
                     %s TEXT,
                     %s TEXT,
                     %s TEXT,
                     %s BLOB,
                     %s BLOB,
                     %s TEXT,
                     %s TEXT,
                     FOREIGN KEY(Source) REFERENCES Sources(Source)
                    )''' %((category,) + tuple(articles[0].keys()))).title()
                   )
        cur.execute('CREATE TABLE IF NOT EXISTS Sources (Source TEXT, Source_Name TEXT, PRIMARY KEY(Source))')
        for article in articles:
            cur.execute('INSERT INTO %s VALUES (?,?,?,?,?,?,?,?)' %category, ((article['source']['id'],) + tuple(article.values())[1:])
                        )
            try: cur.execute('INSERT INTO Sources VALUES (?,?)', tuple(article['source'].values()))
            except sqlite3.IntegrityError: pass
        #news[category] = head['articles']
        

    #sleep()
"""
conn = sqlite3.connect('NewsDB.db')
cur = conn.cursor()
cur.execute('DROP TABLE NEWS')
cur.execute('''CREATE TABLE IF NOT EXISTS News(
                %s TEXT,
                %s TEXT,
                %s TEXT,
                %s TEXT,
                %s TEXT,
                %s TEXT,
                %s TEXT)''' %(category_.title() for category_ in categories))

for i in range(20):
    news_tuple = tuple(value[i] for value in news.values())
    cur.execute('INSERT INTO News VALUES (%s, %s, %s, %s, %s, %s'
        
    
    cur.execute('INSERT INTO News'



#evr = api.get_everything()
#src = api.get_sources()
#categories = set(source['category'] for source in src['sources'])
print(news)
#for i in categories: print(i)


import customtkinter as ctk

app = ctk.CTk()
app.grid_columnconfigure(0, weight= 1)
tabview = ctk.CTkTabview(app, segmented_button_selected_color= 'red', text_color_disabled= 'red')

tabview.grid(row= 0, column= 0, sticky= 'ns')

tabview.add('tab 1')
tabview.add('tab 2')

app.mainloop()
"""
