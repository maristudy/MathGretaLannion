"""

Nom : multiplication de matrices
variables numériques : nbLigneA, nbColonneA, nbLigneB, nbColonneB, tabloA, tabloB, tabloC, i, j, k

DEBUT
    Afficher <<quel est le nombre de ligne de la premiere matrice ? >>
    Saisir nbLigneA
    Afficher <<quel est le nombre de colonne de la premiere matrice ? >>
    Saisir nbColonneA
    Afficher <<quel est le nombre de ligne de la seconde matrice ? >>
    Saisir nbLigneB
    Afficher <<quel est le nombre de colonne de la seconde matrice ? >>
    Saisir nbColonneB
    Si nbColonneA=nbLigneB alors:
        Afficher <<Nous allons calculer le produit des deux matrices>>
        Afficher <<Saisie de la premiere matrice>>
        
        Pour i allant de 0 à nbLigneA-1
            Pour j allant de 0 à nbColonneA-1
                Saisir tabloA[i][j]
            Fin Pour
        Fin Pour
        
        Afficher <<Saisie de la seconde matrice>>
        
        Pour i allant de 0 à nbLigneB-1
            Pour j allant de 0 à nbColonneB-1
                Saisir tabloB[i][j]
            Fin Pour
        Fin Pour                 
        
        Pour i allant de 0 à nbLigneA-1 
            Pour j allant de 0 à nbColonneB-1
                tabloC[i][j]=0 #initialisation
                Pour k allant de 0 à nbColonneA-1 #calcul
                    tabloC[i][j]=tabloC[i][j]+(tabloA[i][k]*tabloB[k][j])
                Fin Pour
            Fin Pour
        Fin Pour
        
        Afficher tabloC
    Sinon :
        Afficher <<multiplication impossible>>
    Fin Si
FIN


"""
"""


nbLigneA=int(input("quel est le nombre de ligne de la premiere matrice ? "))
nbColonneA=int(input("quel est le nombre de colonne de la premiere matrice ? "))
nbLigneB=int(input("quel est le nombre de ligne de la seconde matrice ? "))
nbColonneB=int(input("quel est le nombre de colonne de la seconde matrice ? "))
tabloA=[0]*nbLigneA
tabloB=[0]*nbLigneB
tabloC=[0]*nbLigneA
for i in range (0,nbLigneA):
    tabloA[i]=[0]*nbColonneA
for i in range (0,nbLigneB):
    tabloB[i]=[0]*nbColonneB
for i in range (0,nbLigneA):
    tabloC[i]=[0]*nbColonneB    
if nbColonneA==nbLigneB:
    print("Nous allons calculer le produit des deux matrices")
    print("Saisie de la premiere matrice")
    for i in range (0,nbLigneA):
        for j in range (0,nbColonneA):
            tabloA[i][j]=float(input())
    print ("Saisie de la seconde matrice")
    for i in range (0,nbLigneB):
        for j in range (0,nbColonneB):
            tabloB[i][j]=float(input())
    for i in range (0,nbLigneA):
        for j in range (0,nbColonneB):
            tabloC[i][j]=0
            for k in range (0,nbColonneA):
                tabloC[i][j]=tabloC[i][j]+(tabloA[i][k]*tabloB[k][j])
    print("c=",tabloC)
else :
    print("multiplication impossible")


