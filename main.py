# /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from functools import partial
import sqlite3
from turtle import color

# Classe de 'stockage' :
class Data() :
	
	def __init__(self) :
		self.couleur="jaune" # Temporaire


# Classe de mise en forme :
class main():	
	def __init__(self):
		self.txt="Test"
		print(self.__dict__)
		
		conn = sqlite3.connect('base.db')

		window = tk.Tk()
		window.title("Logiciel Gestion Commande")
		window.geometry('1500x1000')
		window.configure(bg="#666363")
		self.titrerestor = tk.Label(window,text=" REST'OR ",font = 25,bg="#666363").place(x=650,y=15)
		self.searchBarre = tk.Entry(window,width=40,font = ('courier', 20, 'bold')).place(x=445,y=130)
		
		def showClients():
			#cur = conn.cursor()
			#rqt = "SELECT * FROM Clients;"
			#cur.execute(rqt)
			#rows = cur.fetchall()
			#for row in rows:
			#	print(row)        
			#cur.close()
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
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg="grey",height=233,width=400).place(x=0,y=0)
			self.LabelIdCommande = tk.Label(self.topShowCommande,text="Clients",bg="grey").place(x=20,y=20)


		def showCommande(txt):
			# modif() < showCommand() #
			color = "#EEEC7C"
			data = Data()
			def modif():
				print("function 'motif' is running")
				data.pluspreDateDepot = tk.Entry(self.top,width=30).place(x=100 ,y=40)
				data.plusnumCommand = tk.Entry(self.top,width=30).place(x=100 ,y=70)
				data.pluspreNom = tk.Entry(self.top,width=30).place(x=100 ,y=100)
				data.plusprePrenom = tk.Entry(self.top,width=30).place(x=100 ,y=130)
				data.pluspreAdress = tk.Entry(self.top,width=30).place(x=100 ,y=160)
				data.pluspreCp = tk.Entry(self.top,width=30).place(x=100 , y= 190)
				data.pluspreVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)
				data.pluspreVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)
				data.pluspreAdressMail = tk.Entry(self.top,width=30).place(x=100 , y= 250)
				data.pluspreTel = tk.Entry(self.top,width=30).place(x=100 , y= 280)
				data.plusprePrixConvenue = tk.Entry(self.top,width=30).place(x=100,y=320)
				data.pluspreDevis = tk.Entry(self.top,width=30).place(x=100,y=350)
				data.pluspreAcompt = tk.Entry(self.top,width=30).place(x=100,y=380)
				data.pluspreResterPaye = tk.Entry(self.top,width=30).place(x=100,y=410)


			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("400x700")
			self.frameClientsInfo = tk.Frame(self.top,bg="grey",height=233,width=400).place()
			self.titreself = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)
			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=40)
			self.titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=70)
			self.titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=100)
			self.titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=130)		
			self.titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=160)
			self.titreCp = tk.Label(self.top,text="C.P",bg="#EEEC7C").place(x=10 , y= 190)
			self.titreVille = tk.Label(self.top,text="Ville",bg="#EEEC7C").place(x=10 , y= 220)
			self.titreAdressMail = tk.Label(self.top,text="Adresse mail",bg="#EEEC7C").place(x=10 , y= 250)
			self.titreTel = tk.Label(self.top,text="Tel",bg="#EEEC7C").place(x=10 , y= 280)
			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg="#EEEC7C").place(x=10 , y=320)
			self.titreDevis= tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=350)
			self.titreAcompt = tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=380)			
			self.titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg="#EEEC7C").place(x=10 , y=410)
			self.preDateDepot = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=40)
			self.numCommand = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=70)
			self.preNom = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=100)
			self.prePrenom = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=130)
			self.preAdress = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 ,y=160)
			self.preCp = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 190)
			self.preVille = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 220)
			self.preVille = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 220)
			self.preAdressMail = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 250)
			self.preTel = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100 , y= 280)
			self.prePrixConvenue = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=320)
			self.preDevis = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=350)
			self.preAcompt = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=380)
			self.preResterPaye = tk.Label(self.top,text=txt,width=30,bg="#EEEC7C").place(x=100,y=410)

			self.btnValide = tk.Button(self.top,text="modification",bg="#666363",highlightbackground =color,bd=0,command=modif).place(x=200,y=10)

			
		def homeListe(self):
			self.txt = 'Le nom de la commande '
			bg1 = "grey"
			bg2 = "#D34514"
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg=bg2,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg='orange',relief="ridge",command=showClients).place(x=260,y=300)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=350)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=400)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=450)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=300)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=350)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=400)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=450)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=300)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=350)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=400)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=450)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=300)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=350)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=400)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=450)


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
			self.top.geometry("400x700")

			self.titreWindow = tk.Label(self.top,text="Fiche Commande",bg=color,font=10).place(x=30 , y=0)
			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg=color).place(x=10 , y=40)
			self.titreNumCommande = tk.Label(self.top,text="n ° :",bg=color).place(x=10 , y=70)
			self.titreNom = tk.Label(self.top,text="Nom :",bg=color).place(x=10 , y=100)
			self.titrePrenom = tk.Label(self.top,text="Prénom",bg=color).place(x=10 , y=130)
			self.titreAdress = tk.Label(self.top,text="Adresse",bg=color).place(x=10 , y=160)			
			self.titreCp = tk.Label(self.top,text="C.P",bg=color).place(x=10 , y= 190)
			self.titreVille = tk.Label(self.top,text="Ville",bg=color).place(x=10 , y= 220)
			self.titreAdressMail = tk.Label(self.top,text="Adresse mail",bg=color).place(x=10 , y= 250)			
			self.titreTel = tk.Label(self.top,text="Tel",bg=color).place(x=10 , y= 280)
			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg=color).place(x=10 , y=320)
			self.titreDevis= tk.Label(self.top,text="Devis",bg=color).place(x=10 , y=350)
			self.titreAcompt = tk.Label(self.top,text="Devis",bg=color).place(x=10 , y=380)
			self.titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg=color).place(x=10 , y=410)


			data.dateDepot = tk.Entry(self.top,width=w).place(x=l ,y=40)
			data.numCommand = tk.Entry(self.top,width=w).place(x=l ,y=70)
			data.preNom = tk.Entry(self.top,width=w).place(x=l ,y=100)
			data.prePrenom = tk.Entry(self.top,width=w).place(x=l ,y=130)
			data.preAdress = tk.Entry(self.top,width=w).place(x=l ,y=160)
			data.preCp = tk.Entry(self.top,width=w).place(x=l , y= 190)
			data.preCp = tk.Entry(self.top,width=w).place(x=l , y= 190)
			data.preAdressMail = tk.Entry(self.top,width=w).place(x=l , y= 250)
			data.preTel = tk.Entry(self.top,width=w).place(x=l , y= 280)
			data.prePrixConvenue = tk.Entry(self.top,width=w).place(x=l,y=320)
			data.preDevis = tk.Entry(self.top,width=w).place(x=l,y=350)
			data.preAcompt = tk.Entry(self.top,width=w).place(x=l,y=380)
			data.preResterPaye = tk.Entry(self.top,width=w).place(x=l,y=410)
					
			def getVarCommande(self, data):
				#print(data.dateDepot.get()) Exemple d'un .get() fonctionnel
				rqt = "INSERT INTO Commandes (idCommande, dateDepot, adresse, cp, ville, idClient) VALUES ('"+data.idCommande.get()+"','"+data.dateDepot.get()+"','"+data.adresse.get()+"','"+data.cp.get()+"','"+data.ville.get()+"','"+data.idClient.get()+"')"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
        								
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarCommande, self, data)).place(x=200,y= 500)

		# Top Level Clients #
		def windowClient(self):
			data = Data()
			w = 25
			l = 120
			color = "#52575B"

			self.top = tk.Toplevel(bg=color)
			self.top.title("Nouveau client")
			self.top.geometry("400x700")
			
			self.labelTitre = tk.Label(self.top,text="Nouveaux Clients",bg=color,font=10).place(x=30,y=10)
			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg=color).place(x=10, y= 80)
			self.titreClientsNom = tk.Label(self.top,text='Nom',bg=color).place(x=10, y= 110)
			self.titrePrenom = tk.Label(self.top,text='Prenom',bg=color).place(x=10, y= 140)
			self.titreAdressMail = tk.Label(self.top,text='Adresse Mail',bg=color).place(x=10, y= 170)
			self.titreCompte = tk.Label(self.top,text='Compte poids',bg=color).place(x=10, y= 200)
			self.titreTelephone = tk.Label(self.top,text='Tel',bg=color).place(x=10, y= 230)
			
			data.firmeNom = tk.Entry(self.top)
			data.clientNom = tk.Entry(self.top)
			data.clientPrenom = tk.Entry(self.top)
			data.adresseMail = tk.Entry(self.top)
			data.compte = tk.Entry(self.top)
			data.telephone = tk.Entry(self.top)

			data.firmeNom.grid(row=0, column=2)
			data.clientNom.grid(row=1, column=2)
			data.clientPrenom.grid(row=2, column=2)
			data.adresseMail.grid(row=3, column=2)
			data.compte.grid(row=4, column=2)
			data.telephone.grid(row=5, column=2)

			def getVarClients(data):
				#print(data.__dict__) Affiche les attributs de data (classe Data()) pour le deboguage
				rqt = "INSERT INTO Clients (clientNom,clientPrenom,firmeNom,adresseMail,compte,telephone) VALUES ('"+data.firmeNom.get()+"','"+data.clientNom.get()+"','"+data.clientPrenom.get()+"','"+data.adresseMail.get()+"',"+data.compte.get()+","+data.telephone.get()+");"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
        		
			self.btnValide = tk.Button(self.top, text='Valider', highlightbackground =color,command=partial(getVarClients,data)).place(x=200,y= 500)

		def windowControle():
			data = Data()
			color = '#AAD1CA' 
			self.windowControle = tk.Toplevel(bg=color)
			self.windowControle.title("Nouveaux Controle")
			self.windowControle.geometry("400x700")

			data.entryControle=tk.Entry(self.windowControle)
			data.entryControle.grid(row=0, column=1)
			
			def getVar(data):
				print(data.entryControle.get())

			self.button = tk.Button(self.windowControle,width=10,bg=color,text='Ajouter',command=partial(getVar,data)).grid(column=2,row=2)
			

		def prolongBtn():
			btnprolong1 = tk.Button(window,text="Nouvelle Commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowCommande,self),width=18).place(x=1165,y=147)
			btnprolong2 = tk.Button(window,text="Nouveaux Client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=173)
			opencommandeWindow = tk.Button(window,text="New Controle",bg="#666363",relief="ridge",highlightbackground = "#666363",command = windowControle,width=18).place(x=1165,y=198)
	


		def creer_base():
			print("Base créée.")


		if __name__ == '__main__':
			homeListe(self)
			if creer_base():
				schema = verifier_base()


		def verifier_base():
			sql = "SELECT * from sqlite_master;"
			li = sqlite3.connect("base.db")
	
			if li:
				cons = li.cursor()
				cons.execute(sql)
				resp = cons.fetchall()
				li.close()
				return resp

		def creer_base(db):
			sql = ["CREATE TABLE Clients (idClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firmeNom TEXT, clientNom TEXT, clientPrenom TEXT, adresseMail TEXT, compte REAL, telephone INTEGER);","CREATE TABLE Commandes (idCommande INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateDepot INTEGER, adresse TEXT, cp INTEGER, ville TEXT, idClient INTEGER, FOREIGN KEY (idClient) REFERENCES Clients(idClient));"]
			li = sqlite3.connect("base.db")
			
			if li:
				cons = li.cursor()

				for i in range(len(sql)):
					cons.execute(sql[i])
				li.commit()
				li.close()
				

		#print(self.__dict__) Affiche les attributs de self (classe main()) pour le déboguage

		window.btn1 = tk.Button(window,text="+",width=3,height=1,font=2,highlightbackground = "#666363",command=prolongBtn).place(x=1300,y=120)
		window.mainloop()

app = main()
