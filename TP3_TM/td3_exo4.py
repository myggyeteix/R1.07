import random

x = random.randint(0,100)
print(x)
cpt = 1

n = int(input("Devinez le nombre magique : "))
while n != x:
    cpt += 1
    if n < x:
        print("Faux ! Indice : Plus grand !")
    if n > x:
        print("Faux ! Indice : Plus petit !")
    n = int(input("Essayez encore : "))

print("Bravo, c'etait :",x,", vous l'avez deviner en",cpt,"fois !!")
