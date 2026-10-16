#a
n = int(input("Entrez un nombre : "))
rslt = 0
for i in range(0,n+1):
    rslt += i
    i+=1

print(rslt)

#b
x = int(input("Entrez un nombre : "))
while x!= 100:
    x = int(input("Incorrect, entrez un nouveau nombre : "))
print("Vous avez atteint 100 !!!")

#c
l = []
for i in range(10):
    x = int(input("Entrez un nombre compris entre 0 et 20: "))
    while not(0 <= x <= 20):
        x = int(input("Incorrect, entrez un nombre compris entre 0 et 20 : "))
    l.append(x)

print(l)

a = 0 #Le nombre de valeurs inférieur strictement à 10
b = 0 #Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15
c = 0 #Le nombre de valeurs supérieur ou égale à 15

for i in l:
    if i < 10:
        a +=1
    if (10 <= i < 15):
        b +=1
    if i >= 15:
        c +=1
print("Le nombre de valeurs inferieur strictement a 10 : ",a)
print("Le nombre de valeurs superieur ou egale a 10 et inferieur strictement a 15 : ",b)
print("Le nombre de valeurs superieur ou egale a 15 : ",c)

#d
x = int(input("Entrez un nombre : "))
rslt = 0
i = 0
while rslt < x:
    i += 1
    rslt += i
print("Le nombre recherche est : ",i)

