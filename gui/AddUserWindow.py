# encoding:utf-8
import tkinter as tk
import customtkinter as ctk
from dao.UserDB import UserDao, User
from tkinter import messagebox

class AddUserWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._basic_config()
        self._create_components()
        self.mainloop()
    
    def _basic_config(self):
        self.title("Creer un nouveau utilisateur")
        self.resizable(False, False)
        window_width = 500
        window_height = 300
        margin_x = int((self.winfo_screenwidth()/2) - (window_width/2))
        margin_y = int((self.winfo_screenheight()/2) - (window_height/2))
        self.geometry(f"{window_width}x{window_height}+{margin_x}+{margin_y}")
    
    def _create_components(self):
        ctk.CTkLabel(self, text="Entrez le username", width=190, height=40).place(x=30,y=30)
        self.username = ctk.CTkEntry(self, width=180, height=40, font=("Calibri Light", 12), corner_radius=8)
        self.username.place(x=250,y=30)
        
        ctk.CTkLabel(self, text="Entrez le mot de passe", width=190, height=40).place(x=43,y=90)
        self.password1 = ctk.CTkEntry(self, show="*",width=180, height=40, font=("Calibri Light", 12), corner_radius=8)
        self.password1.place(x=250,y=90)
        
        ctk.CTkLabel(self, text="Confirmez le mot de passe", width=190, height=40).place(x=43,y=150)
        self.password2 = ctk.CTkEntry(self, show="*",width=180, height=40, font=("Calibri Light", 12), corner_radius=8)
        self.password2.place(x=250,y=150)
        
        self.admin = ctk.CTkCheckBox(master=self, text="Administrateur")
        self.admin.place(x=250, y=200)
        
        self.submit = ctk.CTkButton(master=self, text="Valider", command=self._submit)
        self.submit.place(x=120, y=240)
        
        self.reset = ctk.CTkButton(master=self, text="Effacer", command=self._reset)
        self.reset.place(x=270, y=240)
    
    def _submit(self):
        if self.username.get().strip() == "" or self.password1.get().strip() == "" or self.password2.get().strip() == "" :
            messagebox.showwarning("Erreur", "Veuillez remplire toutes les informations")
            return
        if self.password1.get() != self.password2.get() :
            messagebox.showwarning("Erreur", "les deux mots de passe ne correspondent pas")
            return
        is_admin = True if self.admin.get() == 1 else False
        if UserDao.add_user(User(self.username.get().strip().lower(), self.username.get().strip(), is_admin)):
            messagebox.showinfo("information", "Utilisateur ajouté avec succes")
        else:
            messagebox.showerror("erreur", "ce nom d'utilisateur (username) est déjà utilisé")

    def _reset(self):
        self.username.delete(0, tk.END)
        self.password1.delete(0, tk.END)
        self.password2.delete(0, tk.END)
        self.admin.check_state = False
        self.admin.on_leave()
