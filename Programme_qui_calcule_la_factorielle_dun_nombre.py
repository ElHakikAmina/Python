n = int(input("Veuillez saisir la valeur de n : "))
while True:
    n=int(input("Veuillez saisir la valeur de n : "))
    if n>=0:
        break
if n == 0:
    print("La factorielle de 0 est 1")
else:
    F = 1
    for i in range(2,n+1):
        F=F*i
    print("La factorielle de ",n,"est ",F)