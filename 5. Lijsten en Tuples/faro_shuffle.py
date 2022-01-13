# https://dodona.ugent.be/nl/courses/399/series/7098/activities/623087135
import math
def nieuw_kaartspel(kleuren, waarden):
    kaarten_lijst = []
    for kleur in kleuren:
        for waarde in waarden:
            kaarten_lijst.append(kleur + waarde)
    return kaarten_lijst

def splits_kaartspel(kaarten):
    deel1 = kaarten[:len(kaarten)//2]
    deel2 = kaarten[len(kaarten)//2:]
    return tuple([deel1, deel2])

def faro_shuffle(deel1, deel2):
    if len(deel1) == len(deel2):
        return [a for b in zip(deel1, deel2) for a in b]
    else:
        return [a for b in zip(deel1, deel2) for a in b] + [deel2[-1]]