# https://dodona.ugent.be/nl/courses/399/series/7098/activities/117689921
def alfabetisch(zin):
    woorden = [woord.lower() for woord in zin.split(' ')]
    woorden.sort()
    return (' '.join([str(i) for i in woorden]))
