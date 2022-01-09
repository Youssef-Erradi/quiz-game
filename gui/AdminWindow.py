# encoding:utf-8
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from os import walk

class AdminWindow(ctk.CTk):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.data = []
        self.btn_files = []
        self.options = []
        self.entries = []
        self._basic_config()
        self._create_components()
        self.mainloop()
    
    def _basic_config(self):
        self.title("Administration")
        self.geometry(f"{700}x{500}")
        self.resizable(False, False)
    
    def _create_components(self):
        self.frame_left = ctk.CTkFrame(master=self,width=200,height=500-40,corner_radius=10)
        self.frame_left.place(relx=0.32, rely=0.5, anchor=tk.E)

        self.frame_right = ctk.CTkFrame(master=self, width=420, height=500-40, corner_radius=10)
        self.frame_right.place(relx=0.365, rely=0.5, anchor=tk.W)
        
        for index,filename in enumerate(next(walk("../topics/"), (None, None, []))[2]) :
            btn = ctk.CTkButton(master=self.frame_left, text=filename.split(".")[0],
                                corner_radius=8, command=lambda filename=filename : self._load_data(filename))
            btn.place(relx=0.5, y=35+(50*index), anchor=tk.CENTER)
            self.btn_files.append(btn)

        self.btn_add_quiz = ctk.CTkButton(master=self.frame_left, text="Ajouter Quiz", corner_radius=8, command=self._add_quiz)
        self.btn_add_quiz.place(relx=0.5, rely=0.92, anchor=tk.CENTER)
        
        self.frame_info = ctk.CTkFrame(master=self.frame_right, width=380, height=230, corner_radius=10)
        self.frame_info.place(relx=0.5, y=20, anchor=tk.N)
        
        self.lbl_question = ctk.CTkLabel(master=self.frame_info, text="", width=450, height=50, corner_radius=10)
        self.lbl_question.place(relx=0.5, rely=0, anchor=tk.N)
        
        self.btn_save = ctk.CTkButton(master=self.frame_info, text="Enregistrer", corner_radius=8, command=self._save)
        self.btn_save.place(relx=0.3, rely=0.90, anchor=tk.CENTER)
        
        self.btn_add_question = ctk.CTkButton(master=self.frame_info, text="Ajouter Question", corner_radius=8,
                                              command=self._add_question)
        self.btn_add_question.place(relx=0.7, rely=0.90, anchor=tk.CENTER)
        
        for i in range(4) :
            check_box = ctk.CTkCheckBox(master=self.frame_info, text="",)
            check_box.function = lambda check_box=check_box: self._check(check_box)
            check_box.place(relx=0.15, rely=0.2+(0.15*i), anchor=tk.N)
            self.options.append(check_box)
            entry = ctk.CTkEntry(master=self.frame_info, width=250, height=25, font=("Calibri Light", 12), corner_radius=8)
            entry.place(relx=0.6, rely=0.2+(0.15*i), anchor=tk.N)
            self.entries.append(entry)
            
        ttk.Style().configure("Treeview", rowheight=15)
        
        self.data_table = ttk.Treeview(self.frame_right, columns=("question"), show="headings")
        self.data_table.bind("<Button-1>", self._on_table_click)
        self.data_table.heading("question", text="Question")
        self.data_table.column("question", width=380)
        self.data_table.place(x=20, rely=0.78, anchor=tk.W)
        vsb = ttk.Scrollbar(self.frame_right, orient="vertical", command=self.data_table.yview)
        vsb.place(x=385, rely=0.591, height=175)
        self.data_table.configure(yscrollcommand=vsb.set)
    
    def _check(self, check_box):
        for cbx in self.options:
            cbx.check_state = False
            cbx.on_leave()
        check_box.check_state = True
        check_box.on_leave()
    
    def _add_question(self):
        # Enter Question
        # add to self.data
        # add to self.data_table
        pass
    
    def _add_quiz(self):
        # Enter quiz name
        # create json file
        # create buttons
        pass
    
    def _save(self):
        is_valid = True
        for entry in self.entries:
            if entry.get().strip() == "" :
                is_valid = False
                break
        for option in self.options:
            if option.get() == 1 and is_valid:
                is_valid = True
                break
        print(str(self.data[self.index]).replace("'", "\""))
        # modify the self.data[self.index] object if is_valid :
    
    def _on_table_click(self, event):
        self.index = int( self.data_table.identify("item",event.x,event.y) )
        self.lbl_question.text_label["text"] = self.data[self.index]["question"]
        for i,option in enumerate(self.data[self.index]["options"]):
            self.options[i].check_state = option==self.data[self.index]["answer"]
            self.options[i].on_leave()
            self.entries[i].delete(0, tk.END)
            self.entries[i].insert(0,option)

    def _load_data(self, filename):
        self.data_table.delete(*self.data_table.get_children())
        with open(file=f"../topics/{filename}") as file :
            self.data = eval(file.readline())
            for iid,json in enumerate(self.data):
                self.data_table.insert('', index=tk.END, iid=iid, values=(json["question"],))
