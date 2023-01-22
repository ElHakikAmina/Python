N = int (input("Veuillez saisir la valeur de N : "))
n=N
Inverse =0
while N!=0:
    Inverse=(Inverse*10)+(N % 10)
    N =N//10
print("L'inverse de N est : ",Inverse)
if n == Inverse :
    print("Palindrome")
else:
    print("n'est pas pamindrome")