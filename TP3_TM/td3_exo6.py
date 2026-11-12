debut = int(input("Donnez l heure de debut de la location (un entier) : "))
fin = int(input("Donnez l heure de fin de la location (un entier) : "))

while (not(0 <= debut <= 24) and not(0 <= fin <= 24)) or (debut >= fin):
    debut = int(input("Respectez la saisie d'horarire ... : "))
    fin = int(input("Respectez la saisie d'horarire ... : "))

euro = 0
tarifun = 0
tarifdeux = 0

I1 = [0,7]
I2 = [17,24]

if (I1[0] <= debut <= I1[1]) and (I1[0] <= fin <= I1[1]):
    euro += (fin - debut) * 1
    tarifun += (fin - debut)

if (I2[0] <= debut <= I2[1]) and (I2[0] <= fin <= I2[1]):
    euro += (fin - debut) * 1
    tarifun += (fin - debut)

if (I1[1] <= debut <= I2[0]) and (I1[1] <= fin <= I2[0]):
    euro += (fin - debut) * 2
    tarifdeux += (fin - debut)

if (I1[0] <= debut < I1[1]) and (I1[1] < fin < I2[0]):
    euro += ((I1[1] - debut) * 1) + ((fin - I1[1]) * 2)
    tarifun += (I1[1] - debut)
    tarifdeux += (fin - I1[1])

if (I1[1] <= debut < I2[0]) and (I2[0] < fin < I2[1]):
    euro += ((I2[0] - debut) * 2) + ((fin - I2[0]) * 1)
    tarifun += (I2[0] - debut)
    tarifdeux += (fin - I2[0])

print(euro)
print(tarifun)
print(tarifdeux)


