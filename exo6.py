tps = int(input("Nombres de minutes passées depuis le début du mois ? : "))
heure = tps // 60
minute_restantes = tps % 60
jour = heure // 24
heure_restantes = heure % 24
print(jour)
print(heure_restantes)
print(minute_restantes)


