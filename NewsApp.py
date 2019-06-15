# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:05:37 2019

@author: md705
"""

from WebScrape import WebScrape
from Interface import Interface

bbc = WebScrape()
bbc.url = 'https://www.bbc.co.uk/news'
bbc.article_tag = 'gel-layout gel-layout--equal nw-c-top-stories--standard nw-c-top-stories--domestic'
bbc.related_tag = 'nw-c-top-stories-primary__related-content gs-u-pb-alt@m gs-u-pb0@l'
bbc.website = 'https://www.bbc.co.uk'
articles = bbc.top_stories()

ui = Interface(articles)
ui.title = 'Top Stories'
ui.site = 'BBC'

ui.display_interface()