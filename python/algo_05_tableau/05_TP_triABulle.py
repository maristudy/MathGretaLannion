"""
Travaux pratiques : tri à bulle

A avec des boucles déterministes
1 travail par écrit
a /
On saisit 5 ; 24 ; 22 ; 40 ; 13; 31

n=6
j		i		tab
                  0   1   2    3    4    5       
0		0		[5 ; 24 ; 22 ; 40 ; 13 ; 31]
0		1		[5 ; 22 ; 24 ; 40 ; 13 ; 31]
0		2		[5 ; 22 ; 24 ; 40 ; 13 ; 31]
0		3		[5 ; 22 ; 24 ; 13 ; 40 ; 31]
0		4		[5 ; 22 ; 24 ; 13 ; 31 ; 40]
1		0		[5 ; 22 ; 24 ; 13 ; 31 ; 40]
1		1		[5 ; 22 ; 24 ; 13 ; 31 ; 40]
1		2		[5 ; 22 ; 13 ; 24 ; 31 ; 40]
1		3		[5 ; 22 ; 13 ; 24 ; 31 ; 40]
1		4		[5 ; 22 ; 13 ; 24 ; 31 ; 40]
2		0		[5 ; 22 ; 13 ; 24 ; 31 ; 40]
2		1		[5 ; 22 ; 13 ; 24 ; 31 ; 40]
2		2		[5 ; 13 ; 22 ; 24 ; 31 ; 40]
il n'y a plus de changements jusqu'à la fin ( j = 4 et i = 4 )

b /
Les lignes 8, 9, 10 permettet d'échanger la valeur de tab[n+1] avec tab[n]

c/

nom : algorithme A1
variables numériques : i, j, aux, n, tab(n)

DEBUT
    Saisir n
    Pour i allant de 0 à n-1
        Saisir tab(i)
    Fin Pour
    Pour j allant de 0 à n-2
        Pour i allant de 0 à n-2
            Si tab[i]>tab[i+1] alors :
                aux <- tab[i]
                tab[i] <- tab[i+1]
                tab[i+1] <- aux
            Fin Si
        Fin Pour
    Fin Pour
    Pour i allant de 0 à n-1
        Afficher tab[i]
    Fin Pour
FIN

On modifie A1 en A2. A2 prend en compte le fait qu'après chaque parcours du tableau, un élément supplémentaire est trié à la fin du tableau.
Que peut-on modifier à la ligne 6 pour en tenir compte ?


nom : algorithme A2
variables numériques : i, j, aux, n, tab(n)

DEBUT
    Saisir n
    Pour i allant de 0 à n-1
        Saisir tab(i)
    Fin Pour
    Pour j allant de 0 à n-2
        Pour i allant de 0 à n-2-j
            Si tab[i]>tab[i+1] alors :
                aux <- tab[i]
                tab[i] <- tab[i+1]
                tab[i+1] <- aux
            Fin Si
        Fin Pour
    Fin Pour
    Pour i allant de 0 à n-1
        Afficher tab[i]
    Fin Pour
FIN


2 travail sur poste informatique

a/ implementer et tester A1 et A2

"""
"""
#On saisit 5 ; 24 ; 22 ; 40 ; 13; 31

#implementation algorithme A1

n=int(input())
tab=[0]*n
for i in range(0,n):
    tab[i]=int(input())
for j in range(0,n-1):
    for i in range(0,n-1):
        if tab[i]>tab[i+1]:
            aux = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = aux
print(tab)

"""
"""
b/
#On saisit 5 ; 24 ; 22 ; 40 ; 13; 31

#implementation algorithme A2

n=int(input())
tab=[0]*n
for i in range(0,n):
    tab[i]=int(input())
for j in range(0,n-1):
    for i in range(0,n-1-j):
        if tab[i]>tab[i+1]:
            aux = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = aux       
        print("i=",i,"j=",j,"tab=",tab)



"""
"""
c/ ajouter un compteur qui compte les comparaisons

#On saisit 5 ; 24 ; 22 ; 40 ; 13; 31
#implementation algorithme A2

n=int(input())
tab=[0]*n
compteur=0
for i in range(0,n):
    tab[i]=int(input())
for j in range(0,n-1):
    for i in range(0,n-1-j):
        compteur=compteur+1
        if tab[i]>tab[i+1]:
            aux = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = aux
        print("i=",i," j=",j," iteration=",compteur," tab=",tab)
print("nb total de comparaison : ",compteur)



d/
i= 3  j= 0  iteration= 4  tab= [7, 19, 12, 18, 25]
i= 0  j= 0  iteration= 1  tab= [1, 5, 7, 8, 9]
i= 3  j= 0  iteration= 4  tab= [2, 3, 5, 6, 8]
i= 0  j= 3  iteration= 10  tab= [0, 2, 5, 7, 9]


B Limiter le nombre de comparaison
1/


nom : algorithme A3
variables numériques : i, j, aux, n, tab(n)
variable booleenne : permutation

DEBUT
    Saisir n
    permutation <- Vrai
    j=0
    Pour i allant de 0 à n-1
        Saisir tab(i)
    Fin Pour
    tant que permutation=Vrai
        permutation <- Faux
        Pour i allant de 0 à n-2-j
            Si tab[i]>tab[i+1] alors :
                aux <- tab[i]
                tab[i] <- tab[i+1]
                tab[i+1] <- aux
                permutation <- Vrai
            Fin Si
        Fin Pour
        j=j+1
    Fin tant que
    Pour i allant de 0 à n-1
        Afficher tab[i]
    Fin Pour
FIN


B2 /
a/
"""

#On saisit 5 ; 24 ; 22 ; 40 ; 13; 31
#implementation algorithme A3

n=int(input())
permutation=True
j=0
tab=[0]*n
compteur=0
for i in range(0,n):
    tab[i]=int(input())
while permutation==True:
    permutation=False
    for i in range(0,n-1-j):
        compteur=compteur+1
        if tab[i]>tab[i+1]:
            aux = tab[i]
            tab[i] = tab[i+1]
            tab[i+1] = aux
            permutation=True
        print("i=",i," j=",j," iteration=",compteur," tab=",tab)
    j=j+1
print("nb total de comparaison : ",compteur)


"""
b/
i= 1  j= 2  iteration= 9  tab= [7, 12, 18, 19, 25]
nb total de comparaison :  9

i= 3  j= 0  iteration= 4  tab= [1, 5, 7, 8, 9]
nb total de comparaison :  4

i= 2  j= 1  iteration= 7  tab= [2, 3, 5, 6, 8]
nb total de comparaison :  7

i= 0  j= 3  iteration= 10  tab= [0, 2, 6, 7, 9]
nb total de comparaison :  10

resultat 2d/
i= 3  j= 0  iteration= 4  tab= [7, 19, 12, 18, 25]
i= 0  j= 0  iteration= 1  tab= [1, 5, 7, 8, 9]
i= 3  j= 0  iteration= 4  tab= [2, 3, 5, 6, 8]
i= 0  j= 3  iteration= 10  tab= [0, 2, 5, 7, 9]

"""
"""
autre solution
    def tri_bulle(tableau):
        permutation = True
        passage = 0
        while permutation == True:
            permutation = False
            passage = passage + 1
            for en_cours in range(0, len(tableau) - passage):
                if tableau[en_cours] > tableau[en_cours + 1]:
                    permutation = True
                    # On echange les deux elements
                    tableau[en_cours], tableau[en_cours + 1] = \
                    tableau[en_cours + 1],tableau[en_cours]
        return tableau  
"""
"""

