dico = {}
dico2 = {}

dico ['name'] = "TEIXEIRA"
dico ['firstname'] = "Miguel"
dico ['promo'] = "RT1"
dico ['group'] = "RT122"
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