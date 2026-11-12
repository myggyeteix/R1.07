nMax = int(input("Donnez la taille maximale des vecteurs : "))

v1 = []
v2 = []

n = int(input("Donnez la taille effective des vecteurs : "))
while (1 > n) or (n > nMax):
    n = int(input("Respectez la taille effective des vecteurs : "))

print("Saisie du premier vecteur :")
for i in range(n):
    v1.append(int(input(f"v1[{i}] = ")))

print("Saisie du deuxième vecteur :")
for i in range(n):
    v2.append(int(input(f"v2[{i}] = ")))

ps = 0
for i in range(n):
    ps += v1[i] * v2[i]

print("Le produit scalaire de v1 par v2 vaut",float(ps))