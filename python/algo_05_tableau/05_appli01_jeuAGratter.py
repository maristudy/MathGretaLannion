nom : jeu à gratter
variables numériques : tablo, somme, max, gain, i, j, compteur

DEBUT
    somme <- 0
    max <- 0
    Pour i allant de 0 à 4
        tablo[i] <- hasard(1,5)
        somme <- somme + tab[i]
        Si tab[i] > max alors
            max <- tab [i]
        Fin Si
    Fin Pour
    Si somme%2 = 0 alors
        gain <- gain + 1
        afficher("La somme est paire, vous gagnez 1 euro")
    Fin Si
    Si max = 2 alors
        gain <- gain + 2
        afficher("Le plus grand nombre est 2, vous gagnez 2 euros")
    Fin Si
    compteur <- 0
    Pour i de 0 à 4
        Pour j de 0 à 4
            Si tab[i] = tab[j] alors
                compteur <- compteur + 1
                Si compteur = 3 alors
                    gain <- gain + 5
                    afficher("3 fois le même nombre, vous gagnez 5 euros")
                    i <- 5
                    j <- 5
                Fin Si
            Fin Si
        Fin Pour
        compteur <- 0
    Fin Pour
    Affiche gain
FIN
















