nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
notes = []

for i in range(nombreEtudiants):
    notes.append(float(input(f"Note de l'étudiant {i} : ")))

moyenne = sum(notes) / nombreEtudiants
print(moyenne)

for i in range(nombreEtudiants):
    print("Ecart à la moyenne de l'étudiant ",i,":",(notes[i]-moyenne))
