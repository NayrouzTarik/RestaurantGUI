import tkinter as tk
from tkinter import ttk, messagebox
import csv

class ReceptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reception")
        self.root.geometry("600x400")
        self.root.configure(bg='#FCE4EC')

        self.search_label = tk.Label(root, text="Rechercher par Nom du Client:", font=("Arial", 12), bg='#FCE4EC')
        self.search_label.pack(padx=10, pady=(10, 0), anchor='w')

        # ou saisir le nom rechercher
        self.search_entry = tk.Entry(root, font=("Arial", 12))
        self.search_entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        #bouton de recherche
        self.search_button = tk.Button(root, text="Search", command=self.search_reservation, font=("Arial", 12), bg='#00433F', fg='white')
        self.search_button.pack(padx=10, pady=5)
        #bouton d actualisation
        self.refresh_button = tk.Button(root, text="Refresh", command=self.load_reservations, font=("Arial", 12), bg='#00433F', fg='white')
        self.refresh_button.pack(padx=10, pady=5)
        #afficher les infos dans un tableau en utilisant le Treeview
        self.reservation_tree = ttk.Treeview(root, columns=("Table Number", "Date", "Time", "Name", "Number of People"), show="headings")
        self.reservation_tree.heading("Table Number", text="Table Number")
        self.reservation_tree.heading("Date", text="Date")
        self.reservation_tree.heading("Time", text="Time")
        self.reservation_tree.heading("Name", text="Name")
        self.reservation_tree.heading("Number of People", text="Number of People")
        self.reservation_tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        #chargement des reservation
        self.load_reservations()
    #cette fct chercher dans le fichier csv dont le client a enregistrer ca reservetion et affiche ligne par ligne dans notre table 
    def load_reservations(self):
        for item in self.reservation_tree.get_children():
            self.reservation_tree.delete(item)
        try:
            with open("reservations.csv", "r", newline="") as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    self.reservation_tree.insert("", tk.END, values=row)
        except FileNotFoundError:
            messagebox.showerror("Error", "Reservation file nexsite pas encore.")

    #la fct de recherche
    def search_reservation(self):
        name = self.search_entry.get()
        found = False
        for child in self.reservation_tree.get_children():
            values = self.reservation_tree.item(child)["values"]
            if name.lower() in values[3].lower():  #rend le nom saisie dans Entry miniscule et extrait uniquement value[3] qui est donc le nom
                self.reservation_tree.selection_set(child)
                self.reservation_tree.focus(child)
                found = True
                break
        if not found:
            messagebox.showinfo("Search", "Aucune Reservation sous ce nom")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReceptionApp(root)
    root.mainloop()
