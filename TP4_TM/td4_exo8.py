dico = {}
dico2 = {}
binome = {}

dico ['name'] = "TEIXEIRA"
dico ['firstname'] = "Miguel"
dico ['promo'] = "RT1"
dico ['group'] = "RT122"

dico2 ['name'] = "SIESS"
dico2 ['firstname'] = "Théo"
dico2 ['promo'] = "RT1"
dico2 ['group'] = "RT122"

binome ['ID1'] = dico
binome ['ID2'] = dico2

print(f"Votre nom est {dico['name']}, votre prenom est {dico['firstname']}, votre promo est {dico ['promo']} et votre groupe est {dico['group']}.")

print("Les cles du dico sont :")
for i in dico.keys():
    print(f"- {i}")

print("\nLes valeurs du dico sont :")
for i in dico.values():
    print(f"- {i}")

print("\nLes tuplets du dico sont :")
for i in dico.items():
    print(f"- {i}")

print (binome['ID1']['name'])
print("Les étudiants formants le binôme sont :")
print(f"- L'etudiant : ", end=" ")
for val in binome['ID1'].values():
    print(f"{val}", end=" ")
print()
print(f"- L'etudiant : ", end=" ")
for val in binome['ID2'].values():
    print(f"{val}", end=" ")