import time

n = int(input("Entrez un nombre positif : "))
while n < 0:
    n = int(input("Incorrect, entrez un nombre positif : "))

for i in range(n, 0, -1):
    print(i, flush=True)
    time.sleep(1)
    i -= 1

print("BOUMMMM!!!")

n = int(input("Entrez un nombre positif : "))
while n < 0:
    n = int(input("Incorrect, entrez un nombre positif : "))

i = n
while i != 0:
    print(i, flush=True)
    time.sleep(1)
    i -= 1

print("BOUMMMM!!!")

