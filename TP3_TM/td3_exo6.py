debut = int(input("Donnez l heure de debut de la location (un entier) : "))
fin = int(input("Donnez l heure de fin de la location (un entier) : "))

while (not(0 <= debut <= 24) and not(0 <= fin <= 24)) or (debut >= fin):
    debut = int(input("Respectez la saisie d'horarire ... : "))
    fin = int(input("Respectez la saisie d'horarire ... : "))

euro = 0

I1 = [0,17]
I2 = [17,24]

if (I1[0] <= debut <= I1[1]) and (I1[0] <= fin <= I1[1]):
    euro += (fin - debut) * 1

if (I2[0] <= debut <= I2[1]) and (I2[0] <= fin <= I2[1]):
    euro += (fin - debut) * 2

if (I1[0] <= debut <= I1[1]) and (I2[0] <= fin <= I2[1]):
    euro += ((I1[1] - debut) * 1) + ((fin - I2[0]) * 2)



