# https://dodona.ugent.be/nl/courses/399/series/7773/activities/581452346
def bovensteboven(getal):
    resultaat = [int(x) for x in str(getal)]
    totaal = 0
    if len(resultaat) % 2 == 0:
        for i in range(len(resultaat) // 2):
            if ((resultaat[i] == 9 and resultaat[(i + 1) * -1] == 6) or (resultaat[i] == 6 and resultaat[(i + 1) * -1] == 9) or
                    (resultaat[i] == 8 and resultaat[(i + 1) * -1] == 8) or (
                            resultaat[i] == 1 and resultaat[(i + 1) * -1] == 1) or (
                            resultaat[i] == 0 and resultaat[(i + 1) * -1] == 0)):
                totaal += 2
    elif len(resultaat) % 2 != 0:
        for i in range(len(resultaat) // 2):
            if ((resultaat[i] == 9 and resultaat[(i + 1) * -1] == 6) or (resultaat[i] == 6 and resultaat[(i + 1) * -1] == 9) or
                    (resultaat[i] == 8 and resultaat[(i + 1) * -1] == 8) or (
                            resultaat[i] == 1 and resultaat[(i + 1) * -1] == 1) or (
                            resultaat[i] == 0 and resultaat[(i + 1) * -1] == 0)):
                totaal += 2
        if resultaat[i + 1] == 8 or resultaat[i + 1] == 1 or resultaat[i + 1] == 0:
            totaal += 1

    if totaal == len(resultaat):
        return True
    else:
        return False


def volgende(getal):
    getal += 1
    waarde = bovensteboven(getal)
    while not waarde:
        getal += 1
        waarde = bovensteboven(getal)
    return getal
