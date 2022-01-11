# https://dodona.ugent.be/nl/courses/399/series/3960/activities/567405275
kilometertellerBegin = float(input())
kilometertellerEinde = float(input())
benzine = float(input())

geredenKilometers = kilometertellerEinde - kilometertellerBegin
benzineverbruik = (benzine * 100) / geredenKilometers

print(benzineverbruik)
