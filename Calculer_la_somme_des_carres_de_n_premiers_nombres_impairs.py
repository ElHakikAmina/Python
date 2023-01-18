n = int(input("donner n : "))
s=0
j=1
for i in range(n):
    s=s+(j**2)
    j = j+2
print("La somme des nombres impaires est : ",s)