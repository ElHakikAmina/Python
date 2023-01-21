import random
n=random.randint(1,30)
nombreTentatives = 5
while nombreTentatives>0:
    nombreTentatives-=1
    var = int(input("Entrez un nombre : "))
    if var > n:
        print("C'est moins !")
    elif var < n:
        print("C'est plus !")
    else:
        break
if nombreTentatives != 0:
    print("bon réponse!")
else:
    print("echoué !")
