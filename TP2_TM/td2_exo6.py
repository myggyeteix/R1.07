import random

nb = random.randint(1, 100)
print(nb)
if nb < 50:
    print("Pile !")
else:
    print("Face!")