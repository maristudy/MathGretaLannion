# Un premier algorithme

# étape 1 : Choisir un nombre nombre
# étape 2 : Lui soustraire 4
# étape 3 : Multiplier le résultat obtenu par le nombre n choisi
# étape 4 : Ajouter 4 à ce produit
# étape 5 : Afficher le résultat

# 1/ Faire fonctionner cet algorithme pour les entiers n compris entre 0 et 5

# étape 1				n=0		n=1		n=2		n=3		n=4		n=5
# étape 2				-4		-3		-2		-1		0		1
# étape 3				0		-3		-4		-3		0		5
# étape 4				4		1		0		1		4		9

# 2/ Quelle remarque peut-on faire ?

# Les nombres sont tous positifs. Nous avons une valeur nulle pour n=2. Les valeurs sont identiques pour n=0 et n=4 ainsi que pour n=1 et n=3.

# 3/ Traduire cet algorithme en pseudo-code

# nom : algorithme de calcul
# variables numériques : n, resultat, tempo
# DEBUT
# 	Afficher "Saisir un nombre entier n : "
# 	Saisir n
# 	tempo <- n - 4
# 	tempo <- tempo * n
# 	resultat <- tempo + 4
# 	Afficher resultat
# FIN

# 4/ Programmer en Python l'algorithme de calcul

n=int(input("Saisissez un nombre : "))
tempo=n-4
tempo=tempo*n
resultat=tempo+4
print(resultat)