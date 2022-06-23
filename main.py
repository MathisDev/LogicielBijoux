# /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from functools import partial
import sqlite3

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
			self.topShowCommande = tk.Toplevel(bg="#8E44AD")
			self.topShowCommande.geometry("400x700")
			
			cur = conn.cursor()
			rqt = "SELECT * FROM Clients;"
			cur.execute(rqt)
			rows = cur.fetchall()  
			
			"""  
			for row in rows:
				print(row)        
			cur.close()
    		"""
		
			l=["ID", "Entreprise", "Nom", "Prénom", "Adresse mail", "Solde du compte", "Numéro de téléphone"]
		
			self.frameClientsInfo = tk.Frame(self.topShowCommande,bg="grey",height=233,width=400).place(x=0,y=0)
			self.LabelIdCommande = tk.Label(self.topShowCommande,text="Clients",bg="grey").place(x=20,y=20)

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
			self.btnValide = tk.Button(self.top,text="modification",bg="#666363",bd=0,command=modif).place(x=200,y=10)

			
		def homeListe(self):
			self.txt = 'Le nom de la commande '
			bg1 = "grey"
			bg2 = "#D34514"
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg=bg2,relief="ridge",command=partial(showCommande,self.txt)).place(x=260,y=250)
			self.commandeShowHome1 = tk.Button(window,text=self.txt,width=19,height=2,bg='orange',relief="ridge",command=partial(showClients,self)).place(x=260,y=300)
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

			self.top = tk.Toplevel()
			self.top.title("Nouvelle commande")
			self.top.geometry("400x700")

			data = Data() # Instance de Data() qui va nous permettre de stocker les str récupérées grâce à main()
					
			data.idCommande=tk.Entry(self.top).place(x=l ,y=40)
			data.dateDepot=tk.Entry(self.top).place(x=l ,y=70)
			data.adresse=tk.Entry(self.top).place(x=l ,y=100)
			data.cp=tk.Entry(self.top).place(x=l ,y=130)
			data.ville=tk.Entry(self.top).place(x=l ,y=160)
			data.idClient=tk.Entry(self.top).place(x=l , y= 190)

			def getVarCommande(self, data):
				#print(data.dateDepot.get()) Exemple d'un .get() fonctionnel
				rqt = "INSERT INTO Commandes (idCommande, dateDepot, adresse, cp, ville, idClient) VALUES ('"+data.idCommande.get()+"','"+data.dateDepot.get()+"','"+data.adresse.get()+"','"+data.cp.get()+"','"+data.ville.get()+"','"+data.idClient.get()+"')"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
        								
			btnValide = tk.Button(self.top, text='Valider', command=partial(getVarCommande, self, data)).grid(row=6,column=1,sticky=tk.W,pady=4)

		# Top Level Clients #
		def windowClient(self):
			w = 25
			l = 120
			color = "#52575B"

			self.top = tk.Toplevel()
			self.top.title("Nouveau client")
			self.top.geometry("400x700")
			
			data = Data()
			
			l = ["Nom", "Prénom", "Entreprise", "@mail", "Solde du compte", "Téléphone"]

			for i in range(len(l)):
				tk.Label(window, text=l[i]).grid(row=i)
    
			data.nom=tk.Entry(self.top)
			data.prenom=tk.Entry(self.top)
			data.entreprise=tk.Entry(self.top)
			data.mail=tk.Entry(self.top)
			data.solde=tk.Entry(self.top)
			data.telephone=tk.Entry(self.top)

			data.nom.grid(row=0, column=1)
			data.prenom.grid(row=1, column=1)
			data.entreprise.grid(row=2, column=1)
			data.mail.grid(row=3, column=1)
			data.solde.grid(row=4, column=1)
			data.telephone.grid(row=5, column=1)

			def getVarClients(self, data):
				#print(data.__dict__) Affiche les attributs de data (classe Data()) pour le deboguage
				rqt = "INSERT INTO Clients (clientNom,clientPrenom,firmeNom,adresseMail,compte,telephone) VALUES ('"+data.nom.get()+"','"+data.prenom.get()+"','"+data.entreprise.get()+"','"+data.mail.get()+"',"+data.solde.get()+","+data.telephone.get()+");"
				cur = conn.cursor()
				cur.execute(rqt)
				conn.commit()
				cur.close()
        		
			btnValide = tk.Button(self.top, text='Valider', command=partial(getVarClients, self, data)).grid(row=6,column=1,sticky=tk.W,pady=4)

		def windowControle():
			color = '#AAD1CA' 
			self.windowControle = tk.Toplevel(bg=color)
			self.windowControle.title("Nouveaux Controle")
			self.windowControle.geometry("400x700")
			
			entryControle = tk.Entry(self.windowControle,width=10,bg=color).place(x=20,y= 20)


		def prolongBtn():
			btnprolong1 = tk.Button(window,text="Nouvelle Commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowCommande,self),width=18).place(x=1165,y=147)
			btnprolong2 = tk.Button(window,text="Nouveaux Client",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=173)
			opencommandeWindow = tk.Button(window,text="New Commande",bg="#666363",relief="ridge",highlightbackground = "#666363",command = partial(windowClient,self),width=18).place(x=1165,y=203)
	


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