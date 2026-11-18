date = str(input("Quelle est votre date ? "))
while len(date) != 8:
    date = str(input("Resaisissez votre date : "))

x = "Correct"
annee = date[4:]
mois = date[2:4]
jour = date[0:2]

lm_30 = [4,6,9,11]
lm_31 = [1,3,5,7,8,10,12]

if ((int(annee) % 4 == 0) and (int(annee) % 100 != 0)) or (int(annee) % 400 == 0) :
    bis = 1
else :
    bis = 0

if int(mois) in lm_30 :
    if (int(jour) > 30) or (int(jour) < 1) :
        x = "Incorrect"

if int(mois) in lm_31 :
    if (int(jour) > 31) or (int(jour) < 1) :
        x = "Incorrect"

if (int(mois) > 12) or (int(mois) < 1) :
    x = "Incorrect"

if int(annee) < 1 :
    x = "Incorrect"

if (bis == 1) and (int(mois)) == 2 :
    if int(jour) > 29 :
        x = "Incorrect"
if (bis == 0) and (int(mois)) == 2 :
    if int(jour) > 28 :
        x = "Incorrect"

print(x)






