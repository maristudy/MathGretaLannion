n=ni		u=4			S=4
n=1			u=4+2=6		S=4+6=10
n=2			u=6+2=8		S=10+8=18
n=3			u=8+2=10	S=18+10=28

role : somme des n+1 premiers termes

nom:somme suite geometrique
variables numeriques : n, u, S, i

DEBUT
    Saisir n
    u <- 4
    S <- u
    pour i allant de 1 à n-1
        u <- u*3
        S <- S+u
    Fin pour
    Afficher S
FIN