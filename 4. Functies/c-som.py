# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1706631167
def csom(getal):
    if len(str(getal)) > 1:
        som = 0
        for cijfer in str(getal):
            som += int(cijfer)
        return csom(som)
    else:
        return getal
