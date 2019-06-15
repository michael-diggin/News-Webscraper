# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:22:45 2019

@author: md705
"""

from functools import partial
import tkinter as tk
import webbrowser
from tkHyperlinkManager import HyperlinkManager
import datetime 

class Interface():
    
    def __init__(self, articles):
        self.root = tk.Tk()
        self.articles = articles
        self.title = ''
        self.site = ''
        self.date = datetime.datetime.now().strftime("%d-%m-%Y")
        self.text = tk.Text()
        self.text.pack()
        self.hyperlink = HyperlinkManager(self.text)
        
        
    def display_interface(self):
        
        self.root.title(self.title)
        
        self.text.insert(tk.INSERT, self.site.upper() + " TOP STORIES \n")
        self.text.insert(tk.INSERT, self.date)
        self.text.insert(tk.INSERT, "\n")
        self.text.insert(tk.INSERT, "\n")       
        
        
        
        #include a quit button
        Btn = tk.Button(self.root, text="Exit", command=self.root.destroy)
        Btn.pack()
        
        #include links to the articles
        for headline in self.articles:
            self.text.insert(tk.INSERT, headline, self.hyperlink.add(partial(webbrowser.open, self.articles[headline])))
            self.text.insert(tk.INSERT, "\n")
        
        
        
        self.root.mainloop()
        
        
     