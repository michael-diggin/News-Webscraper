# original from http://code.activestate.com/recipes/580774-tkinter-link-or-hyperlink-button/
#I've altered it to suit my needs

from tkinter import Label
from tkinter.font import Font
import webbrowser


class LinkButton(Label, object):
    
    def __init__(self, master, text, url, background='LightBlue', font=None, visited_fg = "#551A8B", normal_fg = "#0000EE", visited=False):
        
        self._visited_fg = visited_fg
        self._normal_fg = normal_fg
        self.url = url
        if visited:
            fg = self._visited_fg
        else:
            fg = self._normal_fg

        if font is None:
            font = Font(family="Arial", size=10, underline=True)
        
        #set up the label
        Label.__init__(self, master, text=text, fg=fg, cursor="hand2", font=font)   

        self._visited = visited
        self.configure(background=background)
        
        #make the label into a link
        self.bind("<Button-1>", self._on_click)

    @property
    def visited(self):
        return self._visited
        
    @visited.setter
    def visited(self, is_visited):
        if is_visited:
            self.configure(fg=self._visited_fg)
            self._visited = True
        else:
            self.configure(fg=self._normal_fg)
            self._visited = False

    #open the link in a new tab
    def _on_click(self, event):
        if not self._visited:
            self.configure(fg=self._visited_fg)

        self._visited = True       
        webbrowser.open_new(self.url) 
