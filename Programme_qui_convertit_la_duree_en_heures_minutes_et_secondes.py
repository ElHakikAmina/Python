T = int(input("Veuillez saisir la durée en seconde : "))
H = T//3600
R = T % 3600
M = R // 60
S = R % 60
print(H,"H: ",M,"m: ",S,"s")