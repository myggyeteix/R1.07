x = int(input("Factorielle de ? :"))
a = input("Vous voulez calculer cette factorielle avec une boucle While ou For ? : ")

rslt = 1

if (a == "While"):
    i = 1
    while i != (x+1):
        rslt *= i
        i += 1

if (a == "For"):
    for i in range(1,x+1):
        rslt *= i
        i += 1

print(rslt)