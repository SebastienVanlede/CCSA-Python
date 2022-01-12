# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1131866318
def waardering(prijs, wisselkoers):
    wissel = prijs / 4.07
    prijs = (wissel - wisselkoers) / wisselkoers * 100

    if prijs > 25:
        return 'sterk overgewaardeerd'
    elif prijs > 5:
        return 'overgewaardeerd'
    elif prijs > -5:
        return 'ongeveer gelijk'
    elif prijs > -25:
        return 'ondergewaardeerd'
    else:
        return 'sterk ondergewaardeerd'


def wisselkoersanalyse(prijs, wisselkoers):
    e = ' '
    s = str(prijs).split()
    koers = float(s[0])
    valuta = e.join(s[1:])

    return f'De {valuta} is {waardering(koers, wisselkoers)} ten opzichte van de dollar.'
