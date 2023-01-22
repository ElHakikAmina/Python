a = int(input("donner a : "))
b = int(input("donner b : "))
if(a>b):
    min=b
else:
    min=a
for i in range (1,min+1):
    if a%i==0 and b%i==0:
        pgcd=i
print("le pgcd est : ",pgcd)