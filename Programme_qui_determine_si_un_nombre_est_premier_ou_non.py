n =int(input("Veuillez entrer un nombre : "))
f=0
for i in(2,int(n/2)):
    if n%i==0:
        f=1
if f==0:
    print("premier")
else:
    print("n'est pas premier")