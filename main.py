import tkinter as tk
from tkinter import PhotoImage, messagebox
import os

#iuverture d une interface
def open_interface(interface_file):
    os.system(f"python {interface_file}")

#ouvrir la page login en fct de role "chef - server - reception"
def open_login_page(user_type):
    os.system(f"python login.py {user_type}")

main_window = tk.Tk()
main_window.title("WELCOME TO N&W Restaurant")
main_window.geometry("2800x400") 
main_window.configure(bg='#FCE4EC') 

#creation des boutons qui auront une description image et role 
def create_button(text, icon_path, command, bg1, bg2, fg, interface_file, row, column, description):
    button_frame = tk.Frame(main_window, bg='#FCE4EC') 
    button_frame.grid(row=row, column=column, pady=(20, 0), padx=20, sticky="nsew")

    image = PhotoImage(file=icon_path).subsample(3, 3)
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        image=image,
        compound=tk.TOP,
        bg=bg1,
        fg=fg,
        font=("Arial", 14, "bold"),
        bd=0,
        relief=tk.GROOVE,
        borderwidth=3,
        overrelief=tk.RAISED,
        activebackground=bg2
    )
    button.image = image
    button.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    label = tk.Label(button_frame, text=description, font=("Arial", 10), bg='#FCE4EC', fg=fg, wraplength=200)
    label.pack(side=tk.TOP, pady=(0, 20), padx=20, fill=tk.BOTH, expand=True)
#liste des utilisateurs possible 
buttons = [
    ("Client", "client_icon.png", lambda: open_interface("client.py"), '#00433F', '#FF80AB', 'black', "client.py", 0, 0, "Explorez la section Client pour effectuer des réservations, consulter votre historique de repas et profiter d'une expérience personnalisée. Découvrez la facilité de navigation à travers notre menu et réservez votre table préférée en quelques clics seulement."),
    ("Server", "server_icon.png", lambda: open_login_page("Server"), '#AC573D', '#FFD54F', 'black', "login.py", 0, 1, "En tant que serveur dédié, accédez à la Console Serveur pour rationaliser vos tâches. Prenez efficacement les commandes. Élevez l'expérience culinaire et assurez la satisfaction des clients à chaque interaction."),
    ("Chef", "chef_icon.png", lambda: open_login_page("Chef"), '#00433F', '#B0BEC5', 'black', "login.py", 0, 2, "Pour nos chefs talentueux, le Tableau de bord du Chef fournit un hub central pour gérer les recettes, suivre les commandes et coordonner avec l'équipe de cuisine. Restez organisé, améliorez la collaboration et livrez des créations culinaires exceptionnelles sans effort."),
    ("Reception", "reception.png", lambda: open_login_page("Reception"), '#FFB74D', '#FFCCBC', 'black', "login.py", 0, 3, "En tant que réceptionniste dévouée, accédez à notre Tableau de bord de Réception pour gérer les réservations, coordonner les arrivées. Restez à jour sur les disponibilités, communiquez efficacement avec les clients et assurez-vous que chaque séjour soit mémorable.")
]

#boucle for pour creeer tous les boutons dans la liste 
for i, button_data in enumerate(buttons):
    create_button(*button_data)
#config de la grille pour qu il aille le meme alignememet 
main_window.grid_rowconfigure(0, weight=1, uniform="buttons")
for i in range(4):
    main_window.grid_columnconfigure(i, weight=1)

main_window.mainloop()
