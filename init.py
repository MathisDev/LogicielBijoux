#!/usr/bin/python3

import sqlite3
from sqlite3 import Error

db = "./base.db"

def creer_base(db):
	try:
		li = sqlite3.connect(db)
		li.close()
		return 1

	except Error as e:
		print(e)
		return -1

def peupler_base(db):

	sql = ["CREATE TABLE Clients (identifiant_Clients INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nom_client TEXT NOT NULL, type_client TEXT);","CREATE TABLE Commandes (identifiants_Commandes INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, identifiant_Clients INTEGER, FOREIGN KEY(identifiant_Clients) REFERENCES Clients(identifiant_Clients));"]
	li = sqlite3.connect(db)

	if li:
		cons = li.cursor()

		for i in range(len(sql)):
			cons.execute(sql[i])
		li.commit()
		li.close()
		return 1

	else :
		return -1

if __name__ == '__main__':
	if creer_base(db) == 1:
		peupler_base(db)



