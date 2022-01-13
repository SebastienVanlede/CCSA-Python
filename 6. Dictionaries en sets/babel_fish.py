# https://dodona.ugent.be/nl/courses/399/series/7814/activities/431253538
def vertalingToevoegen(woord, vertaling, dictionary):
    dictionary[woord] = vertaling

def vertaling(woord, woordenboek):
    return woordenboek.get(woord, '???')
