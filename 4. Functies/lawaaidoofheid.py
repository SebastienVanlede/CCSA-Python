# https://dodona.ugent.be/nl/courses/399/series/7773/activities/1563511392
def maximale_blootstelling(geluidsniveauDB):
    seconden = 8 * 3600
    decibel = 83
    while decibel <= geluidsniveauDB:
        seconden /= 2
        decibel += 3

    if geluidsniveauDB >= 80:
        return float(seconden)
    else:
        return -1.0
