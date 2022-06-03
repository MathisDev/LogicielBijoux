# /usr/bin/python3
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

class main():
	def __init__(self):

		self.window = tk.Tk()
		self.window.title("Logiciel Gestion Commande")
		self.window.geometry('1065x1000')
		self.window.configure(bg="#666363")

		self.frame1 = tk.Frame(self.window , width=1065 , height= 60, bg="#DFDFDC")
		self.frame1.grid()

		self.titrerestor = tk.Label(self.frame1,text=" REST'OR ",font= 12,bg="#DFDFDC").place(x=500,y=15)

		self.searchBarre = tk.Entry(self.window,width=30,font = ('courier', 12, 'bold')).place(x=400,y=130)
		self.frameHomeListe = tk.Frame(self.window,width=700,height=350,bg="white").place(x=200,y=200)

		def showCommande():
				self.topShowCommande = tk.Toplevel(bg="#EEEC7C")
				self.topShowCommande.geometry("400x700")
				self.LabelIdCommande = tk.Label(self.topShowCommande,text="L'Id Commande",bg="#EEEC7C").place(x=20,y=20)

		def showClients():
				self.topShowCommande = tk.Toplevel(bg="#8E44AD")
				self.topShowCommande.geometry("400x700")
				self.frameClientsInfo = tk.Frame(self.topShowCommande,bg="grey",height=233,width=400).place(x=0,y=0)
				self.LabelIdCommande = tk.Label(self.topShowCommande,text="L'Id Commande",bg="grey").place(x=20,y=20)

		def homeListe():
			txt = "Le nom de la commande "
			bg1 = "grey"
			bg2 = "orange"
			
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,bg=bg2,relief="ridge",command=showCommande).place(x=250,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,bg=bg2,relief="ridge",command=showCommande).place(x=250,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,bg=bg1,relief="ridge",command=showCommande).place(x=250,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,bg=bg1,relief="ridge",command=showCommande).place(x=250,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,bg=bg1,relief="ridge",command=showCommande).place(x=250,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=400,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=400,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=400,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=400,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=400,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=550,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=550,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=550,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=550,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=550,y=450)

			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=700,y=250)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=700,y=300)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=700,y=350)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=700,y=400)
			self.commandeShowHome1 = tk.Button(self.window,text=txt,width=19,height=2,relief="ridge",bg=bg1,command=showCommande).place(x=700,y=450)


		homeListe()
		def getAllvar():
			print("function 'getAllvar' for Commande running")
			self.top.destroy()
  			
		def getAllvarClients():
			print("function 'getAllvar' for Clients running")
			self.top.destroy()

		def prolongBtn():
			self.btntest = tk.Button(self.window,text="Nouvelle Commande",bg="#666363",relief="ridge", width=18,command=newWindow).place(x=895,y=119)
			self.btntest = tk.Button(self.window,text="Nouveaux Client",bg="#666363",relief="ridge",width=18,command=newWindow1).place(x=895,y=145)


		def newWindow():
			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("400x700")

			titreWindow = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)

			titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=40)
			preDateDepot = tk.Entry(self.top,width=30).place(x=100 ,y=40)

			titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=70)
			preNumCommand = tk.Entry(self.top,width=30).place(x=100 ,y=70)

			titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=100)
			preNom = tk.Entry(self.top,width=30).place(x=100 ,y=100)

			titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=130)
			prePrenom = tk.Entry(self.top,width=30).place(x=100 ,y=130)

			titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=160)
			preAdress = tk.Entry(self.top,width=30).place(x=100 ,y=160)

			titreCp = tk.Label(self.top,text="C.P",bg="#EEEC7C").place(x=10 , y= 190)
			preCp = tk.Entry(self.top,width=30).place(x=100 , y= 190)

			titreVille = tk.Label(self.top,text="Ville",bg="#EEEC7C").place(x=10 , y= 220)
			preVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)

			titreAdressMail = tk.Label(self.top,text="Adresse mail",bg="#EEEC7C").place(x=10 , y= 250)
			preAdressMail = tk.Entry(self.top,width=30).place(x=100 , y= 250)

			titreTel = tk.Label(self.top,text="Tel",bg="#EEEC7C").place(x=10 , y= 280)
			preTel = tk.Entry(self.top,width=30).place(x=100 , y= 280)

			titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg="#EEEC7C").place(x=10 , y=320)
			prePrixConvenue = tk.Entry(self.top,width=30).place(x=100,y=320)

			titreDevis= tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=350)
			preDevis = tk.Entry(self.top,width=30).place(x=100,y=350)

			titreAcompt = tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=380)
			preAcompt = tk.Entry(self.top,width=30).place(x=100,y=380)

			titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg="#EEEC7C").place(x=10 , y=410)
			preResterPaye = tk.Entry(self.top,width=30).place(x=100,y=410)		

			btnValide = tk.Button(self.top,text="Valider",bg="#666363",bd=0,command=getAllvar).place(x=200,y=600)


		def newWindow1():
			self.top = tk.Toplevel(bg="#8E44AD")
			self.top.geometry("400x700")
			self.labelTitre = tk.Label(self.top,text="Nouveaux Clients",bg="#8E44AD",font=10).place(x=110,y=10)

			self.titreIdClient = tk.Label(self.top,text='Nom du clients',bg="#8E44AD").place(x=10, y= 50)
			self.idClient = tk.Entry(self.top,width=30).place(x=100, y= 50)

			self.titrefirmeNom = tk.Label(self.top,text='Nom Entreprise',bg="#8E44AD").place(x=10, y= 80)
			self.firmeNom = tk.Entry(self.top,width=30).place(x=100, y= 80)

			self.titreClientsNom = tk.Label(self.top,text='Nom',bg="#8E44AD").place(x=10, y= 110)
			self.clientNom = tk.Entry(self.top,width=30).place(x=100, y= 110)

			self.titrePrenom = tk.Label(self.top,text='Prenom',bg="#8E44AD").place(x=10, y= 140)
			self.clientPrenom = tk.Entry(self.top,width=30).place(x=100, y= 140)

			self.titreAdressMail = tk.Label(self.top,text='Adresse Mail',bg="#8E44AD").place(x=10, y= 170)
			self.adresseMail = tk.Entry(self.top,width=30).place(x=100, y= 170)

			self.titreCompte = tk.Label(self.top,text='Compte poids',bg="#8E44AD").place(x=10, y= 200)
			self.compte = tk.Entry(self.top,width=30).place(x=100, y= 200)

			self.titreTelephone = tk.Label(self.top,text='Tel',bg="#8E44AD").place(x=10, y= 230)
			self.telephone = tk.Entry(self.top,width=30).place(x=100, y= 230)

			btnValide = tk.Button(self.top,text="Valider",bg="#666363",bd=0,command=getAllvarClients).place(x=200,y=600)

		def showCommande(txt):
			self.top = tk.Toplevel(bg="#8E44AD")
			self.top.geometry("400x700")
			self.frameClientsInfo = tk.Frame(self.top,bg="grey",height=233,width=400).place()
			self.LabelIdCommande = tk.Label(self.frameClientsInfo,text=txt,bg="grey").place(x=20,y=20)


			 

		self.btn1 = tk.Button(self.window,text="+",bg="#666363",width=3,height=1,bd=0,font=2,command=prolongBtn).place(x=900,y=70)
		



		self.window.mainloop()



		

app = main()