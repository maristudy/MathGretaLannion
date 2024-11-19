1/
nom : jeu de dés
variables numériques : somme, dé, points, nbdé

DEBUT
    points <- 10
    somme <- 0
    pour nbdé allant de 1 à 10 
        dé <- nombre aléatoire entier compris entre 1 et 6
        somme <- somme + dé
    Fin pour
    Si (somme%2) = 0 alors
        points <- points + 1
    sinon
        points <- points - 2
    Fin si
    Afficher points
FIN

2/
nom : jeu de dés 5 parties
variables numériques : somme, dé, points, nbdé, nbpartie

DEBUT
    points <- 10
    somme <- 0
    pour nbpartie allant de 1 à 5
        pour nbdé allant de 1 à 10 
            dé <- nombre aléatoire entier compris entre 1 et 6
            somme <- somme + dé
        Fin pour
        Si (somme%2) = 0 alors
            points <- points + 1
        sinon
            points <- points - 2
        Fin si
        somme <- 0
    Fin pour    
    Afficher points
FIN







3/
nom : jeu de dés points positifs
variables numériques : somme, dé, points, nbdé, nbpartie

DEBUT
    points <- 10
    somme <- 0
    nbpartie <- 0
    tant que points > 0
        nbpartie <- nbpartie + 1
        pour nbdé allant de 1 à 10 
            dé <- nombre aléatoire entier compris entre 1 et 6
            somme <- somme + dé
        Fin pour
        Si (somme%2) = 0 alors
            points <- points + 1
        sinon
            points <- points - 2
        Fin si
        somme <- 0
        Afficher "partie ",nbpartie," il reste ",points," points"
    Fin tant que    
FIN


