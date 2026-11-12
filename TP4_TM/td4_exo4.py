L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]
occurence = []
for i in range(len(L1)):
    occurence.append(0)

for j in range(len(L1)):
    for i in L1:
        if i == L1[j]:
            occurence[j] += 1

chiffre_max = []
for i in range(len(L1)):
    if occurence[i] == max(occurence):
        chiffre_max.append(L1[i])

print("La ou les valeur(s) qui sont le plus apparus dans la liste sont : ",set(chiffre_max))
print("Ils sont apparus ",max(occurence),"fois")

#méthode avec count()
occurence2 = []
for i in range(len(L1)):
    occurence2.append(L1.count(L1[i]))

chiffre_max2 = []
for i in range(len(L1)):
    if occurence2[i] == max(occurence2):
        chiffre_max2.append(L1[i])

print("La ou les valeur(s) qui sont le plus apparus dans la liste sont : ",set(chiffre_max2))
print("Ils sont apparus ",max(occurence2),"fois")