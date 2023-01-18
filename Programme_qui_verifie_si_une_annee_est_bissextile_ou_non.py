annee = int (input("Veuillez saisir une annee"))
if ( ((annee % 4 ==0) and (annee % 100 !=0)) or (annee % 400 == 0) ) :
    print(annee," est une année bissextile")
else :
    print(annee," n'est une année bissextile")