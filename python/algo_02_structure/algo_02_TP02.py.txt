# nom: rendu monnaie 1, 2, 5, 10, 20, 50 centimes
# variables numériques : nb1cent, nb2cent, nb5cent, nb10cent, nb20cent, nb50cent, reste, somme
# DEBUT
#     Afficher "Indiquez la somme à rendre "
#     Saisir somme
#     nb50cent <- somme //50
#     reste <- somme % 50
#     nb20cent <- reste //20
#     reste <- somme % 20
#     nb10cent <- reste //10
#     reste <- somme % 10
#     nb5cent <- reste //5
#     reste <- somme % 5
#     nb2cent <- reste //2
#     nb1cent <- somme % 2      
#     Afficher nb50cent, " pièces de 50 centimes"
#     Afficher nb20cent, "pièces de 20 centimes"
#     Afficher nb10cent, "pièces de 10 centimes"
#     Afficher nb5cent, "pièces de 5 centimes"
#     Afficher nb2cent, "pièces de 2 centimes"
#     Afficher nb1cent, "pièces de 1 centime"
# FIN

somme=int(input("Indiquez la somme à rendre "))
nb50cent=somme // 50
reste=somme%50
nb20cent=reste // 20
reste=reste%20
nb10cent=reste // 10
reste=reste%10
nb5cent=reste // 5
reste=reste%5
nb2cent=reste // 2
nb1cent=reste%2
print( nb50cent, " pièces de 50 centimes ")
print( nb20cent, " pièces de 20 centimes ")
print( nb10cent, " pièces de 10 centimes ")
print( nb5cent, " pièces de 5 centimes ")
print( nb2cent, " pièces de 2 centimes ")
print( nb1cent, " pièces de 1 centimes ")