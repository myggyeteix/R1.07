tab = [1, "Eh !", 3, "Oh !"]
print(type(tab)) # affiche le type de la variable tab
for val in tab :
    print (val) # affiche toutes les valeurs de tab une par une dans l'ordre
tab[3] = "Ah! "
for i in range(len(tab)) :
    print(tab[i]) # affiche toutes les valeurs de tab comme avant, en prenant en compte le changement de la 4e valeur
i=0
while i < len(tab) : # affiche encore toutes les valeurs en utilisant un autre systeme avec while
    print(tab[i])
    i+=1

# en résumé il s'agit de plusieurs façon d'afficher les valeurs dans une liste...