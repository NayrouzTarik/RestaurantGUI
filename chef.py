import tkinter as tk
import subprocess
from tkinter import ttk, messagebox

class RestaurantChefApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Chef App")
        self.root.geometry("800x600")  

        #config du  style de mon app        
        self.style = ttk.Style()
        self.style.configure('TFrame', background='pink')
        self.style.configure('TButton', background='#00433F', foreground='black', width=15, height=1, font=('Arial', 9))
        self.style.configure('TLabel', background='pink', foreground='black', font=('Arial', 11))
        self.style.configure('TListbox', background='#e1d8b9', font=('Arial', 12))
        self.style.configure('Treeview.Heading', foreground='#00433F')

        
        top_frame = ttk.Frame(root)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        logout_icon = tk.PhotoImage(file="logout_icon.png")  
        small_logout_icon = logout_icon.subsample(8, 8) 

        logout_button = ttk.Button(top_frame, text="Logout", image=small_logout_icon, compound=tk.LEFT, command=self.logout, style='TButton')
        logout_button.photo = small_logout_icon  
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

       #creation de la fenetre 
        self.paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.paned_window.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        #panneau left
        left_panel = ttk.Frame(self.paned_window, style='TFrame')
        self.paned_window.add(left_panel)

        header_frame = ttk.Frame(left_panel)
        header_frame.pack()

        header_label = ttk.Label(header_frame, text="Commandes aux Chefs", style='TLabel')
        header_label.grid(row=0, column=0, pady=10)

        # Creation de la listebox pour afficher les commandes 
        self.order_listbox = tk.Listbox(left_panel, height=25, width=50, selectmode=tk.SINGLE)
        self.order_listbox.pack(pady=10)

        #charger les commandes depuis le fichier
        self.orders = self.load_orders()
        self.current_command_index = None

        #les afficher tous
        self.show_all_commands()
        #la fct onselect
        self.order_listbox.bind("<<ListboxSelect>>", self.on_select)


        ready_button = ttk.Button(left_panel, text="Ready", command=self.mark_as_ready)
        ready_button.pack()

        refresh_button = ttk.Button(left_panel, text="Actualiser", command=self.refresh_orders)
        refresh_button.pack()

        #oanneau droite
        right_panel = ttk.Frame(self.paned_window)
        self.paned_window.add(right_panel)

        #creation de cadre ingredients
        ingredients_frame = ttk.Frame(right_panel)
        ingredients_frame.pack(pady=10)

        #saisir le label du tableau
        ingredients_header_label = ttk.Label(ingredients_frame, text="Ingredients en Stock", style='TLabel')
        ingredients_header_label.grid(row=0, column=0, pady=10, columnspan=2)

        #saisir le label du tableau en utilisant TreeView
        self.ingredients_tree = ttk.Treeview(ingredients_frame, columns=('Dish', 'Ingredient', 'Quantity'), show='headings', height=20)
        self.ingredients_tree.grid(row=1, column=0, columnspan=3)

        self.ingredients_tree.heading('Dish', text='Dish')
        self.ingredients_tree.heading(1, text='Ingredient') 
        self.ingredients_tree.heading('Quantity', text='Quantity')
        
        # Chargement des ingrédients depuis le dictionnaire
        self.ingredients = self.load_ingredients()

        # Affichage de tous les ingrédients dans le Treeview
        self.show_all_ingredients()

    #utilisasion de subprocess pour ouvrir un autre script python que sera main
    def logout(self):
        self.root.destroy()
        subprocess.run(["python", "main.py"])

    #from projetRestau.txt je vais lire les commandes et les retourner avec la qtt de chaqune 
    def load_orders(self):
        try:
            with open("projetRestau.txt", "r") as file:
                orders = file.readlines()
                return [order.strip() for order in orders]
        except FileNotFoundError:
            messagebox.showerror("Error", "File 'projetRestau.txt' est introuvable.")
            return []

    #affichage de toute les commades 
    def show_all_commands(self):
        for order in self.orders:
            self.order_listbox.insert(tk.END, order)

    # Marque la commande comme ready et maj la liste des commandes et le fichier
    def mark_as_ready(self):
        if self.current_command_index is not None and self.current_command_index < len(self.orders):
            selected_order = self.order_listbox.get(self.current_command_index)
            messagebox.showinfo("Commande Prete", f"{selected_order} est prete avec succes.")

            # Suppression de la commande de la listebox et de la liste des commandes
            self.order_listbox.delete(self.current_command_index)
            self.orders.pop(self.current_command_index)

            # Écriture des commandes mises à jour dans le fichier
            with open("projetRestau.txt", "w") as file:
                for order in self.orders:
                    file.write(order + "\n")

            self.current_command_index = None
     # Actualise la liste des commandes
    def refresh_orders(self):
        self.order_listbox.delete(0, tk.END)

        self.orders = self.load_orders()

        self.show_all_commands()

        self.current_command_index = None

    # Fonction appelee lors de select dune commande dans la listebox
    def on_select(self, event):
        selected_index = self.order_listbox.curselection()

        if selected_index:
            self.current_command_index = selected_index[0]

    #le dict ingredients qui contient chqaue plat et ses ingredients et la qtts de chqaue ingredients
    def load_ingredients(self):
        ingredients = {
            'Salade': {
                'Leafy greens': 150,
                'Vegetables': 100,
                'Salad dressing': 30,
                'Optional toppings': 20,
            },
            'Soupes': {
                'Broth': 800,
                'Vegetables': 300,
                'Protein': 150,
                'Herbs and spices': 10,
                'Optional extras': 100,
            },
            'Assiettes': {
                'Main protein': 200,
                'Starch': 150,
                'Vegetables': 150,
                'Sauce or gravy': 100,
            },
            'Canapes': {
                'Bread or crackers': 100,
                'Spread or topping': 100,
                'Garnish': 30,
            },
            'Viandes': {
                'Meat of choice': 250,
                'Marinade or seasoning': 20,
                'Cooking oil or fat': 20,
            },
            'Poissons': {
                'Fish fillet or whole fish': 200,
                'Marinade or seasoning': 15,
                'Cooking oil or butter': 20,
                'Lemon or citrus': 2,
            },
            'Pates': {
                'Pasta of choice': 200,
                'Pasta sauce': 200,
                'Protein': 100,
                'Grated cheese': 100,
            },
            'Vegetariens': {
                'Plant-based protein': 250,
                'Vegetables': 200,
                'Grains or starch': 200,
                'Sauce or dressing': 150,
            },
            'Gateaux': {
                'Flour': 300,
                'Sugar': 200,
                'Eggs': 4,
                'Butter': 150,
                'Baking powder/soda': 10,
                'Flavorings': 'Vanilla extract',
            },
            'Tartes': {
                'Pie crust or pastry dough': 250,
                'Filling': 300,
                'Sweeteners': 100,
                'Toppings': 'Whipped cream',
            },
            'Crepes': {
                'Flour': 150,
                'Eggs': 2,
                'Milk': 200,
                'Butter': 50,
                'Filling': 'Nutella and strawberries',
            },
            'Glaces': {
                'Cream': 300,
                'Milk': 200,
                'Sugar': 150,
                'Flavorings': 'Vanilla extract',
            },
            'Croissants': {
                'Puff pastry dough': 300,
                'Butter': 200,
                'Egg wash': 1,
            },
            'PainsViennoiseries': {
                'Flour': 400,
                'Yeast': 10,
                'Butter': 150,
                'Milk': 200,
                'Sugar': 100,
            },
            'Cereales': {
                'Cereal grains': 150,
                'Milk': 200,
                'Sweeteners': 20,
                'Fresh fruits': 'Berries',
                'Nuts or seeds': 'Almonds',
                'Yogurt': 100,
            },
            'OmelettesOeufs': {
                'Eggs': 3,
                'Salt': 'To taste',
                'Pepper': 'To taste',
                'Butter or oil': 20,
                'Fillings': 'Cheese, vegetables, ham',
            },
        }
        return ingredients
    #afficher tous ca dans treeviwe utiliser
    def show_all_ingredients(self):
        for item in self.ingredients_tree.get_children():
            self.ingredients_tree.delete(item)

        for dish, ingredients_dict in self.ingredients.items():
            for ingredient, quantity in ingredients_dict.items():
                ingredient_item = self.ingredients_tree.insert('', 'end', values=(dish, ingredient, quantity))

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantChefApp(root)
    root.mainloop()