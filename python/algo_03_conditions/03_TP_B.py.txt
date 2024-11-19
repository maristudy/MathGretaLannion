#conditions - TP - A3

juin = input("Place en juin ( O/N) ? ")
etudiant = input("Etes-vous étudiant ( O/N) ? ")

if (etudiant=="O" or etudiant=="o") :
    if ( juin=="O" or juin=="o"):
        prix = 16*0.75
    else :
        prix = 20*0.75
else :
    n = int(input("Nombre de place : "))
    if ( juin=="O" or juin=="o"):
        prix = 16*n
    else :
        if n >= 3:
            prix = n * ( 20*0.9)
        else :
            prix = n*20
print(prix)
