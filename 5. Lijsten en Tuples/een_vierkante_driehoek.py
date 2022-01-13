# https://dodona.ugent.be/nl/courses/399/series/7098/activities/818147392
import math

def driehoek(getal):
    if not isinstance(getal, int) or getal < 0:
        raise AssertionError('ongeldig aantal rijen')
    rij = []
    for i in range(getal):
        rij2 = []
        for j in range(len(rij) + 1):
            if len(rij2) == 0 or len(rij2) == len(rij):
                rij2.append(1)
            else:
                rij2.append(rij[i - 1][j - 1] + rij[i - 1][j])
        rij.append(rij2)
    return rij


def zeshoek(rij, kolom):
    if rij <= 1 or kolom <= 1 or rij <= kolom:
        raise AssertionError('ongeldige interne positie')
    try:
        hoek = driehoek(rij + 1)
        getal = [hoek[rij - 2][kolom - 2], hoek[rij - 2][kolom - 1], hoek[rij - 1][kolom], hoek[rij][kolom],
                 hoek[rij][kolom - 1], hoek[rij - 1][kolom - 2]]
    except AssertionError as ae:
        raise AssertionError('ongeldige interne positie')
    return getal


def kwadraat(rij, kolom):
    if rij <= 1 or kolom <= 1 or rij <= kolom:
        raise AssertionError('ongeldige interne positie')
    try:
        output = ''
        x = 1
        valid = zeshoek(rij, kolom)
        for i in range(len(valid)):
            x *= valid[i]
            if i == len(valid) - 1:
                output = output + str(valid[i])
            else:
                output = output + str(valid[i]) + ' x '
        kwadraat = math.sqrt(x)
        output = output + ' = ' + str(x) + ' = ' + \
                 str(int(kwadraat)) + ' x ' + str(int(kwadraat))
    except AssertionError as ae:
        raise AssertionError('ongeldig aantal rijen')
    return output
