PHT = float(input("Veuillez saisir le prix hors taxe de produit : "))
Cat = input("Veuillez saisir la catégorie de produit : ")
if Cat =="A": 
    print("Le prix TTC de produit est : ",PHT+PHT*0.07)
elif Cat == "B" :
    print("Le prix TTC de produit est : ",PHT+PHT*0.2)
elif Cat == "C" :
    print("Le prix TTC de produit est : ",PHT+PHT*0.25)
else:
    print("La catégorie n'existe pas ")