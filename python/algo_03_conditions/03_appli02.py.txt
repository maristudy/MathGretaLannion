#conditions - application 2 : le plus grand nombre

nb1 = int(input("Donner un nombre : "))
nb2 = int(input("Donner un nombre : "))
nb3 = int(input("Donner un nombre : "))

if nb1>nb2 and nb1>nb3 :
    print(nb1," est le nombre le plus grand")
elif nb2>nb1 and nb2>nb3 :
    print(nb2," est le nombre le plus grand")
else :
    print(nb3," est le nombre le plus grand")
