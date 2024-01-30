import tkinter as tk
from tkinter import ttk
import os
import sqlite3

class LoginApp:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.geometry("400x300")
        master.configure(bg='#FCE4EC')

        tk.Label(master, text="Username:", font=("Arial", 14), bg='#FCE4EC').pack(pady=10)
        self.username_entry = tk.Entry(master, font=("Arial", 12))
        self.username_entry.pack(pady=10)

        tk.Label(master, text="Password:", font=("Arial", 14), bg='#FCE4EC').pack(pady=10)
        self.password_entry = tk.Entry(master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=10)

  
        tk.Label(master, text="User Type:", font=("Arial", 14), bg='#FCE4EC').pack(pady=10)
        self.user_type = ttk.Combobox(master, values=["Server", "Chef", "Reception"], font=("Arial", 12))
        self.user_type.pack(pady=10)


        self.login_button = tk.Button(master, text="Login", command=self.login, font=("Arial", 14, "bold"), bg='#00433F', fg='beige', bd=0)
        self.login_button.pack(pady=20)

        self.error_label = tk.Label(master, text="", font=("Arial", 12), bg='#FCE4EC', fg='red')
        self.error_label.pack(pady=10)
    #cette nethode utilise la base de donnee sqlite called restaurant.db pour verfier les coordonees entrees si il existe ou pas 
    def authenticate(self):
        connection = sqlite3.connect("restaurant.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=? AND user_type=?", 
                       (self.username_entry.get(), self.password_entry.get(), self.user_type.get()))
        user = cursor.fetchone()

        connection.close()

        return user
    #fermer la fenetre de connection et ouvrir la fenetre convenable au Role choisie
    def open_interface(self, interface_file):
        self.master.destroy()
        os.system(f"python {interface_file}")

    def login(self):
        user = self.authenticate()
        if user:
            if self.user_type.get() == "Server":
                self.open_interface("projectRestau.py")
            elif self.user_type.get() == "Reception":
                self.open_interface("reception.py")
            elif self.user_type.get() == "Chef":
                self.open_interface("chef.py")
        else:
            self.error_label.config(text="Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
