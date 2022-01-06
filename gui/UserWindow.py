# encoding:utf-8
import tkinter as tk
import random as rd
import time as tm
from tkinter import messagebox
import customtkinter as ctk

class UserWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._basic_config()
        self.data = []
        self.index = 0
        self.options = []
        self.answers = []
        self._create_components()
    
    def _basic_config(self):
        self.title("Authentification")
        self.resizable(False, False)
        window_width = 500
        window_height = 300
        margin_x = int((self.winfo_screenwidth()/2) - (window_width/2))
        margin_y = int((self.winfo_screenheight()/2) - (window_height/2))
        self.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
    
    def _create_components(self):
        self.lbl_question = ctk.CTkLabel(self, text="", width=450, height=50)
        self.lbl_question.place(x=25, y=10)
        
        for i in range(4) :
            check_box = ctk.CTkCheckBox(master=self, text="")
            check_box.function = lambda check_box=check_box : self._check(check_box)
            check_box.place(x=170, y=90+(i*30))
            self.options.append(check_box)
        
        self.btn_previous = ctk.CTkButton(master=self, text="<", width=50, command=self._previous)
        self.btn_previous.place(x=40, y=250)
        
        self.btn_submit = ctk.CTkButton(master=self, text="Submit", command=self._submit)
        self.btn_submit.place(x=120, y=250)
        
        self.btn_clear = ctk.CTkButton(master=self, text="Clear", state=tk.DISABLED, hover=False, command=self._clear)
        self.btn_clear.place(x=260, y=250)
        
        self.btn_next = ctk.CTkButton(master=self, text=">", width=50, command=self._next)
        self.btn_next.place(x=400, y=250)
        
        if len(self.data) == 0:
            self._load_data()
            for _ in self.data:
                self.answers.append(None)
        
        self._setup_components()
        
    def _setup_components(self):
        if self.index == -1 : return
        json = self.data[self.index]
        self.lbl_question.text_label["text"] = json["question"]
        if self.answers[self.index] is None :
            self.btn_clear.configure(state=tk.DISABLED)
        else :
            self.btn_clear.configure(state=tk.NORMAL)
            
        
        for index,option in enumerate(json["options"]):
            self.options[index].set_text(option)
            self.options[index].check_state = self.answers[self.index] == option
            self.options[index].on_leave()
        self.update()
       
    def _next(self):
        if self.index < len(self.data)-1:
            self.index += 1
            self._setup_components()
            self._verify_btns()
            
    def _previous(self):
        if self.index > 0:
            self.index -= 1
            self._setup_components()
            self._verify_btns()
    
    def _verify_btns(self):
        self.btn_previous.set_state(tk.NORMAL) 
        self.btn_next.set_state(tk.NORMAL) 
        if self.index == 0  :
            self.btn_previous.set_state(tk.DISABLED) 
        if self.index == len(self.data)-1 :
            self.btn_next.set_state(tk.DISABLED) 
    
    def _check(self,check_box):
        for option in self.options:
            option.check_state = check_box.text == option.text
            option.on_leave()
        self.answers[self.index] = check_box.text
        self.btn_clear.configure(state=tk.NORMAL)
    
    def _clear(self):
        for option in self.options:
            option.check_state = False
            option.on_leave()
        self.answers[self.index] = None
        self.btn_clear.configure(state=tk.DISABLED)
    
    def _submit(self):
        print(self.data[self.index]["question"], self.answers[self.index])
    
    def _load_data(self):
        with open(file="../topics/python.json") as file :
            temp = ""
            for line in file.readlines():
                temp += line.strip()
            temp = eval(temp)
            rd.shuffle(temp)
            self.data = temp

if __name__ == '__main__':
    ctk.set_appearance_mode("Dark")
    UserWindow()
    tk.mainloop()