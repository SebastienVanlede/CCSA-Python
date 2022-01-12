# https://dodona.ugent.be/nl/courses/399/series/3962/activities/2134730675
getal = int(input())
i = 3
output = 1

while getal % 2 == 0:
    getal /= 2

while i * i <= getal:
    teller = 0
    while getal % i == 0:
        getal /= i
        teller += 1
    output *= teller + 1
    i += 2
if getal > 2:
    output *= 2

print(output - 1)
