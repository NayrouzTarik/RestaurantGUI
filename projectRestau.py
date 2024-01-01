from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime

class NWRestaurant:
    def __init__(self, master):
        self.master = master
        master.title("N&W Restaurant")
        master.geometry('1270x685')
        master.configure(bg='pink')
        
        self.txtReceipt = Text(master, height=10, width=40)
        self.txtReceipt.grid(row=0, column=0, rowspan=20, columnspan=20)
        # Les Details des clients
        self.client_details = LabelFrame(master, text='Details du Client', font=('times new roman', 15, 'bold'),
                                         relief=GROOVE, bg="#FFD1DC", fg='#000080')
        self.client_details.grid(row=0, column=0, sticky="ew")


        self.nomLabel = Label(self.client_details, text='Nom du Client', font=('times new roman', 10, 'bold'))
        self.nomLabel.grid(row=0, column=0, padx=20)
        self.nomEntry = Entry(self.client_details, font=('arial', 15), bd=7)
        self.nomEntry.grid(row=0, column=1, padx=10)

        self.phoneLabel = Label(self.client_details, text='Phone', font=('times new roman', 10, 'bold'))
        self.phoneLabel.grid(row=0, column=2, padx=20, pady=2)
        self.phoneEntry = Entry(self.client_details, font=('arial', 15), bd=7)
        self.phoneEntry.grid(row=0, column=3, padx=10)

        self.factureLabel = Label(self.client_details, text='Facture', font=('times new roman', 10, 'bold'))
        self.factureLabel.grid(row=0, column=4, padx=20, pady=2)
        self.factureEntry = Entry(self.client_details, font=('arial', 15), bd=7)
        self.factureEntry.grid(row=0, column=5, padx=10)

        self.searchButton = Button(self.client_details, text="Search", font=('arial', 15), command=self.search_facture)
        self.searchButton.grid(row=0, column=6, padx=10, pady=8)

        # Produit
        self.produitsFrame = Frame(master, bg='pink')
        self.produitsFrame.grid(row=1, column=0, columnspan=3)  


        # ENTREE
        self.EntreeFrame = LabelFrame(self.produitsFrame, text="Entree", font=('times new roman', 15, 'bold'), fg='#000080',
                                    relief=GROOVE, bd=8, width=150, height=150, bg="#FFD1DC")
        self.EntreeFrame.grid(row=0, column=0)

        # Salade
        self.SaladeLabel = Label(self.EntreeFrame, text="Salade", font=('times new roman', 15, 'bold'), fg='#000080',
                                bg="#FFD1DC")
        self.SaladeLabel.grid(row=0, column=0)

        self.SaladeEntry = Entry(self.EntreeFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.SaladeEntry.grid(row=0, column=1)

        # Soupes
        self.SoupesLabel = Label(self.EntreeFrame, text="Soupes", font=('times new roman', 15, 'bold'), fg='#000080',
                                bg="#FFD1DC")
        self.SoupesLabel.grid(row=1, column=0)

        self.SoupesEntry = Entry(self.EntreeFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.SoupesEntry.grid(row=1, column=1)

        # Assiettes de charcuterie/fromage
        self.AssiettesLabel = Label(self.EntreeFrame, text="Charcuterie/fromage", font=('times new roman', 15, 'bold'),
                                    fg='#000080', bg="#FFD1DC")
        self.AssiettesLabel.grid(row=2, column=0)

        self.AssiettesEntry = Entry(self.EntreeFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.AssiettesEntry.grid(row=2, column=1)

        # Canapés et amuse-bouches
        self.CanapesLabel = Label(self.EntreeFrame, text="Canapés et amuse-bouches", font=('times new roman', 15, 'bold'),
                                fg='#000080', bg="#FFD1DC")
        self.CanapesLabel.grid(row=3, column=0)

        self.CanapesEntry = Entry(self.EntreeFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.CanapesEntry.grid(row=3, column=1)


        # PLATS
        self.PlatsFrame = LabelFrame(self.produitsFrame, text="Plats Principaux (Plats)", font=('times new roman', 15, 'bold'),
                                    fg='#000080', relief=GROOVE, bd=8, bg="#FFD1DC")
        self.PlatsFrame.grid(row=0, column=1, padx=10)

        # Viandes grillées
        self.ViandesLabel = Label(self.PlatsFrame, text="Viandes grillées", font=('times new roman', 15, 'bold'), fg='#000080',
                                bg="#FFD1DC")
        self.ViandesLabel.grid(row=0, column=0)

        self.ViandesEntry = Entry(self.PlatsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.ViandesEntry.grid(row=0, column=1)

        # Poissons et fruits de mer
        self.PoissonsLabel = Label(self.PlatsFrame, text="Poissons et fruits de mer", font=('times new roman', 15, 'bold'),
                                    fg='#000080', bg="#FFD1DC")
        self.PoissonsLabel.grid(row=1, column=0)

        self.PoissonsEntry = Entry(self.PlatsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.PoissonsEntry.grid(row=1, column=1)

        # Pâtes
        self.PatesLabel = Label(self.PlatsFrame, text="Pâtes", font=('times new roman', 15, 'bold'), fg='#000080',
                                bg="#FFD1DC")
        self.PatesLabel.grid(row=2, column=0)

        self.PatesEntry = Entry(self.PlatsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.PatesEntry.grid(row=2, column=1)

        # Plats végétariens
        self.VegetariensLabel = Label(self.PlatsFrame, text="Plats végétariens", font=('times new roman', 15, 'bold'),
                                    fg='#000080', bg="#FFD1DC")
        self.VegetariensLabel.grid(row=3, column=0)

        self.VegetariensEntry = Entry(self.PlatsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.VegetariensEntry.grid(row=3, column=1)


        # DESSERTS
        self.DessertsFrame = LabelFrame(self.produitsFrame, text="Desserts", font=('times new roman', 15, 'bold'), fg='#000080',
                                        relief=GROOVE, bd=8, padx=20, bg="#FFD1DC")
        self.DessertsFrame.grid(row=0, column=2)

        # Gâteaux
        self.GateauxLabel = Label(self.DessertsFrame, text="Gâteaux", font=('times new roman', 15, 'bold'), fg='#000080',
                                bg="#FFD1DC")
        self.GateauxLabel.grid(row=0, column=0)

        self.GateauxEntry = Entry(self.DessertsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.GateauxEntry.grid(row=0, column=1)

        # Tartes et tartelettes
        self.TartesLabel = Label(self.DessertsFrame, text="Tartes et tartelettes", font=('times new roman', 15, 'bold'),
                                fg='#000080', bg="#FFD1DC")
        self.TartesLabel.grid(row=1, column=0)

        self.TartesEntry = Entry(self.DessertsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.TartesEntry.grid(row=1, column=1)

        # Crêpes et gaufres
        self.CrepesLabel = Label(self.DessertsFrame, text="Crêpes et gaufres", font=('times new roman', 15, 'bold'),
                                fg='#000080', bg="#FFD1DC")
        self.CrepesLabel.grid(row=2, column=0)

        self.CrepesEntry = Entry(self.DessertsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.CrepesEntry.grid(row=2, column=1)

        # Glaces et sorbets
        self.GlacesLabel = Label(self.DessertsFrame, text="Glaces et sorbets", font=('times new roman', 15, 'bold'),
                                fg='#000080', bg="#FFD1DC")
        self.GlacesLabel.grid(row=3, column=0)

        self.GlacesEntry = Entry(self.DessertsFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.GlacesEntry.grid(row=3, column=1)

        #Les Petit Dejeuner
        self.PetitDejeunerFrame = LabelFrame(self.produitsFrame, text="Petit-déjeuner", font=('times new roman', 15, 'bold'),
                                            fg='#000080', relief=GROOVE, bd=8, bg="#FFD1DC")
        self.PetitDejeunerFrame.grid(row=1, column=0, padx=10, pady=10)

        
        self.CroissantsLabel = Label(self.PetitDejeunerFrame, text="Croissants", font=('times new roman', 15, 'bold'),
                                    fg='#000080', bg="#FFD1DC")
        self.CroissantsLabel.grid(row=0, column=0)

        self.CroissantsEntry = Entry(self.PetitDejeunerFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.CroissantsEntry.grid(row=0, column=1)

        # Pains et viennoiseries
        self.PainsViennoiseriesLabel = Label(self.PetitDejeunerFrame, text="Pains et viennoiseries",
                                            font=('times new roman', 15, 'bold'), fg='#000080', bg="#FFD1DC")
        self.PainsViennoiseriesLabel.grid(row=1, column=0)

        self.PainsViennoiseriesEntry = Entry(self.PetitDejeunerFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.PainsViennoiseriesEntry.grid(row=1, column=1)

        # Céréales
        self.CerealesLabel = Label(self.PetitDejeunerFrame, text="Céréales", font=('times new roman', 15, 'bold'),
                                fg='#000080', bg="#FFD1DC")
        self.CerealesLabel.grid(row=2, column=0)

        self.CerealesEntry = Entry(self.PetitDejeunerFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.CerealesEntry.grid(row=2, column=1)

        # Omelettes et œufs
        self.OmelettesOeufsLabel = Label(self.PetitDejeunerFrame, text="Omelettes et œufs", font=('times new roman', 15, 'bold'),
                                        fg='#000080', bg="#FFD1DC")
        self.OmelettesOeufsLabel.grid(row=3, column=0)

        self.OmelettesOeufsEntry = Entry(self.PetitDejeunerFrame, font=('times new roman', 15, 'bold'), width=10, bd=8)
        self.OmelettesOeufsEntry.grid(row=3, column=1)

        # Facture output
        self.factureFrame = Frame(self.produitsFrame, bd=8, relief=GROOVE)
        self.factureFrame.grid(row=1, column=1, pady=29)

        self.factureLabel = Label(self.factureFrame, text='Facture', font=('times new roman', 15, 'bold'), bd=7,
                                relief=GROOVE, bg='pink')
        self.factureLabel.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.scroll = Scrollbar(self.factureFrame, orient=VERTICAL)
        self.scroll.grid(row=1, column=1, sticky="ns")
        self.textarea = Text(self.factureFrame, width=47, height=10, yscrollcommand=self.scroll.set)
        self.textarea.grid(row=1, column=0)
        self.scroll.config(command=self.textarea.yview)


        #Choix desoptions
        self.FACTMenuFrame = LabelFrame(self.produitsFrame, text="Facture Menu", font=('times new roman', 15, 'bold'),
                                        fg='#000080', relief=GROOVE, bd=8, bg="#FFD1DC")
        self.FACTMenuFrame.grid(row=1, column=2, padx=10, pady=10, sticky="w")


        # Buttons pour La Facture
        self.total_button = Button(self.FACTMenuFrame, text="Calculate Total", font=('arial', 15),
                                   command=self.calculate_total, bg='pink')
        self.total_button.pack(side=LEFT, padx=10, pady=10)

        self.clear_button = Button(self.FACTMenuFrame, text="Clear Facture", font=('arial', 15),
                           command=self.update_facture, bg='pink')
        self.clear_button.pack(side=LEFT, padx=10, pady=10)

        self.print_button = Button(self.FACTMenuFrame, text="Print Facture", font=('arial', 15),
                                    command=self.print_facture, bg='pink')
        self.print_button.pack(side=LEFT, padx=10, pady=10)

        # Facture Variable
        self.CostofFood = StringVar()
        self.ServiceCharge = StringVar()
        self.PaidTax = StringVar()
        self.SubTotal = StringVar()
        self.TotalCost = StringVar()
        self.Receipt_Ref = StringVar()

    def calculate_total(self):
        print("CEn Cours de Calcule du TOTAL...")
        try:
            #Les Valeurs
            Item1 = float(self.SaladeEntry.get()) if self.SaladeEntry.get() else 0
            Item2 = float(self.SoupesEntry.get()) if self.SoupesEntry.get() else 0
            Item3 = float(self.AssiettesEntry.get()) if self.AssiettesEntry.get() else 0
            Item4 = float(self.CanapesEntry.get()) if self.CanapesEntry.get() else 0
            Item5 = float(self.ViandesEntry.get()) if self.ViandesEntry.get() else 0
            Item6 = float(self.PoissonsEntry.get()) if self.PoissonsEntry.get() else 0
            Item7 = float(self.PatesEntry.get()) if self.PatesEntry.get() else 0
            Item8 = float(self.VegetariensEntry.get()) if self.VegetariensEntry.get() else 0
            Item9 = float(self.GateauxEntry.get()) if self.GateauxEntry.get() else 0
            Item10 = float(self.TartesEntry.get()) if self.TartesEntry.get() else 0
            Item11 = float(self.CrepesEntry.get()) if self.CrepesEntry.get() else 0
            Item12 = float(self.GlacesEntry.get()) if self.GlacesEntry.get() else 0
            Item13 = float(self.CroissantsEntry.get()) if self.CroissantsEntry.get() else 0
            Item14 = float(self.PainsViennoiseriesEntry.get()) if self.PainsViennoiseriesEntry.get() else 0
            Item15 = float(self.CerealesEntry.get()) if self.CerealesEntry.get() else 0
            Item16 = float(self.OmelettesOeufsEntry.get()) if self.OmelettesOeufsEntry.get() else 0

            # Calculer Les prix de chaque items
            PriceofFood = (Item1 * 70) + (Item2 * 90) + (Item3 * 50) + (Item4 * 80) + (Item5 * 50) + (Item6 * 80) + \
                        (Item7 * 50) + (Item8 * 120) + (Item9 * 100) + (Item10 * 110) + (Item11 * 100) + (Item12 * 110) + (Item13 * 70) + \
                                    (Item14 * 70) + (Item15 * 80) + (Item16 * 100)


            FoodPrice = str('%.2f' % PriceofFood) + "DH"
            self.CostofFood.set(FoodPrice)

            # Charge du Service
            service_charge = 0.15
            SC = str("%.2f" % service_charge)+ "DH"
            print(SC)
            self.ServiceCharge.set(SC)

            # SubTotal sans Charge
            subtotal_of_items = PriceofFood 

            #Calculer les Taxs,le prix total et lafficher sur le GUI
            Tax =  str(round(subtotal_of_items * 0.05)) + "DH"
            self.PaidTax.set(Tax)
            TT = subtotal_of_items * 0.05
            TC = str(round(subtotal_of_items + service_charge + TT)) + "DH"
            self.TotalCost.set(TC)

            
            #Mettez à jour le contenu du reçu avec les quantités d'articles et les coûts totaux.
            receipt_content = self.get_receipt_content()
            self.txtReceipt.delete('1.0', 'end')
            self.txtReceipt.insert('1.0', receipt_content)

            # Append Le prix total dans la FactureFrame
            self.textarea.insert('end', f'\nTotal Facture: {TC}')
        except ValueError as e:
                print(f"Error: {e}")


    def get_receipt_content(self):
        #chaque tuple se compose du nom de larticle de la quantite saisie par lutilisateur a laide de get()
        item_quantities = [
            ('Salade', self.SaladeEntry.get(), 45),
            ('Soupes', self.SoupesEntry.get(), 50),
            ('Assiettes', self.AssiettesEntry.get(), 35),
            ('Canapes', self.CanapesEntry.get(), 60),
            ('Viandes', self.ViandesEntry.get(), 40),
            ('Poissons', self.PoissonsEntry.get(), 55),
            ('Pates', self.PatesEntry.get(), 30),
            ('Vegetariens', self.VegetariensEntry.get(), 50),
            ('Gateaux', self.GateauxEntry.get(), 80),
            ('Tartes', self.TartesEntry.get(), 70),
            ('Crepes', self.CrepesEntry.get(), 45),
            ('Glaces', self.GlacesEntry.get(), 60),
            ('Croissants', self.CroissantsEntry.get(), 25),
            ('PainsViennoiseries', self.PainsViennoiseriesEntry.get(), 30),
            ('Cereales', self.CerealesEntry.get(), 40),
            ('OmelettesOeufs', self.OmelettesOeufsEntry.get(), 50),
        ]
        # Initialisation receipt_content pour stocker le contenu du recu et d total_cost pour le total.
        receipt_content = ""
        total_cost = 0
        # Boucler a Travers les Articles
        for item, quantity, cost in item_quantities:
            # quantity et cost non vide
            if quantity and cost:
                # Calculer le cout total  avec maj
                total_item_cost = float(quantity) * float(cost)
                receipt_content += f"{item}: {quantity} x {cost} = {total_item_cost}\n"
                total_cost += total_item_cost
        # revoie du contenu nouveau
        receipt_content += "\nTotal Facture: {:.2f} DH".format(total_cost)
        return receipt_content

    def print_facture(self):
        # check si au moins un article est commande
        if all(entry.get() == '' for entry in [self.SaladeEntry, self.SoupesEntry, self.AssiettesEntry, 
                                                self.CanapesEntry, self.ViandesEntry, self.PoissonsEntry, 
                                                self.PatesEntry, self.VegetariensEntry, self.GateauxEntry, 
                                                self.TartesEntry, self.CrepesEntry, self.GlacesEntry, 
                                                self.CroissantsEntry, self.PainsViennoiseriesEntry, 
                                                self.CerealesEntry, self.OmelettesOeufsEntry]):
            messagebox.showinfo("Information", "Vous n avez rien commander.")
            return

        # Le temps et jour 
        current_time = datetime.now().strftime("%H:%M:%S")
        current_day = datetime.now().strftime("%Y-%m-%d")

        # Creation de la lost qui sera afficher et initialisation de la data et temps courant
        items = ["Salade", "Soupes", "Assiettes", "Canapes", "Viandes", "Poissons", "Pates", 
                 "Vegetariens", "Gateaux", "Tartes", "Crepes", "Glaces", "Croissants", 
                 "PainsViennoiseries", "Cereales", "OmelettesOeufs"]
        receipt_content = f"Date: {current_day}\nTime: {current_time}\n\n"

        #Si larticle est commander en ecrit la quantite sinon cest 0 et on ajoute le res a receipt_content
        for item in items:
            quantity = getattr(self, f"{item}Entry").get()
            receipt_content += f"{item}: {quantity}\n"

        # Insert receipt_content dans txtReceipt widget
        self.txtReceipt.insert('1.0', receipt_content)

        # Sauvgarde dans un fichier avec le nom phone et facture du client
        client_name = self.nomEntry.get()
        phone_number = self.phoneEntry.get()
        facture_number = self.factureEntry.get()
        filename = f"{client_name}_{phone_number}_{facture_number}.txt"

        # creation d un dossier pour sauvgarder le data 
        output_directory = "factures"
        os.makedirs(output_directory, exist_ok=True)

        # ecrire dans le fichier convenable
        with open(os.path.join(output_directory, filename), 'w') as file:
            file.write(receipt_content)

        messagebox.showinfo("Information", f"Facture sauvgarder vers {filename}")

    def update_facture(self):
            # supprime le contenu dans (Entry) 
            self.SaladeEntry.delete(0, END)
            self.SoupesEntry.delete(0, END)
            self.AssiettesEntry.delete(0, END)
            self.CanapesEntry.delete(0, END)
            self.ViandesEntry.delete(0, END)
            self.PoissonsEntry.delete(0, END)
            self.PatesEntry.delete(0, END)
            self.VegetariensEntry.delete(0, END)
            self.GateauxEntry.delete(0, END)
            self.TartesEntry.delete(0, END)
            self.CrepesEntry.delete(0, END)
            self.GlacesEntry.delete(0, END)
            self.CroissantsEntry.delete(0, END)
            self.PainsViennoiseriesEntry.delete(0, END)
            self.CerealesEntry.delete(0, END)
            self.OmelettesOeufsEntry.delete(0, END)

            # Reset billing system variables
            self.CostofFood.set("")
            self.ServiceCharge.set("")
            self.PaidTax.set("")
            self.SubTotal.set("")
            self.TotalCost.set("")

            # Reinit du Texte recu
            self.txtReceipt.delete("1.0", END)

            # Renit e textarea in FactureFrame
            self.textarea.delete("1.0", END)

    def search_facture(self):
        #Recup des donnes en util get
        name = self.nomEntry.get()
        phone_number = self.phoneEntry.get()
        facture_number = self.factureEntry.get()

        # donner le nom a rechercher dans le dossier factures
        filename = f"{name}_{phone_number}_{facture_number}.txt"
        file_path = os.path.join("factures", filename)

        print(f"A la Recherche de: {file_path}")  # Res au terminal

        # si le fichier exist 
        if os.path.exists(file_path):
            # Lire le contenue du fichier
            with open(file_path, 'r') as file:
                facture_content = file.read()

            print(f"Content of the file: {facture_content}")  # Terminal output

            # pour afficher la facture en forme message UIG
            messagebox.showinfo("Facture Trouvee", f"Facture contenu:\n\n{facture_content}")
        else:
            # Pas trouver
            messagebox.showinfo("Facture Pas Trouvee", "La facture de ce client nexiste pas")

def main():
    root = Tk()
    app = NWRestaurant(root)
    root.mainloop()

if __name__ == "__main__":
    main()
