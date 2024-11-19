"""
A première approche

1 travail par écrit

a) lister les variables de A1 et leur type
   nombresecret : variable numérique
   proposition : variable numérique
    
b) rôle de la ligne 1
   initialiser la variable nombresecret.
   C'est un nombre aléatoire compris entre 1 et 10 000 

c) Quelle est la condition qui doit être vérifié pour effectuer la ligne 9
   On effectue la ligne 9 si proposition n'est pas supérieur strictement à nombresecret et
   si proposition n'est pas inférieur strictement à nombre secret.
   Cela revient à dire que proposition est égale à nombresecret

d) Quel est le rôle de cet algorithme
   Le rôle de cet algorithme est de tirer un nombre aléatoire compris entre 1 et 10 000.
   L'utilisateur doit deviner ce nombre.
   Puis on demande à l'utilisateur de saisir un nombre. Si les nombres sont identiques
   alors on indique que la personne a gagné. Dans le cas contraire on indique
   si le nombre à deviner est plus grand ou plus petit que le nombre de l'utilisateur
   
e) Ecrire un nouvel algorithme A2 qui, à partir d'un nombre secret compris
   entre 1 et 10 000, demande au joueur de faire des propositions
   tant qu'il n'a pas trouvé et en indiquant, à chaque fois,
   si le nombre secret est plus petit ou plus grand. L'algorithme devra indiquer
   à la fin en combien d'essais le nombre secret a été trouvé
   ( on pourra mettre en place un compteur ).

nom : A2
variables numériques : nombresecret, proposition, compteur

DEBUT
    nombresecret <- hasard(1,10 000)
    proposition <- -1
    compteur <- 0
    tant que ( proposition != nombresecret ) 
        saisir proposition
        compteur <- compteur + 1
        si ( proposition > nombresecret ) alors
            Afficher "le nombre secret est plus petit"
        sinon
            si (proposition < nombresecret ) alors
                Afficher "le nombre secret est plus grand"
            sinon
                afficher "bravo ! Vous avez trouvé le nombre secret !"
            Fin si
        Fin si
    Fin tant que
    Afficher "Vous avez trouvé après ",compteur," essais "
FIN











f) Modifier l'algorithme A2 en un algorithme A3
   pour qu'il impose, en plus, que le nombre secret
   soit trouvé en 15 essais maximum.

nom : A3
DEBUT
    nombresecret <- hasard(1,10 000)
    proposition <- -1
    compteur <- 0
    tant que ( ( proposition != nombresecret ) et ( compteur < 15 ) )
        saisir proposition
        compteur <- compteur + 1
        si ( proposition > nombresecret ) alors
            Afficher "le nombre secret est plus petit"
        sinon
            si (proposition < nombresecret ) alors
                Afficher "le nombre secret est plus grand"
            sinon
                afficher "bravo ! Vous avez trouvé le nombre secret !"
            Fin si
        Fin si
    Fin tant que
    Si proposition == nombresecret
        Afficher "Vous avez trouvé après ",compteur," essais "
    Sinon
        Afficher "Vous n'avez pas trouvé après 15 essais "    
FIN
"""







# 2 travail sur poste informatique

#A1
"""
from random import *
nombresecret = randint(1,10000)
print(nombresecret)
proposition=int(input("Faite votre proposition : "))
if (proposition > nombresecret):
    print("Le nombre secret est plus petit")
else:
    if (proposition < nombresecret ):
        print("Le nombre secret est plus grand")
    else:
        print("Bravo ! vous avez trouvé le nombre secret !")
"""





"""
#A2
from random import *
nombresecret = randint(1,10000)
proposition=-1
compteur=0
print(nombresecret)
while ( proposition != nombresecret ) :
    proposition=int(input("Faite votre proposition : "))
    compteur=compteur+1
    if (proposition > nombresecret):
        print("Le nombre secret est plus petit")
    else:
        if (proposition < nombresecret ):
            print("Le nombre secret est plus grand")
        else:
            print("Bravo ! vous avez trouvé le nombre secret !")
print( "Vous avez trouvé après ",compteur," essais ")
"""







"""
#A3
from random import *
nombresecret = randint(1,10000)
proposition=-1
compteur=0
print(nombresecret)
while ( proposition != nombresecret and compteur <15 ) :
    proposition=int(input("Faite votre proposition : "))
    compteur=compteur+1
    if (proposition > nombresecret):
        print("Le nombre secret est plus petit",compteur)
    else:
        if (proposition < nombresecret ):
            print("Le nombre secret est plus grand",compteur)
        else:
            print("Bravo ! vous avez trouvé le nombre secret !")
if (proposition == nombresecret):
    print( "Vous avez trouvé après ",compteur," essais ")
else :
    print( "Vous n'avez pas trouvé après 15 essais ")
    
"""





"""


B Pour les braves ! le nombre secret, le retour !
1 travail par écrit

a) Pour être efficace, elle devra commencer par le milieu de l'intervalle [1;10000].
Il s'agit de la valeur 5000

b) Nous allons utiliser un raisonnement par dichotomie.
Si la valeur est trop petite, alors on prend le milieu de l'intervalle [valeur proposée;maximum possible]
Si la valeur est trop grande, alors on prend le milieu de l'intervalle [minimum possible;valeur proposée]

nom : B1
DEBUT
    Saisir min_possible
    Saisir max_possible
    proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
    Afficher proposition
FIN

c) min_possible, max_possible, proposition sont des variables numériques

d) cet algorithme permet de calculer le nombre au milieu de l'intervalle [minimum possible;maximum possible]

e) Ecrire un algorithme B2 qui affiche la proposition de la machine,
    puis où l'utilisateur dit si le nombre secret est plus petit,
    plus grand ou égal à cette proposition. La machine doit ensuite,
    selon la réponse de l'utilisateur, lui faire une nouvelle proposition.

"""
"""
nom : B2
variables numériques : min_possible, max_possible, proposition

DEBUT
    min_possible <- 1
    max_possible <- 10000
    proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
    Afficher proposition
    Saisir reponse
    Si reponse = "+" #le nombre est plus grand
        min_possible <- proposition
        proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
        Afficher proposition
    Sinon
        Si reponse = "-" #le nombre est plus petit
            max_possible <- proposition
            proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
            Afficher proposition
        Sinon
            Afficher "Youpi j'ai gagné"
        Fin si
    Fin si       
FIN
"""

"""

f) Ecrire un algorithme B3 qui demande à la machine des propositions tant qu'elle n'a pas trouvé le nombre secret.

nom : B3
DEBUT
    min_possible <- 1
    max_possible <- 10000
    proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
    Afficher proposition
    Saisir reponse
    tant que reponse != "="
        Si reponse = "+" #le nombre est plus grand
            min_possible <- proposition
            proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
        Sinon #le nombre est plus petit
            max_possible <- proposition
            proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
        Fin si
        Afficher proposition
        Saisir reponse            
    Fin tant que
    Afficher "Youpi j'ai gagné"
FIN
"""





"""


# 2 travail sur poste informatique

a) Implémenter et tester les algorithmes B1, B2, B3
"""
"""
# B1
from math import *

min_possible=int(input("Saisissez le minimum possible : "))
max_possible=int(input("Saisissez le maximum possible : "))
proposition = floor((min_possible+max_possible)/2)
print(proposition)
"""
"""
DEBUT
    min_possible <- 1
    max_possible <- 10000
    proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
    Afficher proposition
    Saisir reponse
    Si reponse = "+" #le nombre est plus grand
        min_possible <- proposition
        proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
        Afficher proposition
    Sinon
        Si reponse = "-" #le nombre est plus petit
            max_possible <- proposition
            proposition <- PartieEntiere ( (min_possible + max_possible) / 2 )
            Afficher proposition
        Sinon
            Afficher "Youpi j'ai gagné"
        Fin si
    Fin si       
FIN
"""

"""
# B2
from math import *
min_possible=1
max_possible=10000
proposition=floor ( (min_possible + max_possible) / 2 )
print( proposition )
reponse=input("Donnez votre réponse ")
if reponse == "+" :
    min_possible = proposition
    proposition=floor ( (min_possible + max_possible) / 2 )
    print( proposition )
elif reponse == "-":
    max_possible = proposition
    proposition = floor ( (min_possible + max_possible) / 2 )
    print( proposition )
else:
    print( "Youpi j'ai gagné" )
"""
"""

#nom : B3
from math import *
min_possible=1
max_possible=10000
proposition=floor ( (min_possible + max_possible) / 2 )
print( proposition )
reponse=input("Donnez votre réponse ")
while (reponse != "=") :
    if (reponse == "+") :
         min_possible = proposition
         proposition=floor ( (min_possible + max_possible) / 2 )
    else :
           max_possible = proposition
           proposition = floor ( (min_possible + max_possible) / 2 )
    print( proposition )
    reponse=input("Donnez votre réponse ")           
print( "Youpi j'ai gagné" )



b) Modifier le programme B3 pour qu'il impose à l'ordinateur de trouver en 15 essais maximum
"""
#nom : B3 bis
from math import *
min_possible=1
max_possible=10000
compteur=1
proposition=floor ( (min_possible + max_possible) / 2 )
print( proposition )
reponse=input("Donnez votre réponse ")
while (reponse != "=") and (compteur < 15):
    compteur=1+compteur
    if (reponse == "+") :
         min_possible = proposition
         proposition=floor ( (min_possible + max_possible) / 2 )
    else :
           max_possible = proposition
           proposition = floor ( (min_possible + max_possible) / 2 )
    print( proposition )
    reponse=input("Donnez votre réponse ")           
if reponse == "=" :
    print( "Youpi j'ai gagné" )
else:
    print( "Perdu" )


