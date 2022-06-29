# /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from functools import partial
import sqlite3
import functools
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkinter import RIGHT, TOP, ttk


# Classe de 'stockage' :
class Data():
	
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
			env.title("Clients")
			arbre = ttk.Treeview(env, column=("c2", "c3","c4","c5","c6","c7"), show='headings')
			
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
			
			env = tk.Tk()
			env.title("Commandes")
			arbre = ttk.Treeview(env, column=("c1", "c2","c4","c7","c8","c9","c10"), show='headings')
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
			
			l = ["Date de dépôt","Identifiant du client","Code postale","Devis","Acompte","Reste à payer","Description"]

			for i in range(len(l)):
				arbre.column("#"+str(i+1), anchor=tk.CENTER)
				arbre.heading("#"+str(i+1), text=l[i])
			arbre.pack()
			
			def quitter():
				env.destroy()
			
			tk.Button(env, text='Quitter', command=quitter).pack(side=TOP)

		def get_commandes(event):
			tree = event.widget
			citem = tree.focus()
			val = tree.item(citem)
			nom = val["values"][2]
			conn = sqlite3.connect("base.db")
			curs = conn.cursor()
			curs.execute("SELECT * FROM Commandes WHERE idClient = (Select idClient FROM Clients WHERE clientNom = ?);", [nom])
			fetch = curs.fetchall()
			print(fetch)

		# - Recherche un client par son nom de famille et affiche ses informations -
		def search(entree):
			tree = ttk.Treeview(window, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10"), show='headings')
			l = ["idClient","firmeNom","firmeAdresse","firmeCP","firmeVille","clientNom","clientPrenom","adresseMail","telephone","soldeCompte"]
			for i in range(len(l)):
				tree.column("#"+str(i+1), anchor=tk.CENTER)
				tree.heading("#"+str(i+1), text=l[i])
			tree.place(x=0,y=250)
			if entree.queryString != None:
				print(entree.queryString)
			tree.delete(*tree.get_children())
			conn = sqlite3.connect("base.db")
			cur = conn.cursor()
			cur.execute("SELECT * FROM Clients WHERE clientNom LIKE ?;", [entree.queryString.get()])
			fetch = cur.fetchall()
			for res in fetch:
				tree.insert('', 'end', values=(res))
				tree.bind("<Double-1>", get_commandes)
			cur.close()
			conn.close()
	
		# - Récupération des noms des clients -
		def recuperer_noms():
			conn = sqlite3.connect("base.db")
			cur = conn.cursor()
			cur.execute('SELECT clientNom FROM Clients')
			fetch = cur.fetchall()
			cur.close()
			conn.close()
			return [r[0] for r in fetch]


		# - Barre de recherche et tableau -
		barr_rech.queryString = AutocompleteCombobox(window,width=30,font=('Times', 18),completevalues=recuperer_noms())
		barr_rech.queryString.pack(padx=10,pady=130)
		tk.Button(window, text='Chercher',highlightbackground = "#666363", command=partial(search,barr_rech)).place(x=0,y=180)

		
		# - Permet d'ajouter une commande -
		def windowCommande(self):
			color = "#52575B"
			data = Data() # Instance de Data() qui va nous permettre de stocker les str récupérées grâce à main()
			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouvelle Commande")
			self.top.geometry("400x350")

			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg=color).grid(row=1)
			self.titreidClient = tk.Label(self.top,text="num Fiche",bg=color).grid(row=2)
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
				#if data.idClient.get()!="" and data.Description.get()!="":
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Commandes (dateDepot,idClient,adresseLivraison,cp,ville,prixConvenu,devis,acompte,resterPaye,description) VALUES ('"+data.dateDepot.get()+"','"+data.adresseLivraison.get()+"','"+data.cp.get()+"','"+data.ville.get()+"','"+data.prixConvenu.get()+"','"+data.devis.get()+"','"+data.acompte.get()+"','"+data.resterPaye.get()+"','"+data.Description.get()+"')"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
				self.top.destroy()

			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarCommande,data,self)).place(x=250,y=300)


		# - Permet d'ajouter un client -
		def windowClient(self):
			color = "#52575B"
			data = Data()
			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouveau client")
			self.top.geometry("400x350")
	
			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg=color).grid(row=2)
			self.titrefirmeAdresse = tk.Label(self.top,text='Adresse Entreprise',bg=color).grid(row=3)
			self.titrefirmeCP = tk.Label(self.top,text='Code Postale Entreprise',bg=color).grid(row=4)
			self.titrefirmeVille = tk.Label(self.top,text='Ville Entreprise',bg=color).grid(row=5)
			self.titreclientNom = tk.Label(self.top,text='Nom',bg=color).grid(row=6)
			self.titrePrenom = tk.Label(self.top,text='Prenom',bg=color).grid(row=7)
			self.titreadresseMail = tk.Label(self.top,text='Adresse Mail',bg=color).grid(row=8)
			self.titreSoldeCompte = tk.Label(self.top,text='Compte poids',bg=color).grid(row=9)
			self.titreTelephone = tk.Label(self.top,text='Tel',bg=color).grid(row=10)
			
			data.firmeNom = tk.Entry(self.top)
			data.firmeAdresse = tk.Entry(self.top)
			data.firmeCP = tk.Entry(self.top)
			data.firmeVille = tk.Entry(self.top)
			data.clientNom = tk.Entry(self.top)
			data.clientPrenom = tk.Entry(self.top)
			data.adresseMail = tk.Entry(self.top)
			data.soldeCompte = tk.Entry(self.top)
			data.telephone = tk.Entry(self.top)

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
			def getVarClients(data,self):
				#if data.idClient.get()!="" and data.firmeNom.get()!="" and data.clientNom.get()!="":
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Clients (firmeNom,firmeAdresse,firmeCP,firmeVille,clientNom,clientPrenom,adresseMail,telephone,soldeCompte) VALUES ('"+data.firmeNom.get()+"','"+data.firmeAdresse.get()+"','"+data.firmeCP.get()+"','"+data.firmeVille.get()+"','"+data.clientNom.get()+"','"+data.clientPrenom.get()+"','"+data.adresseMail.get()+"','"+data.telephone.get()+"','"+data.soldeCompte.get()+"');"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
				self.top.destroy()
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarClients,data,self)).place(x=250,y= 300)


		def showClients():
			color1 = "#666363"
			fg = 13	

			entreprise = 'Odelor'
			nom = 'Durant'
			prenom = 'Jean'
			compte = '100'
			tel = '02.32.80.20.39'
			mail = 'jeanDurant@gmail.com'

			self.topShowCommande = tk.Toplevel(bg=color1)
			self.topShowCommande.geometry("3000x700")
			conn = sqlite3.connect('base.db')
			cur = conn.cursor()
			rqt = "SELECT * FROM Commandes;"
			tree = ttk.Treeview(self.topShowCommande,column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14"), show='headings')
			l=["Date de depot","Description","Nom","Code postal","Adresse mail","Telephone","Prenom","Adresse","Ville","Prix convenu", "Devis", "Acompte", "Reste à payer"] 
			for i in range(len(l)):
				tree.column("#"+str(i+1), anchor=tk.CENTER)
				tree.heading("#"+str(i+1), text=l[i])
			tree.place(x=0,y=250)
			cur.execute(rqt)
			rows = cur.fetchall()
			for row in rows:
				print(row) 
				tree.insert("", tk.END, values=row)
			cur.close()
			conn.close()

			entreCompte = 100
			compte = str(entreCompte) + 'g'

			self.LabelFrames = tk.Label(self.topShowCommande,text=entreprise,font = fg,bg=color1).place(x=20,y=25)
			self.LabelName = tk.Label(self.topShowCommande,text=nom,bg=color1).place(x=20,y=50)
			self.LabelFirstName = tk.Label(self.topShowCommande,text=prenom,bg=color1).place(x=20,y=75)

			self.LabelMail = tk.Label(self.topShowCommande,text=mail,bg=color1).place(x=20,y=110)
			self.LabelNumTel = tk.Label(self.topShowCommande,text=tel,bg=color1).place(x=20,y=135)

			self.LabelCompte = tk.Label(self.topShowCommande,text=compte,bg=color1).place(x=340,y=135)
			self.titreCompte = tk.Label(self.topShowCommande,text='Compte poids : ',bg=color1).place(x=220,y=135)
	
		

		# - modif() < showCommand() -			
		def showCommande():
			
			txt = "Variable Commande "

			def modif(self):

				color = "#EEEC7C"

				data = Data()

				data.titreWindow = tk.Label(self.top,text="Fiche Commande",fg = "#EEEC7C" , bg="#EEEC7C",font=10).grid(column=1,row=1)

				data.dateDepot = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.numCommand = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.nom = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.prenom = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.adress = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.cp = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.ville = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.adressMail = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.tel = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.prixConvenue = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.devis = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.acompt = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.resterPaye = tk.Entry(self.top,relief="ridge",highlightbackground = color)

				data.dateDepot.insert(0, "This is the default text")
				data.numCommand.insert(0, "This is the default text")
				data.nom.insert(0, "This is the default text")
				data.prenom.insert(0, "This is the default text")
				data.adress.insert(0, "This is the default text")
				data.cp.insert(0, "This is the default text")
				data.ville.insert(0, "This is the default text")
				data.adressMail.insert(0, "This is the default text")
				data.tel.insert(0, "This is the default text")
				data.prixConvenue.insert(0, "This is the default text")
				data.devis.insert(0, "This is the default text")
				data.acompt.insert(0, "This is the default text")
				data.resterPaye.insert(0, "This is the default text")

				data.dateDepot.grid(row=2, column=2)
				data.numCommand.grid(row=4, column=2)
				data.nom.grid(row=6, column=2)
				data.prenom.grid(row=8, column=2)
				data.adress.grid(row=10, column=2)
				data.cp.grid(row=12, column=2)
				data.ville.grid(row=14, column=2)
				data.adressMail.grid(row=16, column=2)
				data.tel.grid(row=18, column=2)
				data.prixConvenue.grid(row=20, column=2)
				data.devis.grid(row=22, column=2)
				data.acompt.grid(row=24, column=2)
				data.resterPaye.grid(row=26, column=2)


			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("400x700")
			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=20)
			self.titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=50)
			self.titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=80)
			self.titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=110)		
			self.titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=135)
			self.titreCp = tk.Label(self.top,text="C.P",bg="#EEEC7C").place(x=10 , y= 165)
			self.titreVille = tk.Label(self.top,text="Ville",bg="#EEEC7C").place(x=10 , y= 195)
			self.titreAdressMail = tk.Label(self.top,text="Adresse mail",bg="#EEEC7C").place(x=10 , y= 220)
			self.titreTel = tk.Label(self.top,text="Tel",bg="#EEEC7C").place(x=10 , y= 250)
			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg="#EEEC7C").place(x=10 , y=279)
			self.titreDevis= tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=307)
			self.titreAcompt = tk.Label(self.top,text="Acompt",bg="#EEEC7C").place(x=10 , y=335)			
			self.titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg="#EEEC7C").place(x=10 , y=363)
			
			self.preDateDepot = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=20)
			self.numCommand = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=50)
			self.preNom = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=80)                                                                                                                                    
			self.prePrenom = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=110)
			self.preAdress = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=135)
			self.preCp = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 165)
			self.preVille = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 195)
			self.preAdressMail = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 220)
			self.preTel = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 250)
			self.prePrixConvenue = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=279)
			self.preDevis = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=307)
			self.preAcompt = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=335)
			self.preResterPaye = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=363)

			self.btnValide = tk.Button(self.top,text="Modifier",bg="#EEEC7C",relief="ridge",highlightbackground = "#EEEC7C",bd=0,command=partial(modif,self)).place(x=330,y=10)


		# - Affiche des boutons permettant d'accéder aux fonctionnalités -
		def prolongBtn():

			btnprolong1 = tk.Button(window,text="Nouvelle commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowCommande,self),width=18).place(x=1165,y=80)
			btnprolong2 = tk.Button(window,text="Nouveau client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=110)
			btnprolong3 = tk.Button(window,text="Toutes les commandes",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllCommandes,width=18).place(x=1165,y=140)
			btnprolong4 = tk.Button(window,text="Tout les clients",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllClients,width=18).place(x=1165,y=170)


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
