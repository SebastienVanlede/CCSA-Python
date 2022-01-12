# https://dodona.ugent.be/nl/courses/399/series/3962/activities/654951832/
piraten = int(input())
kokosnoten = int(input())
teller = 1

while teller <= piraten:
    aapKokosnoten = kokosnoten % piraten
    piraatKokosnoten = int(kokosnoten / piraten)

    aapTekst = f'{aapKokosnoten} noten'
    if aapKokosnoten == 1:
        aapTekst = '1 noot'
    elif aapKokosnoten == 0:
        aapTekst = 'geen noten'

    print(f'{kokosnoten} noten = {piraatKokosnoten} noten voor piraat#{teller} en {aapTekst} voor de aap')
    kokosnoten -= piraatKokosnoten + aapKokosnoten
    teller += 1

aapKokosnoten = kokosnoten % piraten
piraatKokosnoten = int(kokosnoten / piraten)
tekst = str()

if kokosnoten != 1:
    if aapKokosnoten == 1:
        print(f'elke piraat krijgt {piraatKokosnoten} noten en 1 noot voor de aap')
    elif aapKokosnoten == 0:
        print(f'elke piraat krijgt {piraatKokosnoten} noten en geen noten voor de aap')
    else:
        print(f'elke piraat krijgt {piraatKokosnoten} noten en {aapKokosnoten} noten voor de aap')
else:
    if aapKokosnoten == 1:
        print('elke piraat krijgt 1 noot en 1 noot voor de aap')
    elif aapKokosnoten == 0:
        print('elke piraat krijgt 1 noot en geen noten voor de aap')
    else:
        print(f'elke piraat krijgt 1 noot en {aapKokosnoten} noten voor de aap')
