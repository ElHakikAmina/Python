age = int(input("Veuillez donner l'age d'amal : "))
s =0
for i in range(1,age+1):
    s=s+(500+(i*3))
print("Le compte d'Amal au ",age,"iéme anniversaire est :",s)