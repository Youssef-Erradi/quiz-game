# encoding:utf-8
import tkinter as tk
import customtkinter as ctk
from os import walk
from gui.UserWindow import UserWindow

class QuizChoiceWindow(ctk.CTk):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.resizable(False, False)
        self.title("Choisissez un quiz")
        for index,filename in enumerate(next(walk("../topics/"), (None, None, []))[2]) :
            ctk.CTkButton(master=self, text=filename.split(".")[0],
                                corner_radius=8, command=lambda filename=filename : self._choice(filename)).place(
                                    relx=0.5, y=35+(50*index), anchor=tk.CENTER)
        else:
            window_width = 300
            window_height = 65*index
            margin_x = int((self.winfo_screenwidth()/2) - (window_width/2))
            margin_y = int((self.winfo_screenheight()/2) - (window_height/2))
            self.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
    
    def _choice(self, filename):
        self.destroy()
        UserWindow(self.user, filename)        
