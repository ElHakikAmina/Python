while True:
    print(" ---- Calculatrice : MENU----")
    print("1- Addition.")
    print("2-Soustraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Reste d'une division entiere.")
    print("6-Puissance")
    opertaion = int(input("Quel calcul veux-tu effectuer ? "))
    A=int(input("Saisir le premier terme : "))
    B=int(input("Saisir le deuxiéme terme : "))
    if opertaion == 1 :
        print("Le résultat : ",A+B)
    elif opertaion ==2:
        print("Le resultat est :",A-B)
    elif opertaion ==3:
        print("Le resultat est :",A*B)
    elif opertaion ==4:
        if B !=0:
            print("Le resultat est :",A/B)
        else:
            print("La division sur 0 est impossible")
    elif opertaion ==5:
        if B!=0:
            print("Le resultat est :",A%B)
        else:
            print("La division sur 0 est impossible")
    elif opertaion ==6:
        print("Le resultat est :",A**B)
    else:
        print("Operateur est incorrect")
    reponse =input("Veux-tu faire un autre calcul (O/N) : ") 
    if reponse == "N":
        break 
    

