Fonction AFoisB(A, B, m, p, n)
   Pour i <- 1 à m
      Pour j <- 1 à n
         C[i,j] <- 0
         Pour k <- 1 à p
            C[i,j] <- C[i,j] + A[i,k] * B[k,j]
         Fin Pour
      Fin Pour
   Fin Pour
   Retourner C
Fin Fonction

A = Matrice de taille m X p
B = Matrice de taille p X n


**********************

Principe : Le produit matriciel s'en d duit : le produit de la matrice A (n × m) par la matrice B (m × p) est la matrice C (n × p) telle que l'élément Cij est égal au produit scalaire de la ligne i de la matrice A par la colonne j de la matrice B.

 

CORRECTION

Algorithme      ProduitMatriciel;

const N = 4 ;

var      i,j,k: entier;

           A, B, C : tableau[1..N] de entier;
Début

ecrire('Entrez les elements de votre premiere matrice ') ;
Pour i de 1 à N faire
Pour j de 1 à N faire
Lire ( A[i,j] );
Fin Pour
Fin Pour

ecrire('Entrez les elements de votre deuxieme matrice ') ;
Pour i de 1 à N faire
Pour j de 1 à N faire
Lire ( B[i,j] );
Fin Pour
Fin Pour

 Pour i de 1 a N Faire
Pour j de 1 a N Faire
C[i,j] <- 0
Pour k de 1 a n Faire
C[i,j] <- C[i,j] + A[i,k] * B[k,j]
Fpour
Fpour
Fpour

ecrire('Affichage de la matrice ') ;
Pour i de 1 à N faire
Pour j de 1 à N faire
ECRIRE( C[i,j] );
Fin Pour
Fin Pour

Fin.