# https://dodona.ugent.be/nl/courses/399/series/7814/activities/1564830716
def ontleding(akkoord):
    akkoord_list = list(akkoord)
    grondnoot = akkoord_list[0]
    voorstelling = ''
    if len(akkoord_list) == 5:
        grondnoot += akkoord_list[1]
        voorstelling += akkoord_list[2] + akkoord_list[3] + akkoord_list[4]
    elif len(akkoord_list) == 4:
        if akkoord_list[1] == '#':
            grondnoot += akkoord_list[1]
            if len(akkoord_list) == 4:
                voorstelling += akkoord_list[2] + akkoord_list[3]
            elif len(akkoord_list) == 3:
                voorstelling += akkoord_list[2]
        else:
            voorstelling = akkoord_list[1] + akkoord_list[2] + akkoord_list[3]
    elif len(akkoord_list) == 3:
        if akkoord_list[1] == '#':
            grondnoot += akkoord_list[1]
            if len(akkoord_list):
                voorstelling += akkoord_list[2]
        else:
            voorstelling = akkoord_list[1] + akkoord_list[2]
    elif len(akkoord_list) == 2:
        if akkoord_list[1] == '#':
            grondnoot += akkoord_list[1]
        else:
            voorstelling = akkoord_list[1]
    else:
        voorstelling = ''
    akkoord_type = (grondnoot, voorstelling)
    return akkoord_type

def noten(grondnoot, toon_intervallen):
    toonladder = ['C', 'C#', 'D','D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    noten_lijst = []

    grondnoot = toonladder.index(grondnoot)
    for i in toon_intervallen:
        tussenstuk = i + grondnoot
        noten_lijst.append(toonladder[tussenstuk % len(toonladder)])
    return noten_lijst

def akkoord(notatie, types, voorstelling):
  xyz = ontleding(notatie)
  a = xyz[1]
  b = voorstelling[a]
  noten_list = types[b]
  first_tupple = xyz[0]
  return tuple(noten(first_tupple, noten_list))
