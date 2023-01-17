sexe = input("Veuillez entrer le sexe de l'habitant : ")
age = int (input("Veuillez entrer l'age de l'habitant : "))
if((sexe =='H' and age>= 20) or (sexe=="F" and age >=18 and age <=35)):
    print("L'habitant est imposable")
else :
    print("L'habitant n'est pas imposable")