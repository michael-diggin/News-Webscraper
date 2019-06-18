# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:22:45 2019

@author: md705
"""


import tkinter as tk
#from tkinter import ttk
from tkinter.font import Font


import datetime 
from LinkButton import LinkButton


class Interface():
    
    def __init__(self, articles):
        self.w = '400'
        self.h = '450'
        self.root = tk.Tk()
        self.root.geometry(f"{self.w}x{self.h}")        
        
        self.frame = tk.Frame(master=self.root, bg='LightBlue')
        self.frame.pack_propagate(0)
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.frame.configure(background='LightBlue')
        
        self.articles = articles
        self.title = ''
        self.site = ''
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.font = Font(family="Arial", size=10)       
        
        
        
    def display_interface(self):
        
        self.root.title(self.title)  
        
        #Display News source and date        
        t_label = tk.Label(text=f"{self.site.upper()} TOP STORIES", font=self.font)
        t_label.place(x=5, y=5, height=30, width=130)
        t_label.configure(background='LightBlue')
        d_label = tk.Label(text=self.date, font=self.font)
        d_label.place(x=200, y=5, height=30, width=100)
        d_label.configure(background='LightBlue')
        
        
        #include links to the articles
        #place them in order
        for i, headline in enumerate(self.articles):
            l = LinkButton(self.frame, text=headline, url=self.articles[headline])
            l.place(x=5, y=40+25*i)    
            
        #include a quit button
        Btn = tk.Button(master=self.frame, text="Exit", fg='red', command=self.root.destroy)
        Btn.place(x=175, y=400, height=25, width=50)
               
        self.root.mainloop()
        
        
     