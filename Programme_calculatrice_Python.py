A = float(input("Veuillez saisir la valeur  de A : "))
op = input("Veuillez saisir l'operateur : ")
B = float(input("Veuillez saisir la valeur  de B : "))
if op == "+":
    op=print("A + B =",A+B)
elif op == "-" :
    op=print("A - B =",A-B)
elif op == "*" :
    op=print("A * B =",A*B)
elif op == "/" :
    op=print("A / B =",A/B)
else:
    print("Vous devez entrer un operateur + - / *")