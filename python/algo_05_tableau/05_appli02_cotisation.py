nom : calcul cotisation
variables numériques : tabloCategorie, i
variables alphanumérique : tabloTarif, reponse

DEBUT
    tabloCategorie[0] <- "Senior"
    tabloCategorie[1] <- "Junior"
    tabloCategorie[2] <- "Cadet"
    tabloCategorie[3] <- "Minime"
    tabloCategorie[4] <- "Benjamin"
    tabloCategorie[5] <- "Poussin"
    tabloCategorie[6] <- "Pousset"
    tabloTarif[0] <- 233
    tabloTarif[1] <- 203
    tabloTarif[2] <- 175
    tabloTarif[3] <- 149
    tabloTarif[4] <- 125
    tabloTarif[5] <- 103
    tabloTarif[6] <- 83
    Afficher "Quelle est votre catégorie ? "
    Saisir reponse
    Pour i allant de 0 à 6
        Si reponse = tabloCategorie[i] alors
            Afficher "votre tarif est de : ",tabloTarif[i]," euros"
        Fin Si
    Fin Pour
FIN
