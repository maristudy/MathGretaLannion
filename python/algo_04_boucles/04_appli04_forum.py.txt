"""
nom : mot de passe
variables alphanumeriques : mdpSaisie, mdp

DEBUT
    mdp <- "mot de passe"
    Répéter
        Afficher "Donnez le mot de passe du forum : "
        Saisir mdpSaisie
    Jusqu'à mdpSaisie = mdp
FIN



mdp="mot de passe"
mdpSaisie=input("Donnez le mot de passe du forum : ")
while (mdp != mdpSaisie) :
    mdpSaisie=input("Donnez le mot de passe du forum : ")
print("Bienvenue sur le forum")




nom : mot de passe limité à 3
variables alphanumeriques : mdpSaisie, mdp, compteur

DEBUT
compteur <- 1
    Répéter
        Afficher "Donnez le mot de passe du forum : "
        Saisir mdpSaisie
        compteur <- compteur+1
    Jusqu'à mdpSaisie = mdp ou compteur >=3
FIN
"""

compteur=1
trouve=0
mdp="mot de passe"
mdpSaisie=input("Donnez le mot de passe du forum : ")
while (mdp != mdpSaisie and compteur<3 ) :
    mdpSaisie=input("Donnez le mot de passe du forum : ")
    compteur=compteur+1
    if(mdp==mdpSaisie):
        trouve=1
if(trouve==1):
    print("Bienvenue sur le forum")
else :
    print("tu as épuisé tes 3 essais")        





