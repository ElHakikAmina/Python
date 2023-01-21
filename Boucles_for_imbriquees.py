n = int(input("Veuillez entrer le nombre d'equipes : "))
for i in range (1,n+1):
    for j in range (1,n+1):
        if i != j:
            print("Equipe",i,"vs equipe",j)