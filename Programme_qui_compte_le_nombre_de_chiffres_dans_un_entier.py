N= int(input("Veullez saisir la valeur de N : "))
nbr=0
while N!=0:
    N=N//10
    nbr+=1
print("Nombre total de chiffre dans le nombre ",N," est : ",nbr)