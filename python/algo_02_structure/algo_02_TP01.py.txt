nom: rendu monnaie 1 et 2 centimes
variables numériques : nb1cent, nb2cent, somme
DEBUT
    Afficher "Indiquez la somme à rendre "
    Saisir somme
    nb2cent <- somme // 2
    nb1cent <- somme % 2
    Afficher "Cela correspond à ", nb2cent, " pièces de 2 centimes et ", nb1cent, "pièce de 1 centime"
FIN    