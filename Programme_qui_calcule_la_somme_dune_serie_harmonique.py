n= int (input("Veuillez saisir la valeur de n : "))
S = 0
for i in range(1,n+1):
    S = S+1/i
print("La somme harmonique de ",n,"est : ",S)