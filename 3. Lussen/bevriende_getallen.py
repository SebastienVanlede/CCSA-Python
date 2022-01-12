# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1258720912
getal1 = int(input())
getal2 = int(input())
som1 = som2 = 0

for i in range(1, getal1, 1):
    if getal1 % i == 0:
        som1 += i

for j in range(1, getal2, 1):
    if getal2 % j == 0:
        som2 += j

if som1 == getal2 and som2 == getal1:
    print(f'{getal1} en {getal2} zijn bevriende getallen')
else:
    print(f'{getal1} en {getal2} zijn geen bevriende getallen')
