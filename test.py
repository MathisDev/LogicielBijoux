import sqlite3


# Variables globales
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# Fonctions
def obtenir():

    """
    rqt ne restera pas comme ça, il sera remplacé par une requête construite à partir du menu déroulant
    et de la valeur entrée dans la barre de recherche.
    

    Exemple : la personne clique sur client car elle cherche la fiche d'un client ensuite elle devra entrer son nom dans 
    la barre de recherche ce qui créera une requête SQL de la forme : 
    
    SELECT * FROM Clients WHERE nom='valeur entrée dans la barre de recherche'
    """
    
    l=[]
    rqt = input("Entrez votre requête SQL : ")
    #cur.execute("SELECT nom FROM Clients WHERE nom='Durant'")
    cur.execute(rqt)
    t = cur.fetchall()
    for i in range(len(t)):
        for j in range(len(t[i])):
            l.append(t[i][j])
    print(l)


# Appel de fonctions
obtenir()

# En fin de code, ferme la connexion avec la base de donnée.
cur.close()