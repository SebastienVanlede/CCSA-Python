# https://dodona.ugent.be/nl/courses/399/series/3961/activities/668571979
ademhaling = str(input())
polshart = int(input())
spierspanning = str(input())
aspect= str(input()) 
reactiePrikkels = str(input())

apgar = [ademhaling, spierspanning, aspect, reactiePrikkels]
score = 0
nul = ["geen", "slap", "blauw", "bleek"]
een = ["zwak", "enige flexie", "extremiteiten", "enige beweging"]
twee = ["goed doorhuilen", "actieve beweging", "roze", "krachtig huilen"]
ongeldig = False

for i in apgar:
    if i in nul:
      score += 0
    elif i in een: 
      score += 1
    elif i in twee: 
      score += 2
    elif (i not in nul or i not in een or i not in twee): 
      ongeldig = True

if polshart == 0:
  score += 0
elif polshart < 100: 
  score += 1
elif polshart > 100: 
  score += 2
elif (polshart < 0 or type(polshart) != int()): 
  ongeldig = True

if ongeldig == False:
    if score < 4: 
      print("alarm")
    else: 
      print(score)
else: 
  print("ongeldige invoer")

