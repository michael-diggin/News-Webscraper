# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:31:36 2019

@author: md705
"""

from bs4 import BeautifulSoup
import requests

class WebScrape():
#class to scrape news website for top stories 
#returns a dictionary of titles and links
    
    def __init__(self):
        self.url = ''
        self.article_tag = ''
        self.related_tag = ''
        self.website = ''
        
    def top_stories(self):
        page = requests.get(self.url)
        data = page.text
        soup = BeautifulSoup(data, 'html.parser')
        
        content = soup.find('div', {"class": self.article_tag})
        
        #sometimes the first headline has 2/3 related links to other closely related articles
        related = soup.find('div', {"class": self.related_tag})        
        try:
            related_links = []  
            for link in related.find_all('a'):
                if not self.website + link.get('href') in related_links:
                    related_links.append(self.website + link.get('href'))
        except: 
            related_links = []
            
        weblinks = []

        #list of links to articles        
        try:
            for link in content.find_all('a'):
                if not self.website + link.get('href') in weblinks:
                    if not self.website + link.get('href') in related_links:
                        weblinks.append(self.website + link.get('href'))
        except:
            print("Error: Cannot find the links")
        
        #this is currently specific to bbc news           
        for link in weblinks:
            if not link[-1] in '0123456789':
                weblinks.remove(link)
                
        #grab the titles
        titles = []
        for title in content.find_all('h3'):
            if not title.text in titles:
                titles.append(title.text)
                
        #return a dictionary of the headlines and links            
        articles = dict(zip(titles, weblinks))
        return articles
        
    














