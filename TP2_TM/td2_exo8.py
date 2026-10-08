print("Pour rappel, I =  [2,3[ U ]0,1] U [-10,-2] !!")
x = int(input("Entrez une valeur : "))

if (2 <= x < 3) or (0 < x <= 1) or (-10 <= x <= -2):
    print("x appartient bien a I !!")
else:
    print("x n'appartient malheuresement pas a I")

