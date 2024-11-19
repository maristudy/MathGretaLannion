"""
https://docs.python.org/fr/3/howto/sorting.html
Un tri ascendant simple est très facile : il suffit d'appeler la fonction sorted(). Elle renvoie une nouvelle liste triée :
>>>

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
"""



"""
#question 1 : saisir 30 notes
Nom : saisie des 30 notes
variables numériques : i, tabNotes(30)

DEBUT
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
    Fin Pour    
FIN


#question 2 : saisir 30 notes, calcul et affiche la moyenne
Nom : saisie des 30 notes
variables numériques : i, tabNotes(30), moyenne, somme

DEBUT
    somme <- 0
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
        somme = somme + tabNotes[i]
    Fin Pour
    moyenne <- somme / 30
    Afficher moyenne
FIN



#question 3 : saisir 30 notes, min et max
Nom : saisie des 30 notes, calcul du min et du max
variables numériques : i, tabNotes(30), min, max

DEBUT
    max <- 0
    min <- 20
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
        Si tabNotes[i] > max alors
            max <- tabNotes[i]
        Fin Si
        Si tabNotes[i] < min alors
            min <- tabNotes[i]
        Fin Si
    Fin Pour
    Afficher <<min = >>,min,<< max = >>,max
FIN




#question 4 : saisir 30 notes, min, max, etendue ( programme )
Nom : saisie des 30 notes, calcul du min et du max
variables numériques : i, tabNotes(30), min, max, etendue

DEBUT
    max <- 0
    min <- 20
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
        Si tabNotes[i] > max alors
            max <- tabNotes[i]
        Fin Si
        Si tabNotes[i] < min alors
            min <- tabNotes[i]
        Fin Si
    Fin Pour
    etendue <- max - min
    Afficher <<etendue = >>,etendue
FIN
"""
"""
max=0
min=20
tabNotes=[0]*30
for i in range(0,30):
    tabNotes[i]=float(input("notes : "))
    if tabNotes[i] > max:
        max = tabNotes[i]
    if tabNotes[i] < min:
        min = tabNotes[i]
print("etendue = ",(max-min))

"""
"""
#question 5 : saisir 30 notes, notes sous 10 ( programme )
Nom : saisie des 30 notes, calcul du min et du max
variables numériques : i, tabNotes(30), noteSous10

DEBUT
    noteSous10 <- 0
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
        Si tabNotes[i] < 10 alors
            noteSous10 <- noteSous10 + 1
        Fin Si
    Fin Pour
    Afficher <<nombre de notes sous 10 = >>,noteSous10
FIN
"""
"""
noteSous10=0
tabNotes=[0]*30
for i in range(0,30):
    tabNotes[i]=float(input("notes : "))
    if tabNotes[i] < 10:
        noteSous10 = noteSous10 + 1
print("nombre de notes sous 10 = ",noteSous10)


"""
"""
#question 6 : saisir 30 notes, mediane ( programme )
Nom : saisie des 30 notes, calcul du min et du max
variables numériques : i, tabNotes(30), mediane

DEBUT
    noteSous10 <- 0
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
    Fin Pour
    Trier(tabNotes,croissant)
    mediane <- (tabNotes(14)+tabNotes(15))/2
    Afficher <<mediane = >>,mediane
FIN
"""
"""
# https://docs.python.org/fr/3/howto/sorting.html

tabNotes=[0]*30
for i in range(0,30):
    tabNotes[i]=float(input("notes : "))
sorted(tabNotes)
mediane = (tabNotes[14]+tabNotes[15])/2
print("mediane = ",mediane)


"""
"""
#question 7 : saisir 30 notes, moyenne elaguee ( programme )
Nom : saisie des 30 notes, calcul du min, du max et de la moyenne elaguee
variables numériques : i, tabNotes(30), min, max, somme, nbNotes

DEBUT
    max <- 0
    min <- 20
    somme <- 0
    nbNotes<- 0
    Pour i allant de 0 à 29
        Saisir tabNotes[i]
        Si tabNotes[i] > max alors
            max <- tabNotes[i]
        Fin Si
        Si tabNotes[i] < min alors
            min <- tabNotes[i]
        Fin Si
    Fin Pour
    Pour i allant de 0 à 29
        Si tabNotes[i] != min et tabNotes[i] != max alors
            somme <- somme + tabNotes[i]
            nbNotes <= nbNotes + 1
        Fin Si
    Fin Pour
    Afficher <<moyenne elaguee = >>,somme / nbNotes
FIN
"""
"""

max=0
min=20
somme=0
nbNotes=0
tabNotes=[0]*30
for i in range(0,30):
    tabNotes[i]=float(input("notes : "))
    if tabNotes[i] > max:
        max = tabNotes[i]
    if tabNotes[i] < min:
        min = tabNotes[i]
for i in range(0,30):
    if tabNotes[i]!= min and tabNotes[i]!=max:
        somme=somme+tabNotes[i]
        nbNotes=nbNotes+1
print("moyenne elaguee : ",(somme / nbNotes))

"""




