# encoding:utf-8
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from gui.UserWindow import UserWindow

class LoginWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ctk.set_appearance_mode("Dark")
        self.title("Authentification")
        self.resizable(False, False)
        window_width = 500
        window_height = 300
        margin_x = int((self.winfo_screenwidth()/2) - (window_width/2))
        margin_y = int((self.winfo_screenheight()/2) - (window_height/2))
        self.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
        
        ctk.CTkLabel(self, text="Entrez votre username", width=190, height=40).place(x=30,y=50)
        self.username = ctk.CTkEntry(self, width=180, height=40, font=("Calibri Light", 12), corner_radius=8)
        self.username.place(x=250,y=50)
        
        ctk.CTkLabel(self, text="Entrez votre mot de passe", width=190, height=40).place(x=43,y=100)
        self.password = ctk.CTkEntry(self, show="*",width=180, height=40, font=("Calibri Light", 12), corner_radius=8)
        self.password.place(x=250,y=100)

        self.submit = ctk.CTkButton(master=self, text="Valider", command=self._submit)
        self.submit.place(x=120, y=180)
        
        self.reset = ctk.CTkButton(master=self, text="Effacer", command=self._reset)
        self.reset.place(x=270, y=180)
    
    def _submit(self):
        if len(self.password.get()) == 0 or self.username.get().strip() == "" :
            messagebox.showerror("Erreur", "Veuillez entrer toutes les informations demandées")
            return
        self.withdraw()
        UserWindow()
    
    def _reset(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
    
if __name__ == '__main__':
    ctk.set_appearance_mode("Dark")
    LoginWindow()
    tk.mainloop()