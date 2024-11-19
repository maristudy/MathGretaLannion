a = ages < 25										a			non a
b = ages permis >	 2						b	 orange			vert
                                        non b	  rouge			orange
                                        
nom : nom du tarif de l'assurance automobile
variables numériques : age, anneePermis, anneEnCours
DEBUT
    Afficher "Indiquer votre âge : "
    Saisir age
    Afficher "Indiquer l'année d'obtention de votre permis : "
    Saisir anneePermis
    Afficher "Indiquer l'année en cours : "
    Saisir anneEnCours
    Si age < 25 alors
        Si anneEnCours-anneePermis<=2 alors
            Afficher "Vous êtes en tarif rouge"
        Sinon
            Afficher "Vous êtes en tarif orange"
        Fin Si
    Sinon
        Si anneEnCours-anneePermis<=2 alors
            Afficher "Vous êtes en tarif orange"
        Sinon
            Afficher "Vous êtes en tarif vert"
        Fin Si
    Fin Si
FIN