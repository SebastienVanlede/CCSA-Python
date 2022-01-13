# https://dodona.ugent.be/nl/courses/399/series/7098/activities/1333299580
def beweeg(coordinates, richting):
    if richting == '^':
        return coordinates[0], coordinates[1] + 1
    if richting == 'v':
        return coordinates[0], coordinates[1] - 1
    if richting == '>':
        return coordinates[0] + 1, coordinates[1]
    if richting == '<':
        return coordinates[0] - 1, coordinates[1]

def teruggekeerd(richting):
    if richting[1] == '>' and richting[0] == '<' or richting[0] == '>' and richting[1] == '<':
        return True
    if richting[1] == 'v' and richting[0] == '^' or richting[0] == 'v' and richting[1] == '^':
        return True
    return False

def laatste_levende_positie(richting):
    coordinates = [0, 0]
    valid = 0
    vorige = None

    for i in richting:
        if vorige is None:
            coordinates = beweeg(coordinates, i)
            vorige = i
            valid += 1
        else:
            if teruggekeerd([vorige, i]):
                return valid, coordinates[0], coordinates[1]
            coordinates = beweeg(coordinates, i)
            vorige = i
            valid += 1
    return valid, coordinates[0], coordinates[1]