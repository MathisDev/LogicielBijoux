# /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from functools import partial
import sqlite3

class main():
	def __init__(self):
		db = "./base.db"
		conn = sqlite3.connect('base.db')
		cur = conn.cursor()

		self.window = tk.Tk()
		self.window.title("Logiciel Gestion Commande")
		self.window.geometry('1500x1000')
		self.window.configure(bg="#666363")
		self.titrerestor = tk.Label(self.window,text=" REST'OR ",font = 25,bg="#666363").place(x=650,y=15)
		self.searchBarre = tk.Entry(self.window,width=40,font = ('courier', 20, 'bold')).place(x=445,y=130)
		
		def showClients():
			self.topShowCommande = tk.Toplevel(bg="#8E44AD")
			self.topShowCommande.geometry("400x700")
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg="grey",height=233,width=400).place(x=0,y=0)
			self.LabelIdCommande = tk.Label(self.topShowCommande,text="Clients",bg="grey").place(x=20,y=20)

		def homeListe():
			self.txt = "Le nom de la commande "
			bg1 = "grey"
			bg2 = "#D34514"
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,bg=bg2,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,bg=bg2,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,bg=bg1,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=490,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=720,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=self.txt,width=19,height=2,relief="ridge",bg=bg1,command=partial(showCommande,self.txt)).place(x=950,y=450)
# Top Level Commande #
		def windowCommand():
			w = 25
			l = 120
			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("400x700")
			titreWindow = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)

			titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=40)
			preDateDepot = tk.Entry(self.top,width=w).place(x=l ,y=40)

			titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=70)
			numCommand = tk.Entry(self.top,width=w).place(x=l ,y=70)

			titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=100)
			preNom = tk.Entry(self.top,width=w).place(x=l ,y=100)

			titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=130)
			prePrenom = tk.Entry(self.top,width=w).place(x=l ,y=130)

			titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=160)
			preAdress = tk.Entry(self.top,width=w).place(x=l ,y=160)

			titreCp = tk.Label(self.top,text="C.P",bg="#EEEC7C").place(x=10 , y= 190)
			preCp = tk.Entry(self.top,width=w).place(x=l , y= 190)

			titreVille = tk.Label(self.top,text="Ville",bg="#EEEC7C").place(x=10 , y= 220)
			preVille = tk.Entry(self.top,width=w).place(x=l , y= 220)

			titreAdressMail = tk.Label(self.top,text="Adresse mail",bg="#EEEC7C").place(x=10 , y= 250)
			preAdressMail = tk.Entry(self.top,width=w).place(x=l , y= 250)

			titreTel = tk.Label(self.top,text="Tel",bg="#EEEC7C").place(x=10 , y= 280)
			preTel = tk.Entry(self.top,width=w).place(x=l , y= 280)

			titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg="#EEEC7C").place(x=10 , y=320)
			prePrixConvenue = tk.Entry(self.top,width=w).place(x=l,y=320)

			titreDevis= tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=350)
			preDevis = tk.Entry(self.top,width=w).place(x=l,y=350)

			titreAcompt = tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=380)
			preAcompt = tk.Entry(self.top,width=w).place(x=l,y=380)

			titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg="#EEEC7C").place(x=10 , y=410)
			preResterPaye = tk.Entry(self.top,width=w).place(x=l,y=410)
	

			# getVarCommande() < windowCommand() #
			def getVarCommande(predate):
				self.date = self.predate.ent.get()
				# recup les valeur des differantes entry dans windowCommande() #
				#rqt = "INSERT INTO Commandes (id_client,date,terminée,adresse,code_postale,ville) VALUES ('"+id_client+"','"+date+"','"+termine+"','"+adresse+"','"+code_postale+"','"+ville+"')"
			# Btn Valider de WindowClients pour run 'getVarCommande()' #
			btnValide = tk.Button(self.top,text="Valider",bg="#666363",highlightbackground = "#EEEC7C",bd=0,command=partial(getVarCommande,preDateDepot)).place(x=200,y=600)

# Top Level Clients #
		def windowClients():
			self.top = tk.Toplevel(bg="#8E44AD")
			self.top.geometry("400x700")
			self.labelTitre = tk.Label(self.top,text="Nouveaux Clients",bg="#8E44AD",font=10).place(x=110,y=10)

			self.titreIdClient = tk.Label(self.top,text='Nom du clients',bg="#8E44AD").place(x=10, y= 50)
			self.idClient = tk.Entry(self.top,width=25).place(x=130, y= 50)

			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg="#8E44AD").place(x=10, y= 80)
			self.firmeNom = tk.Entry(self.top,width=25).place(x=130, y= 80)

			self.titreClientsNom = tk.Label(self.top,text='Nom',bg="#8E44AD").place(x=10, y= 110)
			self.clientNom = tk.Entry(self.top,width=25).place(x=130, y= 110)

			self.titrePrenom = tk.Label(self.top,text='Prenom',bg="#8E44AD").place(x=10, y= 140)
			self.clientPrenom = tk.Entry(self.top,width=25).place(x=130, y= 140)

			self.titreAdressMail = tk.Label(self.top,text='Adresse Mail',bg="#8E44AD").place(x=10, y= 170)
			self.adresseMail = tk.Entry(self.top,width=25).place(x=130, y= 170)

			self.titreCompte = tk.Label(self.top,text='Compte poids',bg="#8E44AD").place(x=10, y= 200)
			self.compte = tk.Entry(self.top,width=25).place(x=130, y= 200)

			self.titreTelephone = tk.Label(self.top,text='Tel',bg="#8E44AD").place(x=10, y= 230)
			self.telephone = tk.Entry(self.top,width=25).place(x=130, y= 230)
			#  getVarClients() < windowClients() #
			def getVarClients():
				print("etVarClients()")
				# recup les valeur des differantes entry dans windowClients() #
				#rqt = "INSERT INTO Clients (nom,prenom,entreprise,email,téléphone) VALUES ('"+nom+"','"+prenom+"','"+entreprise+"','"+email+"',"+tel+")"
			# Btn Valider de WindowClients pour run 'getVarClients()' #
			btnValide = tk.Button(self.top,text="Valider",bg="#666363",highlightbackground = "#8E44AD",bd=0,command=getVarClients).place(x=200,y=600)


		def prolongBtn():
				btnprolong1 = tk.Button(self.window,text="Nouvelle Commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = windowCommand,width=18).place(x=1165,y=147)
				btnprolong2 = tk.Button(self.window,text="Nouveaux Client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = windowClients,width=18).place(x=1165,y=173)	

		def showCommande(txt):
			# modif() < showCommand() #
			def modif():
				print("function 'motif' is running")
				self.pluspreDateDepot = tk.Entry(self.top,width=30).place(x=100 ,y=40)
				self.plusnumCommand = tk.Entry(self.top,width=30).place(x=100 ,y=70)
				self.pluspreNom = tk.Entry(self.top,width=30).place(x=100 ,y=100)
				self.plusprePrenom = tk.Entry(self.top,width=30).place(x=100 ,y=130)
				self.pluspreAdress = tk.Entry(self.top,width=30).place(x=100 ,y=160)
				self.pluspreCp = tk.Entry(self.top,width=30).place(x=100 , y= 190)
				self.pluspreVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)
				self.pluspreVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)
				self.pluspreAdressMail = tk.Entry(self.top,width=30).place(x=100 , y= 250)
				self.pluspreTel = tk.Entry(self.top,width=30).place(x=100 , y= 280)
				self.plusprePrixConvenue = tk.Entry(self.top,width=30).place(x=100,y=320)
				self.pluspreDevis = tk.Entry(self.top,width=30).place(x=100,y=350)
				self.pluspreAcompt = tk.Entry(self.top,width=30).place(x=100,y=380)
				self.pluspreResterPaye = tk.Entry(self.top,width=30).place(x=100,y=410)

			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("400x700")
			self.frameClientsInfo = tk.Frame(self.top,bg="grey",height=233,width=400).place()
			self.titreWindow = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)
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
			self.btnValide = tk.Button(self.top,text="modification",bg="#666363",bd=0,command=modif).place(x=200,y=10)
			
		def creer_base(db):
			print("function 1")
			#sql = ["CREATE TABLE Clients (idClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firmeNom TEXT, clientNom TEXT, clientPrenom TEXT, adresseMail TEXT, compte REAL, telephone INTEGER);","CREATE TABLE Commandes (idCommande INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateDepot INTEGER, adresse TEXT, cp INTEGER, ville TEXT, idClient INTEGER, FOREIGN KEY (idClient) REFERENCES Clients(idClient));"]
			#li = sqlite3.connect(db)
			#if li:
			#	cons = li.cursor()
			#for i in range(len(sql)):
			#	cons.execute(sql[i])
			#li.commit()
			#li.close()

		def verifier_base(db):
			print("function 2")
			#sql = "SELECT * from sqlite_master;"
			#li = sqlite3.connect(db)
			#if li:
			#	cons = li.cursor()
			#	cons.execute(sql)
			#	resp = cons.fetchall()
			#	li.close()
			#	return resp
		# verif DB #
		if __name__ == '__main__':
			if creer_base(db):
				schema = verifier_base(db)
		# run d'homeListe() pas fini j'ai des trucs a rajouter c pk j'ai mis un 'if' #
		if __name__ == '__main__':
			homeListe()
			
		self.btn1 = tk.Button(self.window,text="+",width=3,height=1,font=2,highlightbackground = "#666363",command=prolongBtn).place(x=1300,y=120)
		self.window.mainloop()

app = main()