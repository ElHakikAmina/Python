R1 = float(input("Veuillez saisir la valeur de R1 : "))
R2 = float(input("Veuillez saisir la valeur de R1 : "))
R3 = float(input("Veuillez saisir la valeur de R1 : "))
Rser = R1+R2+R3
Rpar = (R1*R2*R3)/(R1*R2 + R2*R3 + R1*R3)
print("La valeur de résistance en série est : ",format(Rser,".2f"))
print("La valeur de résistance en paralelle est : ",format(Rpar,".2f"))
