nom : le plus grand nombre parmi trois nombres
variables numériques : nb1, nb2, nb3
DEBUT
    Afficher "Saisissez le premier nombre : "
    Saisir nb1
    Afficher "Saisissez le deuxième nombre : "
    Saisir nb2
    Afficher "Saisissez le troisième nombre : "
    Saisir nb3
    Si nb1>nb2 et nb1>nb3 alors
        Afficher "Le plus grand nombre est : ",nb1
    Sinon
        Si nb2>nb1 et nb2>nb3 alors
            Afficher "Le plus grand nombre est : ",nb2
        Sinon
            Afficher "Le plus grand nombre est : ",nb3
        Fin Si
    Fin Si
FIN