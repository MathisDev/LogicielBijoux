import sqlite3


# Variables globales
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# Fonctions
def ajouter():
    table = input("Quelle table voulez-vous modifier ? ")
    
    if table=="Clients":
        nom = input("Nom du client : ")
        prenom = input("Prénom du client : ")
        entreprise = input("Entreprise du client : ")
        email = input("email du client : ")
        tel = input("Numéro de téléphone du client : ")
        rqt = "INSERT INTO Clients (nom,prenom,entreprise,email,téléphone) VALUES ('"+nom+"','"+prenom+"','"+entreprise+"','"+email+"',"+tel+")"
    
    if table=="Commandes":
        id_client = input("ID du client : ")
        date = input("jj/mm/aaaa : ")
        terminée = input("Terminée (Oui/Non) : ")
        adresse = input("Adresse : ")
        code_postale = input("Code postale : ")
        ville = input("Ville : ")
        rqt = "INSERT INTO Commandes (id_client,date,terminée,adresse,code_postale,ville) VALUES ('"+id_client+"','"+date+"','"+terminée+"','"+adresse+"','"+code_postale+"','"+ville+"')"
    
    else:
        return
    print(rqt)
    cur.execute(rqt)
    conn.commit()

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