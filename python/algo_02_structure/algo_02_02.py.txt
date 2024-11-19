nom : conversion temporelle
variables numériques : nbheure, nbminutes, nbsecondes, totalsecondes
DEBUT
    Afficher "indiquez le nombre d'heures : "
    Saisir nbheure
    Afficher "indiquez le nombre de minutes : "
    Saisir nbminutes
    Afficher "indiquez le nombre de secondes : "
    Saisir nbsecondes
    totalsecondes <- (nbheure*3600)+(nbminutes*60)+nbsecondes
    Afficher "Cela représente un total de ", totalsecondes, "secondes"
FIN    