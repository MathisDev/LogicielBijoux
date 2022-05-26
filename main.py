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

		self.frameSearch = tk.Frame(self.window , width=200 , height= 800, bg="grey")
		self.frameSearch.grid()

		self.searchBarre = tk.Entry(self.frameSearch,bg="white",width=60).grid(padx=(350 , 350), pady=(50 , 50))

		def newWindow():
			self.top = tk.Toplevel(bg="#EEEC7C")
			self.top.geometry("300x700")

			self.titreWindow = tk.Label(self.top,text="Fiche Commande",bg="#EEEC7C",font=10).place(x=30 , y=0)

			self.titreDepotDate = tk.Label(self.top,text="Date de depot",bg="#EEEC7C").place(x=10 , y=40)
			self.dateDepot = tk.Entry(self.top,width=30).place(x=100 ,y=40)

			self.titreNumCommande = tk.Label(self.top,text="n ° :",bg="#EEEC7C").place(x=10 , y=70)
			self.numCommand = tk.Entry(self.top,width=30).place(x=100 ,y=70)

			self.titreNom = tk.Label(self.top,text="Nom :",bg="#EEEC7C").place(x=10 , y=100)
			self.nom = tk.Entry(self.top,width=30).place(x=100 ,y=100)

			self.titrePrenom = tk.Label(self.top,text="Prénom",bg="#EEEC7C").place(x=10 , y=130)
			self.prenom = tk.Entry(self.top,width=30).place(x=100 ,y=130)

			self.titreAdress = tk.Label(self.top,text="Adresse",bg="#EEEC7C").place(x=10 , y=160)
			self.adress = tk.Entry(self.top,width=30).place(x=100 ,y=160)

			self.btnValide = tk.Button(self.top,text="Valider",bg="#666363",bd=0,command=newWindow).place(x=200,y=600)

		self.btn1 = tk.Button(self.window,text=". . .",bg="#666363",bd=0,command=newWindow).place(x=1030,y=130)

		self.window.mainloop()



		

app = main()