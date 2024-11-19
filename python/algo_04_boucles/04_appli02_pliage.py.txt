"""
nom : pliage
variables numériques : epaisseur, eiffel, n, h

DEBUT
    epaisseur <- 0.16
    eiffel <- 324000
    n <- 1
    h <- epaisseur
    Tant Que h<eiffel
        h <- h*2
        n <- n*2
    Fin Tant Que
    Afficher n
FIN
"""

epaisseur=0.16 # epaisseur d'une feuille en mm
eiffel=324000  # hauteur de la tour Eiffel en mm
n=1			   # nombre de pliage
h=epaisseur    # épaisseur totale du pliage
while(h<eiffel):
    h=h*2
    n=n*2
    print("		pour n=",n," on a h=",h)
print("il faut plier la feuille ",n," fois pour dépasser la hauteur de la tour Eiffel")