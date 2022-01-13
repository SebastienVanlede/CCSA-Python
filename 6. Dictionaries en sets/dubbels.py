# https://dodona.ugent.be/nl/courses/399/series/7814/activities/531231333
import collections

def dubbel(getallen):
    getal_list = [getal for getal, count in collections.Counter(getallen).items() if count > 1]
    if len(getal_list) != 0:
        return getal_list[0]

def dubbels(getallen):
    getallen_list = set([getal for getal in getallen if getallen.count(getal) > 1])
    getallen_list_zonder = {getal for getal in getallen if getal not in getallen_list}
    return getallen_list_zonder, getallen_list

