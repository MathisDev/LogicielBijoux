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
		self.couleur="jaune" # Temporaire


# Classe de mise en forme :
class main():	
	def __init__(self):
		self.txt="Test"
		print(self.__dict__)
		
		barr_rech = Data()

		#conn = sqlite3.connect('base.db')

		window = tk.Tk()
		window.title("Logiciel Gestion Commande")
		window.geometry('1500x1000')
		window.configure(bg="#666363")
		self.titrerestor = tk.Label(window,text=" REST'OR ",font =('normal',20,'bold'),bg="#666363").place(x=700,y=15)
		
		def showAllClients():
			# - Variable - 
			color1 = "#8E44AD"
			color = 'grey'
			fg = 13	
			
			env = tk.Tk()
			env.title("Commandes")
			arbre = ttk.Treeview(env, column=("c2", "c3","c4","c5","c6","c7"), show='headings')
	
			"""
			self.topShowCommande = tk.Toplevel(bg=color1)
			self.topShowCommande.geometry("400x700")
			"""
			
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

			
			"""	
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg='grey',height=233,width=400).place(x=0,y=0)
			self.LabelFrames = tk.Label(self.topShowCommande,text=entreprise,font = fg,bg=color).place(x=20,y=25)
			self.LabelName = tk.Label(self.topShowCommande,text=nom,bg=color).place(x=20,y=50)
			self.LabelFirstName = tk.Label(self.topShowCommande,text=prenom,bg=color).place(x=20,y=75)
			self.LabelMail = tk.Label(self.topShowCommande,text=mail,bg=color).place(x=20,y=110)
			self.LabelNumTel = tk.Label(self.topShowCommande,text=tel,bg=color).place(x=20,y=135)
			self.LabelCompte = tk.Label(self.topShowCommande,text=compte,bg=color).place(x=320,y=135)
			self.titreCompte = tk.Label(self.topShowCommande,text='Compte poids : ',bg=color).place(x=220,y=135)
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg="grey",height=233,width=400).place(x=0,y=0)
			self.LabelIdCommande = tk.Label(self.topShowCommande,text="Clients",bg="grey").place(x=20,y=20)
			"""


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

		barr_rech.queryString = tk.Entry(window,width=40,font = ('courier', 20, 'bold'))
		barr_rech.queryString.pack(padx=10,pady=130)
		tk.Button(window, text='Chercher',highlightbackground = "#666363", command=partial(search,barr_rech)).place(x=1050,y=130)

		tree = ttk.Treeview(window, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings')

		l=["ID", "Entreprise", "Nom", "Prénom", "Adresse mail", "Solde du compte", "Numéro de téléphone"]

		for i in range(len(l)):
			tree.column("#"+str(i+1), anchor=tk.CENTER)
			tree.heading("#"+str(i+1), text=l[i])
		tree.place(x=20,y=250)

		def showAllCommandes(): 
			# - Variable - 
			color1 = "#8E44AD"
			color = 'grey'
			fg = 13	
			
			env = tk.Tk()
			env.title("Commandes")
			arbre = ttk.Treeview(env, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14"), show='headings')
	
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
			
			l=["IdCommande","Date de depot","Nom","Prenom","Adresse","Code postal","Ville","Adresse mail","Prix convenu", "Devis", "Acompte", "Reste à payer", "Telephone", "Description"]

			for i in range(len(l)):
				arbre.column("#"+str(i+1), anchor=tk.CENTER)
				arbre.heading("#"+str(i+1), text=l[i])
			arbre.pack()
			
			def quitter():
				env.destroy()

			tk.Button(env, text='Quitter', command=quitter).pack(side=TOP)


		# Top Level Commande #
		def windowCommande(self):
			w = 25
			l = 120
			color = "#52575B"

			data = Data() # Instance de Data() qui va nous permettre de stocker les str récupérées grâce à main()
			w = 25
			l = 120
			color = "#52575B"
			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouvelle Commande")
			self.top.geometry("400x500")

			#self.titreWindow = tk.Label(self.top,text="Fiche Commande",fg=color,bg=color,font=10)

			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg=color).grid(row=0)
			self.titreNom = tk.Label(self.top,text="Nom :",bg=color).grid(row=2)
			self.titrePrenom = tk.Label(self.top,text="Prénom",bg=color).grid(row=3)
			self.titreAdress = tk.Label(self.top,text="Adresse",bg=color).grid(row=4)	
			self.titreCp = tk.Label(self.top,text="C.P",bg=color).grid(row=5)
			self.titreVille = tk.Label(self.top,text="Ville",bg=color).grid(row=6)
			self.titreAdressMail = tk.Label(self.top,text="Adresse mail",bg=color).grid(row=7)		
			self.titreTel = tk.Label(self.top,text="Tel",bg=color).grid(row=8)
			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg=color).grid(row=9)
			self.titreDevis= tk.Label(self.top,text="Devis",bg=color).grid(row=10)
			self.titreAcompt = tk.Label(self.top,text="Acompt",bg=color).grid(row=11)
			self.titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg=color).grid(row=12)
			self.titreDescription = tk.Label(self.top, text="Description",bg=color).grid(row=13)

			data.dateDepot = tk.Entry(self.top)
			data.nom = tk.Entry(self.top)
			data.prenom = tk.Entry(self.top)
			data.adress = tk.Entry(self.top)
			data.cp = tk.Entry(self.top)
			data.ville = tk.Entry(self.top)
			data.adressMail = tk.Entry(self.top)
			data.tel = tk.Entry(self.top)
			data.prixConvenue = tk.Entry(self.top)
			data.devis = tk.Entry(self.top)
			data.acompt = tk.Entry(self.top)
			data.resterPaye = tk.Entry(self.top)
			data.Description = tk.Entry(self.top)

			data.dateDepot.grid(row=0, column=2)
			data.nom.grid(row=2, column=2)
			data.prenom.grid(row=3, column=2)
			data.adress.grid(row=4, column=2)
			data.cp.grid(row=5, column=2)
			data.ville.grid(row=6, column=2)
			data.adressMail.grid(row=7, column=2)
			data.tel.grid(row=8, column=2)
			data.prixConvenue.grid(row=9, column=2)
			data.devis.grid(row=10, column=2)
			data.acompt.grid(row=11, column=2)
			data.resterPaye.grid(row=12, column=2)
			data.Description.grid(row=13, column=2)

			def getVarCommande(data,self):
				#print(data.dateDepot.get()) Exemple d'un .get() fonctionnel
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Commandes (dateDepot,nom,prenom,adress,cp,ville,adresseMail,telephone,prixConvenue,devis,acompt,resterPaye,description) VALUES ('"+data.dateDepot.get()+"','"+data.nom.get()+"','"+data.prenom.get()+"','"+data.adress.get()+"','"+data.cp.get()+"','"+data.ville.get()+"','"+data.adressMail.get()+"','"+data.tel.get()+"','"+data.prixConvenue.get()+"','"+data.devis.get()+"','"+data.acompt.get()+"','"+data.resterPaye.get()+"','"+data.Description.get()+"')"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
				self.top.destroy()

        								
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarCommande,data,self)).grid(row=14,column=2,sticky=tk.W,pady=4)

		# Top Level Clients #
		def windowClient(self):
			data = Data()
			w = 25
			l = 120
			color = "#52575B"

			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouveau client")
			self.top.geometry("400x300")
			
			#self.labelTitre = tk.Label(self.top,text="Nouveaux clients",fg= color,bg=color,font=10).grid(row=0)
			
			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg=color).grid(row=1)
			self.titreClientsNom = tk.Label(self.top,text='Nom',bg=color).grid(row=2)
			self.titrePrenom = tk.Label(self.top,text='Prenom',bg=color).grid(row=3)
			self.titreAdressMail = tk.Label(self.top,text='Adresse Mail',bg=color).grid(row=4)
			self.titreCompte = tk.Label(self.top,text='Compte poids',bg=color).grid(row=5)
			self.titreTelephone = tk.Label(self.top,text='Tel',bg=color).grid(row=6)
			
			data.firmeNom = tk.Entry(self.top)
			data.clientNom = tk.Entry(self.top)
			data.clientPrenom = tk.Entry(self.top)
			data.adresseMail = tk.Entry(self.top)
			data.compte = tk.Entry(self.top)
			data.telephone = tk.Entry(self.top)

			data.firmeNom.grid(row=1, column=2)
			data.clientNom.grid(row=2, column=2)
			data.clientPrenom.grid(row=3, column=2)
			data.adresseMail.grid(row=4, column=2)
			data.compte.grid(row=5, column=2)
			data.telephone.grid(row=6, column=2)

			def getVarClients(data):
				#print(data.__dict__) Affiche les attributs de data (classe Data()) pour le deboguage
				conn = sqlite3.connect('base.db')
				rqt = "INSERT INTO Clients (firmeNom,clientNom,clientPrenom,adresseMail,compte,telephone) VALUES ('"+data.firmeNom.get()+"','"+data.clientNom.get()+"','"+data.clientPrenom.get()+"','"+data.adresseMail.get()+"',"+data.compte.get()+","+data.telephone.get()+");"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
				conn.close()
        		
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarClients,data)).place(x=230,y= 230)

		def windowControle():
			data = Data()
			color = '#AAD1CA'
			self.windowControle = tk.Toplevel(bg=color)
			self.windowControle.title("Nouveaux Controle")
			self.windowControle.geometry("400x700")

			data.entryControle=tk.Entry(self.windowControle)
			data.entryControle.grid(row=0, column=1)
			
			def getVarControle(data):
				print(data.entryControle.get())

			self.button = tk.Button(self.windowControle,width=10,bg=color,text='Ajouter',command=partial(getVarControle,data)).grid(column=2,row=2)

		def showClients():
			# - Variable - 
			color1 = "#8E44AD"
			color = 'grey'
			fg = 13	

			entreprise = 'Odelor'
			nom = 'Durant'
			prenom = 'Jean'
			compte = '100'
			tel = '02.32.80.20.39'
			mail = 'jeanDurant@gmail.com'
			
			self.topShowCommande = tk.Toplevel(bg=color1)
			self.topShowCommande.geometry("400x700")
			#cur = conn.cursor()
			#rqt = "SELECT * FROM Clients;"
			#cur.execute(rqt)
			#rows = cur.fetchall()
			#for row in rows:
			#	print(row)        
			#cur.close()

			# -- creation variable Compte -- #
			entreCompte = 100
			compte = str(entreCompte) + 'g'

			
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg='grey',height=233,width=400).place(x=0,y=0)

			self.LabelFrames = tk.Label(self.topShowCommande,text=entreprise,font = fg,bg=color).place(x=20,y=25)
			self.LabelName = tk.Label(self.topShowCommande,text=nom,bg=color).place(x=20,y=50)
			self.LabelFirstName = tk.Label(self.topShowCommande,text=prenom,bg=color).place(x=20,y=75)

			self.LabelMail = tk.Label(self.topShowCommande,text=mail,bg=color).place(x=20,y=110)
			self.LabelNumTel = tk.Label(self.topShowCommande,text=tel,bg=color).place(x=20,y=135)

			self.LabelCompte = tk.Label(self.topShowCommande,text=compte,bg=color).place(x=320,y=135)
			self.titreCompte = tk.Label(self.topShowCommande,text='Compte poids : ',bg=color).place(x=220,y=135)
			
		def showCommande():
			txt = "Variable Commande "
			# modif() < showCommand() #
			def modif(self):
				color = "#EEEC7C"
				data = Data()
				print("function 'motif' is running")
				data.titreWindow = tk.Label(self.top,text="Fiche Commande",fg = "#EEEC7C" , bg="#EEEC7C",font=10).grid(column=1,row=1)

				data.DateDepot = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.numCommand = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Nom = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Prenom = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Adress = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Cp = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Ville = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.AdressMail = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Tel = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.PrixConvenue = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Devis = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.Acompt = tk.Entry(self.top,relief="ridge",highlightbackground = color)
				data.ResterPaye = tk.Entry(self.top,relief="ridge",highlightbackground = color)

				data.DateDepot.grid(row=2, column=2)
				data.numCommand.grid(row=4, column=2)
				data.Nom.grid(row=6, column=2)
				data.Prenom.grid(row=8, column=2)
				data.Adress.grid(row=10, column=2)
				data.Cp.grid(row=12, column=2)
				data.Ville.grid(row=14, column=2)
				data.AdressMail.grid(row=16, column=2)
				data.Tel.grid(row=18, column=2)
				data.PrixConvenue.grid(row=20, column=2)
				data.Devis.grid(row=22, column=2)
				data.Acompt.grid(row=24, column=2)
				data.ResterPaye.grid(row=26, column=2)
				data.ResterPaye.grid(row=28, column=2)


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

			self.btnValide = tk.Button(self.top,text="modif",bg="#EEEC7C",relief="ridge",highlightbackground = "#EEEC7C",bd=0,command=partial(modif,self)).place(x=330,y=10)


		def prolongBtn():
			btnprolong1 = tk.Button(window,text="Nouvelle commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowCommande,self),width=18).place(x=1165,y=80)
			btnprolong2 = tk.Button(window,text="Nouveau client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=105)
			btnprolong3 = tk.Button(window,text="Nouveau contrôle",bg="#666363",relief="ridge",highlightbackground = "#666363",command = windowControle,width=18).place(x=1165,y=130)			
			btnprolong4 = tk.Button(window,text="Tous les Clients",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllClients,width=18).place(x=1165,y=155)
			btnprolong5 = tk.Button(window,text="Toutes les  commandes",bg="#666363",relief="ridge",highlightbackground = "#666363",command = showAllCommandes,width=18).place(x=1165,y=180)

		
		def creer_base( ):
			sql =["CREATE TABLE Clients (idClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firmeNom TEXT, clientNom TEXT, clientPrenom TEXT, adresseMail TEXT, compte REAL, telephone INTEGER, idCommande INTEGER, FOREIGN KEY (idCommande) REFERENCES Commandes(idCommande));","CREATE TABLE Commandes (idCommande INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateDepot TEXT, nom TEXT, prenom TEXT, adress TEXT, cp INTEGER, ville TEXT, adresseMail TEXT, prixConvenue REAL,devis REAL,acompt REAL,resterPaye REAL, telephone INTEGER, description TEXT);"]
			li = sqlite3.connect("base.db")
			
			if li:
				cons = li.cursor()

				for i in range(len(sql)):
					cons.execute(sql[i])
				li.commit()
				li.close()

		def verifier_base(base):
			from os.path import isfile
			if not isfile(base):
				creer_base()
			else:
				print("Base existe déjà !")
		
		#print(self.__dict__) Affiche les attributs de self (classe main()) pour le déboguage
		
		verifier_base('base.db')
		showCommande()
		showClients()

		window.btn1 = tk.Button(window,text="+",width=3,height=1,font=2,highlightbackground = "#666363",command=prolongBtn).place(x=1300,y=50)
		window.mainloop()

app = main()