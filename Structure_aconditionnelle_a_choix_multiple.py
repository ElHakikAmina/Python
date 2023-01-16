age = int (input("Veuillez entrer  l'age de l'enfant : "))
if age >= 6 and age <= 7 :
    print("La catégorie de l'element est POUSSIN")
elif age >= 8 and age <=9 :
    print("La catégorie de l'element est PUPILLE")
elif age>=10 and age <= 11 :
    print("La catégorie de l'element est MINIME")
elif age >= 12 and age <= 16 :
    print("La catégorie de l'element est CADET")
else:
    print("La catégorie n'existe pas")

    