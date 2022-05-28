#!/usr/bin/python3

import sqlite3
from sqlite3 import Error

db = "./base.db"

def creer_base(db):

	sql = ["CREATE TABLE Clients (idClient INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firmeNom TEXT, clientNom TEXT, clientPrenom TEXT, adresseMail TEXT, compte REAL, telephone INTEGER);","CREATE TABLE Commandes (idCommande INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, dateDepot INTEGER, adresse TEXT, cp INTEGER, ville TEXT, idClient INTEGER, FOREIGN KEY (idClient) REFERENCES Clients(idClient));"]
	li = sqlite3.connect(db)

	if li:
		cons = li.cursor()

		for i in range(len(sql)):
			cons.execute(sql[i])
		li.commit()
		li.close()

def verifier_base(db):

	sql = "SELECT * from sqlite_master;"
	li = sqlite3.connect(db)
	
	if li:
		cons = li.cursor()
		cons.execute(sql)
		resp = cons.fetchall()
		li.close()
		return resp


if __name__ == '__main__':
	if peupler_base(db):
		schema = verifier_base(db)


