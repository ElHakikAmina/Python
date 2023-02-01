import random
nom = input("Veuillez saisir votre nom : ")
user_victories=0
pc_victories=0
nuls=0
while True :
    coupJoueur = input("Entrez votre coup: (p)ierre, (f)euille, (c)iseaux ou (q)uitter : ")
    if coupJoueur == "q":
        print("Vous avez quitté le jeu")
        break
    if coupJoueur!="p" and coupJoueur !="f" and coupJoueur!="c":
        continue

    if coupJoueur == "p":
        print("PIERRE contre ...",end=" ")
    elif coupJoueur == "f":
        print("FEUILLE contre ...",end=" ")
    else:
        print("CISEAUX contre ...",end=" ")

    randomNombre = random.randint(1,3)
    if randomNombre == 1:
        coupPC = "p"
        print("PIERRE")
    elif randomNombre == 2:
        coupPC ="f"
        print("FEUILLE")
    else:
        coupPC = "c"
        print("CISEAUX")
    
    if coupJoueur == coupPC:
        print("Partie est nulle!")
        nuls = nuls+1
    elif coupJoueur =="p" and coupPC == "c":
        print("Vous avez gagné ! ")
        user_victories = user_victories+1
    elif coupJoueur == "f" and coupPC=="p":
        print("Vous avez gagné ! ")
        user_victories = user_victories+1
    elif coupJoueur == "c" and coupPC=="f":
        print("Vous avez gagné ! ")
        user_victories = user_victories+1
    elif coupJoueur == "p" and coupPC=="f":
        print("Vous avez perdu ! ")
        user_victories = user_victories+1
    elif coupJoueur == "f" and coupPC=="c":
        print("Vous avez perdu ! ")
        user_victories = user_victories+1
    elif coupJoueur == "c" and coupPC=="p":
        print("Vous avez perdu ! ")
        user_victories = user_victories+1
    