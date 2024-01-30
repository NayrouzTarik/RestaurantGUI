import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

class MenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.configure(bg='#FCE4EC')

        #dict qui contient le menu avec la description image prix
        self.menu_items = {
            "Salade": {"description": "Fresh and crisp salad with a variety of vegetables.", "price": 70, "image": "menugalary/salade.jpg"},
            "Soup": {"description": "A warm and flavorful soup made with fresh ingredients.", "price": 90, "image": "menugalary/soup.jpg"},
            "Assiettes de charcuterie/fromage": {"description": "A delightful platter of assorted cured meats and cheeses.", "price": 50, "image": "menugalary/charcuterie.jpg"},
            "Canapés et amuse-bouches": {"description": "Small, tasty bites to whet your appetite.", "price": 80, "image": "menugalary/canapes.jpg"},
            "Viandes grillées": {"description": "Grilled meats cooked to perfection.", "price": 50, "image": "menugalary/viandes.jpg"},
            "Poissons et fruits de mer": {"description": "Fresh and delicious seafood dishes.", "price": 80, "image": "menugalary/poissons.jpg"},
            "Pâtes": {"description": "Savory pasta dishes with a variety of sauces.", "price": 50, "image": "menugalary/pates.jpg"},
            "Plats végétariens": {"description": "Vegetarian delights that are both tasty and filling.", "price": 120, "image": "menugalary/vegetariens.jpg"},
            "Gâteaux": {"description": "Sweet and indulgent cakes to satisfy your dessert cravings.", "price": 100, "image": "menugalary/gateaux.jpg"},
            "Tartes et tartelettes": {"description": "Delicate and flavorful pies and tarts.", "price": 110, "image": "menugalary/tartes.jpg"},
            "Crêpes et gaufres": {"description": "Light and fluffy crepes and waffles.", "price": 100, "image": "menugalary/crepes.jpg"},
            "Glaces et sorbets": {"description": "Cool and refreshing ice creams and sorbets.", "price": 110, "image": "menugalary/glaces.jpg"},
            "Croissants": {"description": "Buttery and flaky croissants, perfect for breakfast.", "price": 70, "image": "menugalary/croissants.png"},
            "Pains et viennoiseries": {"description": "Freshly baked bread and pastries to start your day.", "price": 70, "image": "menugalary/pains.jpg"},
            "Céréales": {"description": "A selection of cereals for a quick and healthy breakfast.", "price": 80, "image": "menugalary/cereales.jpg"},
            "Omelettes et œufs": {"description": "Customizable omelettes and eggs prepared just the way you like.", "price": 100, "image": "menugalary/omelettes.jpg"}
        }

        #l interface menu
        title_label = tk.Label(root, text="N&W Restaurant Menu", font=("Arial", 16, "bold"), pady=10, bg='#FCE4EC',
                               fg='#00433F')
        title_label.pack()

        self.menu_frame = tk.Frame(root, bg='#FCE4EC')
        self.menu_frame.pack(padx=20, pady=0)

        row, col = 0, 0
        button_size = (160, 90)

        for item in self.menu_items:
            img = Image.open(self.menu_items[item]["image"])
            img = img.resize(button_size, Image.BICUBIC)
            img = ImageTk.PhotoImage(img)

            button = tk.Button(self.menu_frame, text=item, command=lambda i=item: self.show_description(i),
                               image=img, compound=tk.TOP, bg='#F0F0F0', fg='black', padx=10, pady=0)
            button.image = img
            button.grid(row=row, column=col, padx=5, pady=5, sticky='w')
            col += 1
            if col == 4:
                col = 0
                row += 1

        self.description_label = tk.Label(root, text="", font=("Arial", 14), pady=10, bg='#FCE4EC', fg='#00433F')
        self.description_label.pack()

        self.price_label = tk.Label(root, text="", font=("Arial", 14), pady=10, bg='#FCE4EC', fg='#00433F')
        self.price_label.pack()
    #quand un element du dict est choisi cet methode est appeler pour afficher les details 
    def show_description(self, selected_item):
        description = f"{selected_item}\nDescription: {self.menu_items[selected_item]['description']}"
        price = f"Price: {self.menu_items[selected_item]['price']} DH"

        self.description_label.config(text=description)
        self.price_label.config(text=price)

class ReservationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reservation")
        self.root.configure(bg='#FCE4EC')

        reservation_frame = tk.Frame(self.root, bg='#FCE4EC')
        reservation_frame.pack(padx=20, pady=20)

        tk.Label(reservation_frame, text="Table Number:", bg='#FCE4EC').grid(row=0, column=0, sticky='w')
        self.table_number_entry = tk.Entry(reservation_frame)
        self.table_number_entry.grid(row=0, column=1)

        tk.Label(reservation_frame, text="Date (YYYY-MM-DD):", bg='#FCE4EC').grid(row=1, column=0, sticky='w')
        self.date_entry = tk.Entry(reservation_frame)
        self.date_entry.grid(row=1, column=1)

        tk.Label(reservation_frame, text="Time (HH:MM):", bg='#FCE4EC').grid(row=2, column=0, sticky='w')
        self.time_entry = tk.Entry(reservation_frame)
        self.time_entry.grid(row=2, column=1)

        tk.Label(reservation_frame, text="Name:", bg='#FCE4EC').grid(row=3, column=0, sticky='w')
        self.name_entry = tk.Entry(reservation_frame)
        self.name_entry.grid(row=3, column=1)

        tk.Label(reservation_frame, text="Number of People:", bg='#FCE4EC').grid(row=4, column=0, sticky='w')
        self.num_people_entry = tk.Entry(reservation_frame)
        self.num_people_entry.grid(row=4, column=1)

        reserve_button = tk.Button(reservation_frame, text="Reserve", command=self.attempt_reservation)
        reserve_button.grid(row=5, column=0, columnspan=2)

        self.canvas = tk.Canvas(reservation_frame, width=580, height=408)
        self.canvas.grid(row=6, column=0, columnspan=2)
        self.display_image("table.png")

        self.reservations = self.load_reservations()

    def display_image(self, filename):
        self.img = tk.PhotoImage(file=filename)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
    #charger les rsvts depuis le fichier csv
    def load_reservations(self):
        try:
            with open("reservations.csv", "r") as file:
                reader = csv.DictReader(file)
                return [{key: value for key, value in row.items()} for row in reader]
        except FileNotFoundError:
            return []
    #enregistrer les fichiers dans mon fichier csv
    def save_reservations(self):
        with open("reservations.csv", "w", newline="") as file:
            fieldnames = ["Table Number", "Date", "Time", "Name", "Number of People"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.reservations)
    #recup des donnees saisie verification de dispo de la table et si cest le cas le sauvgarde de le reservation
    def attempt_reservation(self):
        table_number = self.table_number_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        name = self.name_entry.get()
        num_people = self.num_people_entry.get()

        if self.is_table_available(table_number, date, time):
            self.book_table(table_number, date, time, name, num_people)
            messagebox.showinfo("Reservation", "Table reserver avec succes!")
            self.save_reservations()  
        else:
            messagebox.showwarning("Reservation", "Table est deja reserver.")
    #comparer la reserv actuelle avec les autre reserv en numero de table date et heure pour nous pas reserver la meme table 2fois par 2perso diff
    def is_table_available(self, table_number, date, time):
        return not any(
            reservation["Table Number"] == table_number
            and reservation["Date"] == date
            and reservation["Time"] == time
            for reservation in self.reservations
        )
    #la reservation de la table avec des details specifiques 
    def book_table(self, table_number, date, time, name, num_people):
        self.reservations.append({
            "Table Number": table_number,
            "Date": date,
            "Time": time,
            "Name": name,
            "Number of People": num_people
        })

class ClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Page Client")
        self.root.geometry("800x400")
        self.root.configure(bg='#FCE4EC')
        self.root.resizable(False, False)


        button_frame = tk.Frame(root, bg='#FCE4EC')
        button_frame.pack(pady=(20, 0), padx=20, fill=tk.BOTH, expand=True)

        menu_img = Image.open("menu.png") 
        menu_img = menu_img.resize((250, 250))  
        menu_img = ImageTk.PhotoImage(menu_img)
        client_button = tk.Button(button_frame, text="Menu", image=menu_img, command=self.open_menu_interface,
                                   compound=tk.TOP)
        client_button.image = menu_img
        client_button.grid(row=0, column=0, padx=60, pady=10)

        reservation_img = Image.open("download.jpg")
        reservation_img = reservation_img.resize((250, 250))  
        reservation_img = ImageTk.PhotoImage(reservation_img)
        reservation_button = tk.Button(button_frame, text="Reservation", image=reservation_img,
                                       command=self.open_reservation_interface, compound=tk.TOP)
        reservation_button.image = reservation_img
        reservation_button.grid(row=0, column=1, padx=10, pady=10)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    #ouvrir l interface menu si clicker
    def open_menu_interface(self):
        menu_window = tk.Toplevel(self.root)
        menu_app = MenuApp(menu_window)
    #ouvrir l interface reservation si clicker
    def open_reservation_interface(self):
        reservation_window = tk.Toplevel(self.root)
        reservation_app = ReservationApp(reservation_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientApp(root)
    root.mainloop()
