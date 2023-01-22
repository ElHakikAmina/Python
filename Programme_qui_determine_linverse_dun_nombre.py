n = int(input("Donner n : "))
Inverse =0
while N!=0:
    Inverse = (Inverse * 10)+(N % 10)
    N =N//10
print("L'inverse de N est : ",Inverse)