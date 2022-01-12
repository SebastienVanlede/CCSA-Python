#https://dodona.ugent.be/nl/courses/399/series/3962/activities/113082360/
prijs = float(input())
veelvoud = int(prijs * 100)
end = False
for i in range(0, veelvoud):
  for j in range(veelvoud, i - 1, -1):
    cadeau1 = i / 100
    cadeau2 = j / 100
    if cadeau1 * cadeau2 - 1 == 0:
      continue
    cadeau3 = (cadeau1 + cadeau2) / (cadeau1 * cadeau2 - 1)
    if round(cadeau1 + cadeau2 + cadeau3, 6) == prijs:
      if round(cadeau1 + cadeau2 + cadeau3) == round(cadeau1 * cadeau2 * cadeau3):
        if cadeau2 < cadeau3:
          a = cadeau1
          b = cadeau2
          c = cadeau3
        else:
          a = cadeau1
          b = cadeau3
          c = cadeau2
        if cadeau1 > b:
          a = cadeau2
          b = cadeau1
        print(f'€{a:.2f} + €{b:.2f} + €{c:.2f} = €{a:.2f} x €{b:.2f} x €{c:.2f} = €{prijs:.2f}')
        end = True
        break
    if end:
        break
