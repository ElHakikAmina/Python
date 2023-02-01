n = int(input("Veuillez saisir un nombre : "))
s=0
for i in range (1,n):
    if n%i==0:
        s=s+i
if s==n: print("parfait")
else: print("non parfait")