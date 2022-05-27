# /usr/bin/python3

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

		self.titrerestor=tk.Label(self.frame1,text=" REST'OR ",font= 12,bg="#DFDFDC").place(x=500,y=15)

		self.searchBarre =tk.Entry(self.window,width=30,font = ('courier', 12, 'bold')).place(x=400,y=130)   

		def prolongBtn():
			self.btntest = tk.Button(self.window,text="Nouvelle Commande",width=18,bd=0,command=newWindow).place(x=895,y=119)
			self.btntest = tk.Button(self.window,text="Nouveaux Client",width=18,bd=0,command=newWindow1).place(x=895,y=139)


		def newWindow():
			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("300x700")

			self.titreWindow = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)

			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=40)
			self.preDateDepot = tk.Entry(self.top,width=30).place(x=100 ,y=40)

			self.titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=70)
			self.preNumCommand = tk.Entry(self.top,width=30).place(x=100 ,y=70)

			self.titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=100)
			self.preNom = tk.Entry(self.top,width=30).place(x=100 ,y=100)

			self.titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=130)
			self.prePrenom = tk.Entry(self.top,width=30).place(x=100 ,y=130)

			self.titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=160)
			self.preAdress = tk.Entry(self.top,width=30).place(x=100 ,y=160)

			self.titreCp = tk.Label(self.top,text="C.P",bg="#EEEC7C").place(x=10 , y= 190)
			self.preCp = tk.Entry(self.top,width=30).place(x=100 , y= 190)

			self.titreVille = tk.Label(self.top,text="Ville",bg="#EEEC7C").place(x=10 , y= 220)
			self.preVille = tk.Entry(self.top,width=30).place(x=100 , y= 220)

			self.titreAdressMail = tk.Label(self.top,text="Adresse mail",bg="#EEEC7C").place(x=10 , y= 250)
			self.preAdressMail = tk.Entry(self.top,width=30).place(x=100 , y= 250)

			self.titreTel = tk.Label(self.top,text="Tel",bg="#EEEC7C").place(x=10 , y= 280)
			self.preTel = tk.Entry(self.top,width=30).place(x=100 , y= 280)

			self.titrePrixConvenue = tk.Label(self.top,text="Prix Convenue",bg="#EEEC7C").place(x=10 , y=320)
			self.prePrixConvenue = tk.Entry(self.top,width=30).place(x=100,y=320)

			self.titreDevis= tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=350)
			self.preDevis = tk.Entry(self.top,width=30).place(x=100,y=350)

			self.titreAcompt = tk.Label(self.top,text="Devis",bg="#EEEC7C").place(x=10 , y=380)
			self.preAcompt = tk.Entry(self.top,width=30).place(x=100,y=380)

			self.titreRestePaye = tk.Label(self.top,text="Reste a Payer",bg="#EEEC7C").place(x=10 , y=410)
			self.preResterPaye = tk.Entry(self.top,width=30).place(x=100,y=410)

			self.btnValide = tk.Button(self.top,text="Valider",bg="#666363",bd=0,command=getAllvar).place(x=200,y=600)
		
		# La fonction getALL var ne run pas mais juste le principe 
		def getAllvar():
			dateDepot = self.preDateDepot.get() 
			numCommand = self.preNumCommand.get()
			nom = self.preNom.get()
			prenom = self.prePrenom.get()					
			adress = self.preAdress.get()			
			cp = self.preCp.get() 		
			ville = self.preVille.get()					
			adreeMail = self.preAdressMail.get()					
			tel = self.preTel.get()					
			prixConvenue = self.prePrixConvenue.get()
			devis = self.preDevis()
			acompt = self.preAcompt()
			restPaye = self.preRestePaye.get()


		def newWindow1():
			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("300x700")


		self.btn1 = tk.Button(self.window,text="+",bg="#666363",width=3,height=1,bd=0,font=2,command=prolongBtn).place(x=900,y=70)

		self.window.mainloop()



		

app = main()