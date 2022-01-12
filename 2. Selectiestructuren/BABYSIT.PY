# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1797346540
aankomstUur = int(input())
aankomstMinuut = int(input()) 
vertrekUur = int(input()) 
vertrekMinuut = int(input())

aankomstDecimal = aankomstUur + aankomstMinuut/60.0
vertrekDecimal = vertrekUur + vertrekMinuut/60.0
p1 = 18.0
p2 = 21.5

if aankomstDecimal < p1 or vertrekDecimal < aankomstDecimal:
  print("ongeldige invoer")
else:
    if vertrekDecimal < p2:
        tijd1 = vertrekDecimal - aankomstDecimal
        tijd2 = 0
    elif aankomstDecimal < p2:
        tijd1 = p2 - aankomstDecimal
        tijd2 = vertrekDecimal - p2
    else:
        tijd1 = 0
        tijd2 = vertrekDecimal - aankomstDecimal
    totaalVerdiend = 2 * tijd1 + 4 * tijd2
    print(totaalVerdiend)
