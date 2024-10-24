"""
kmjour=30
for i in range(9):
    kmjour=kmjour+10
print(kmjour)

1 : 30
2 : 40
3 : 50
4 : 60
5 : 70
6 : 80
7 : 90
8 : 100
9 : 110
10: 120
"""
kmjour=30
kmtotal=kmjour
for i in range(20):
    kmjour=kmjour+10
    kmtotal=kmtotal+kmjour
print(kmtotal)

"""
kmjour=30
kmtotal=kmjour
for i in range(20): #de 0 à 19
    kmjour=kmjour+10
    kmtotal=kmtotal+kmjour
    if((i+2)%7)==0:
        print ("semaine ",((i+2)//7),", ",kmtotal," km parcourus")
        kmtotal=0
"""