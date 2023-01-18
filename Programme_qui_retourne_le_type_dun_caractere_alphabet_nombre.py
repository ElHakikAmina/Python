caractere = input("Veuillez saisir un caractére : ")
if ("A"<= caractere and "Z">= caractere) or ("a" <= caractere and "z" >= caractere):
    print(caractere, "est un alphabet")
elif ("0" <= caractere and caractere <= "9"):
    print(caractere,"est un numero")
else:
    print(caractere,"est un caractere special")