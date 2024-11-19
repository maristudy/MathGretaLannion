"""
nom : petit chevaux
variable numérique : nb

DEBUT
    Répeter
        nb <- nombre aléatoire entier compris entre 1 et 6
    Jusqu'à nb = 6
FIN
"""

from random import *
nb=0
while(nb != 6):
    nb=randint(1,6)
    print("nb=",nb)

