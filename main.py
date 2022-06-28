              # /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from functools import partial
import sqlite3
from tkinter import RIGHT, TOP, ttk


# Classe de 'stockage' :
class Data() :
	
	def __init__(self) :
		self.utility="Stockage"


# Classe de mise en forme :
class main():

	def __init__(self):
		
		barr_rech = Data()
		
		window = tk.Tk()
		window.title("Logiciel Gestion Commande")
		window.geometry('1500x1000')
		window.configure(bg="#666363")
		self.titrerestor = tk.Label(window,text=" REST'OR ",font =('normal',20,'bold'),bg="#666363").place(x=700,y=15)
		

		# - Affiche tout les clients -
		def showAllClients():

			color1 = "#8E44AD"
			color = 'grey'
			fg = 13	
			
			env = tk.Tk()
			env.title("Commandes")
			arbre = ttk.Treeview(env, column=("c2", "c3","c4","c5","c6","c7"), show='headings')
			
			self.topShowCommande = tk.Toplevel(bg=color1)
			self.topShowCommande.geometry("400x700")
			
			conn = sqlite3.connect('base.db')
			cur = conn.cursor()
			rqt = "SELECT * FROM Clients;"
			cur.execute(rqt)
			rows = cur.fetchall()
			for row in rows:
				print(row) 
				arbre.insert("", tk.END, values=row)
			cur.close()
			conn.close()
			
			l=["Entreprise", "Nom", "Prénom", "Adresse mail", "Solde du compte", "Numéro de téléphone"]

			for i in range(len(l)):
				arbre.column("#"+str(i+1), anchor=tk.CENTER)
				arbre.heading("#"+str(i+1), text=l[i])
			arbre.pack()
			
			def quitter():
				env.destroy()

			tk.Button(env, text='Quitter', command=quitter).pack(side=TOP)


		# - Affiche tout les clients -
		def showAllCommandes():
			
			color1 = "#8E44AD"
			color = 'grey'
			fg = 13	
			
			env = tk.Tk()
			env.title("Commandes")
			arbre = ttk.Treeview(env, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings')
	
			conn = sqlite3.connect('base.db')
			cur = conn.cursor()
			rqt = "SELECT * FROM Commandes;"
			cur.execute(rqt)
			rows = cur.fetchall()
			for row in rows:
				print(row) 
				arbre.insert("", tk.END, values=row)
			cur.close()
			conn.close()
			
			l = ["Date de dépôt","Identifiant du client","Adresse de livraison","Code postale","Ville","Prix convenu","Devis","Acompte","Reste à payer","Description"]

			for i in range(len(l)):
				arbre.column("#"+str(i+1), anchor=tk.CENTER)
				arbre.heading("#"+str(i+1), text=l[i])
			arbre.pack()
			
			def quitter():
				env.destroy()
			
			tk.Button(env, text='Quitter', command=quitter).pack(side=TOP)


		# - Recherche un client par son nom de famille et affiche ses informations -
		def search(entree):
			if entree.queryString != None:
				print(entree.queryString)
			tree.delete(*tree.get_children())
			conn = sqlite3.connect("base.db")
			cur = conn.cursor()
			cur.execute("SELECT * FROM Clients WHERE clientNom LIKE ?;", [entree.queryString.get()])
			fetch = cur.fetchall()
			for res in fetch:
				tree.insert('', 'end', values=(res))
			cur.close()
			conn.close()


		# - Barre de recherche et tableau -
		barr_rech.queryString = tk.Entry(window,width=40,font = ('courier', 20, 'bold'))
		barr_rech.queryString.pack(padx=10,pady=130)
		tk.Button(window, text='Chercher',highlightbackground = "#666363", command=partial(search,barr_rech)).place(x=1050,y=130)

		tree = ttk.Treeview(window, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')

		l=["ID", "Entreprise", "Nom", "Prénom", "Adresse mail", "Solde du compte", "Numéro de téléphone"]

		for i in range(len(l)):
			tree.column("#"+str(i+1), anchor=tk.CENTER)
			tree.heading("#"+str(i+1), text=l[i])
		tree.place(x=20,y=250)

		
		# - Permet d'ajouter une commande -
		def windowCommande(self):
			
			w = 25
			l = 120
			
			color = "#52575B"

			data = Data() # Instance de Data() qui va nous permettre de stocker les str récupérées grâce à main()
		
			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouvelle Commande")
			self.top.geometry("400x500")

			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg=color).grid(row=1)
			self.titreidClient = tk.Label(self.top,text="Identifiant du client",bg=color).grid(row=2)
			self.titreAdresseLivraison = tk.Label(self.top,text="Adresse de livraison",bg=color).grid(row=3)
			self.titreCP = tk.Label(self.top,text="Code postale",bg=color).grid(row=4)
			self.titreVille = tk.Label(self.top,text="Ville",bg=color).grid(row=5)
			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenu",bg=color).grid(row=6)
			self.titreDevis= tk.Label(self.top,text="Devis",bg=color).grid(row=7)
			self.titreAcompte = tk.Label(self.top,text="Acompte",bg=color).grid(row=8)
			self.titreRestePaye = tk.Label(self.top,text="Reste a payer",bg=color).grid(row=9)
			self.titreDescription = tk.Label(self.top, text="Description",bg=color).grid(row=10)

			data.dateDepot = tk.Entry(self.top)
			data.idClient = tk.Entry(self.top)
			data.adresseLivraison = tk.Entry(self.top)
			data.cp = tk.Entry(self.top)
			data.ville = tk.Entry(self.top)
			data.prixConvenu = tk.Entry(self.top)
			data.devis = tk.Entry(self.top)
			data.acompte = tk.Entry(self.top)
			data.resterPaye = tk.Entry(self.top)
			data.Description = tk.Entry(self.top)

			data.dateDepot.grid(row=1, column=2)
			data.idClient.grid(row=2, column=2)
			data.adresseLivraison.grid(row=3, column=2)
			data.cp.grid(row=4, column=2)
			data.ville.grid(row=5, column=2)
			data.prixConvenu.grid(row=6, column=2)
			data.devis.grid(row=7, column=2)
			data.acompte.grid(row=8, column=2)
			data.resterPaye.grid(row=9, column=2)
			data.Description.grid(row=10, column=2)


			# - Permet l'enregistrement de la BDD -
			def getVarCommande(data,self):
				#print(data.dateDepot.get()) Exemple d'un .get() fonctionnel
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Commandes (dateDepot,idClient,adresseLivraison,cp,ville,prixConvenu,devis,acompte,resterPaye,description) VALUES ('"+data.dateDepot.get()+"','"+data.idClient.get()+"','"+data.adresseLivraison.get()+"','"+data.cp.get()+"','"+data.ville.get()+"','"+data.prixConvenu.get()+"','"+data.devis.get()+"','"+data.acompte.get()+"','"+data.resterPaye.get()+"','"+data.Description.get()+"')"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
				self.top.destroy()

			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarCommande,data,self)).grid(row=11,column=2,sticky=tk.W,pady=4)


		# - Permet d'ajouter un client -
		def windowClient(self):

			w = 25
			l = 120

			color = "#52575B"

			data = Data()

			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouveau client")
			self.top.geometry("400x300")
			
			#self.labelTitre = tk.Label(self.top,text="Nouveaux clients",fg= color,bg=color,font=10).grid(row=0)

			self.titreidClient = tk.Label(self.top,text='Identifiant du client',bg=color).grid(row=1)

			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg=color).grid(row=2)
			self.titrefirmeAdresse = tk.Label(self.top,text='Adresse Entreprise',bg=color).grid(row=3)
			self.titrefirmeCP = tk.Label(self.top,text='Code Postale Entreprise',bg=color).grid(row=4)
			self.titrefirmeVille = tk.Label(self.top,text='Ville Entreprise',bg=color).grid(row=5)
			
			self.titreclientNom = tk.Label(self.top,text='Nom',bg=color).grid(row=6)
			self.titrePrenom = tk.Label(self.top,text='Prenom',bg=color).grid(row=7)
			self.titreadresseMail = tk.Label(self.top,text='Adresse Mail',bg=color).grid(row=8)
			self.titreSoldeCompte = tk.Label(self.top,text='Compte poids',bg=color).grid(row=9)
			self.titreTelephone = tk.Label(self.top,text='Tel',bg=color).grid(row=10)
			
			data.idClient = tk.Entry(self.top)
			
			data.firmeNom = tk.Entry(self.top)
			data.firmeAdresse = tk.Entry(self.top)
			data.firmeCP = tk.Entry(self.top)
			data.firmeVille = tk.Entry(self.top)

			data.clientNom = tk.Entry(self.top)
			data.clientPrenom = tk.Entry(self.top)
			data.adresseMail = tk.Entry(self.top)
			data.soldeCompte = tk.Entry(self.top)
			data.telephone = tk.Entry(self.top)

			data.idClient.grid(row=1, column=2)

			data.firmeNom.grid(row=2, column=2)
			data.firmeAdresse.grid(row=3, column=2)
			data.firmeCP.grid(row=4, column=2)
			data.firmeVille.grid(row=5, column=2)

			data.clientNom.grid(row=6, column=2)
			data.clientPrenom.grid(row=7, column=2)
			data.adresseMail.grid(row=8, column=2)
			data.soldeCompte.grid(row=9, column=2)
			data.telephone.grid(row=10, column=2)


			# - Permet l'enregistrement de la BDD -
			def getVarClients(data):

				#print(data.__dict__) Affiche les attributs de data (classe Data()) pour le deboguage
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Clients (idClient,firmeNom,firmeAdresse,firmeCP,firmeVille,clientNom,clientPrenom,adresseMail,telephone,soldeCompte) VALUES ('"+data.idClient.get()+"','"+data.firmeNom.get()+"','"+data.firmeAdresse.get()+"','"+data.firmeCP.get()+"','"+data.firmeVille.get()+"','"+data.clientNom.get()+"','"+data.clientPrenom.get()+"','"+data.adresseMail.get()+"','"+data.telephone.get()+"','"+data.soldeCompte.get()+"');"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
        		
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarClients,data)).place(x=230,y= 230)
			
		
		# - xxx -
		def windowControle():
			
			color = '#AAD1CA'

			data = Data()

			self.windowControle = tk.Toplevel(bg=color)
			self.windowControle.title("Nouveaux Controle")
			self.windowControle.geometry("400x700")

			data.entryControle=tk.Entry(self.windowControle)
			data.entryControle.grid(row=0, column=1)
			

			# - xxx -
			def getVarControle(data):
				print(data.entryControle.get())

			self.button = tk.Button(self.windowControle,width=10,bg=color,text='Ajouter',command=partial(getVarControle,data)).grid(column=2,row=2)
			

		# - Affiche des boutons permettant d'accéder aux fonctionnalités -
		def prolongBtn():

			btnprolong1 = tk.Button(window,text="Nouvelle commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowCommande,self),width=18).place(x=1165,y=80)
			btnprolong2 = tk.Button(window,text="Nouveau client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=105)
			btnprolong3 = tk.Button(window,text="Nouveau contrôle",bg="#666363",relief="ridge",highlightbackground = "#666363",command = windowControle,width=18).place(x=1165,y=130)			
			btnprolong4 = tk.Button(window,text="Tout les clients",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllClients,width=18).place(x=1165,y=155)
			btnprolong5 = tk.Button(window,text="Toutes les commandes",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllCommandes,width=18).place(x=1165,y=180)


		# - Script de création de la BDD -
		def creer_base():

			sql =["CREATE TABLE Clients (idClient INTEGER PRIMARY KEY NOT NULL UNIQUE, firmeNom TEXT, firmeAdresse TEXT, firmeCP TEXT, firmeVille TEXT, clientNom TEXT, clientPrenom TEXT, adresseMail TEXT, telephone TEXT, soldeCompte REAL);","CREATE TABLE Commandes (idCommande INTEGER PRIMARY KEY NOT NULL UNIQUE, dateDepot TEXT, adresseLivraison TEXT, cp INTEGER, ville TEXT, prixConvenu REAL,devis REAL,acompte REAL,resterPaye REAL, description TEXT, idClient INTEGER NOT NULL, FOREIGN KEY (idClient) REFERENCES Clients(idClient));"]
			li = sqlite3.connect("base.db")
			
			if li:
				cons = li.cursor()

				for i in range(len(sql)):
					cons.execute(sql[i])
				li.commit()
				li.close()


		# - Permet de créer la BDD si elle n'exite pas déjà -
		def verifier_base(base):
			from os.path import isfile
			if not isfile(base):
				creer_base()
			else:
				print("Base existe déjà !")

		# - Appel de la fonction verifier_base à l'initialisation de l'UI -		
		verifier_base('base.db')

		# - Bouton qui déroule les boutons permettants d'accéder aux fonctionnalités -
		window.btn1 = tk.Button(window,text="+",width=3,height=1,font=2,highlightbackground = "#666363",command=prolongBtn).place(x=1300,y=50)
		
		# - Affiche la fenêtre principale à l'écran puis attend que l'usager pose une action -
		window.mainloop()


# - Initialisation de l'UI -
app = main()