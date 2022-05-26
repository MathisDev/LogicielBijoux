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
			self.top = tk.Toplevel()
			self.top.geometry("400x200")
			self.label1 = tk.Label(self.top,text="New Window").pack()


		self.btn1 = tk.Button(self.window,text=". . .",bg="#666363",bd=0,command=newWindow).place(x=1030,y=130)

		self.window.mainloop()



		

app = main()