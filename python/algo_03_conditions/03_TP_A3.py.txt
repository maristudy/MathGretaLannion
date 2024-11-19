#conditions - TP - A3

etudiant = input("Etes-vous étudiant ( O/N) ? ")

if (etudiant=="O" or etudiant=="o") :
        prix = 20*0.75
else :
    n = int(input("Nombre de place : "))
    prix = 20*n
    if n >= 3 :
        prix = prix*0.9
print(prix)
