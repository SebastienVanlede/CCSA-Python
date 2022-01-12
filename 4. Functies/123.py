# https://dodona.ugent.be/nl/courses/399/series/7773/activities/192047393
def evenOneven(getal):
    even = oneven = 0
    for cijfer in str(getal):
        if int(cijfer) % 2 != 0:
            oneven += 1
        else:
            even += 1
    return even, oneven

def volgende(getal):
    n_getal = str(evenOneven(getal)[0]) + str(evenOneven(getal)[1]) + str(len(str(getal)))
    return int(n_getal)

def stappen(getal):
    stappen = 0
    nieuw = volgende(getal)
    if getal == 123:
        stappen = -1
    while nieuw != 123:
        nieuw = volgende(nieuw)
        stappen += 1
    return stappen + 1
