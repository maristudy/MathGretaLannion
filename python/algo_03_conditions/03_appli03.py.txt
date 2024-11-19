#conditions - application 3 : assurance auto

age = int(input("Donner votre age : "))
anneePermis = int(input("Donner l'année d'obtention du permis : "))

if age<25 and 2024-anneePermis<2 :
    print("Vous êtes tarif rouge")
elif age<25 and 2024-anneePermis>2 :
    print("Vous êtes tarif orange")
elif age>=25 and 2024-anneePermis>2 :
    print("Vous êtes tarif vert")    
else :
    print("Vous n'avez pas de tarif")
