date = str(input("Quelle est votre date ? "))
while len(date) != 8:
    date = str(input("Resaisissez votre date : "))

x = "Correct"
annee = date[4:]
mois = date[2:4]
jour = date[0:2]

#if ((int(annee) % 4 == 0) and (int(annee) % 100 != 0)) or (int(annee) % 400 == 0):




