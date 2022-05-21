# /usr/bin/python3

import tkinter as tk

class main():
	i = 0
	def __init__(self):
		self.window = tk.Tk()
		self.window.title("Logiciel Gestion Commande")
		self.window.geometry('300x500')

		self.btnA = tk.Button(self.window,text="Color",bg="white",fg="red")
		self.btnA.grid(column=0, row=0 )

		self.btn = tk.Button(self.window,text="clique Her", command=self.clique)
		self.btn.grid(column=2,row=0)

		self.window.mainloop()

	def clique(self):
		print(i)
		if i == 0:
			self.btnA["bg"] = "orange"
			i = 1
		elif i == 1:
			self.btnA["bg"] = "white"
			i = 0


app = main()