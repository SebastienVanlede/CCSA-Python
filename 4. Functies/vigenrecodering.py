# https://dodona.ugent.be/nl/courses/399/series/7773/activities/862295437/
import re
from string import ascii_lowercase

def codeer(tekst, sleutel):
    teller_tekst = 0
    teller_sleutel = 0
    geencrypteerd_bericht = []
    sleutel = str(sleutel)
    tekst = str(tekst)
    hoofdletters = " ".join(re.findall("\D+", tekst))
    hoofdletters = str(hoofdletters)
    for eenheid in hoofdletters:
        length_sleutel = len(sleutel)
        if eenheid != " ":
            sleutel_index = teller_sleutel
            if sleutel_index == length_sleutel:
                sleutel_index = 0
                teller_sleutel = 0
            if eenheid == ".":
                tekst_char = "."
            elif eenheid == "?":
                tekst_char = "?"
            elif eenheid == "!":
                tekst_char = "!"
            elif eenheid == ",":
                tekst_char = ","
            elif eenheid == "-":
                tekst_char = "-"
            elif eenheid == ":":
                tekst_char = ":"
            elif eenheid == "'":
                tekst_char = "'"
            else:
                tekst_positie = PositieAlphabet(eenheid)
                tekst_positie = int(tekst_positie)
                sleutel_eenheid = sleutel[sleutel_index]
                sleutel_positie = PositieAlphabet(sleutel_eenheid)
                sleutel_positie = int(sleutel_positie)
                tekst_en_sleutel_positie = tekst_positie + sleutel_positie
                tekst_eenheid = tekst_en_sleutel_positie % 26
                tekst_char = chr(65 + tekst_eenheid)
        else:
            sleutel_index = teller_sleutel
            if sleutel_index == length_sleutel:
                sleutel_index = 0
                teller_sleutel = 0
            tekst_char = " "

        geencrypteerd_bericht.append(tekst_char)
        teller_tekst = teller_tekst + 1
        teller_sleutel = teller_sleutel + 1
    geencrypteerd_bericht = ''.join(geencrypteerd_bericht)
    return geencrypteerd_bericht


def PositieAlphabet(tekst):
    alphabet_tekst = str(tekst)
    alphabet_letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    alphabet_tekst = alphabet_tekst.lower()
    nummers = [alphabet_letters[character] for character in alphabet_tekst if character in alphabet_letters]
    return ' '.join(nummers)


def decodeer(tekst, sleutel):
    geencrypteerd_bericht = []
    teller_tekst = 0
    teller_sleutel = 0
    tekst = str(tekst)
    sleutel = str(sleutel)
    hoofdletters = " ".join(re.findall("\D+", tekst))

    for eenheid in str(hoofdletters):
        length_s_key = len(sleutel)
        if eenheid != " ":
            sleutel_index = teller_sleutel
            if sleutel_index == length_s_key:
                sleutel_index = 0
                teller_sleutel = 0

            if eenheid == ".":
                tekst_char = "."
            elif eenheid == "?":
                tekst_char = "?"
            elif eenheid == "!":
                tekst_char = "!"
            elif eenheid == ",":
                tekst_char = ","
            elif eenheid == "-":
                tekst_char = "-"
            elif eenheid == ":":
                tekst_char = ":"
            elif eenheid == "'":
                tekst_char = "'"
            else:
                tekst_positie = PositieAlphabet(eenheid)
                tekst_positie = int(tekst_positie)
                sleutel_eenheid = sleutel[sleutel_index]
                sleutel_positie = PositieAlphabet(sleutel_eenheid)
                sleutel_positie = int(sleutel_positie)
                tekst_en_sleutel_positie = tekst_positie - sleutel_positie
                tekst_eenheid = tekst_en_sleutel_positie % 26
                tekst_char = chr(65 + tekst_eenheid)
        else:
            sleutel_index = teller_sleutel
            if sleutel_index == length_s_key:
                sleutel_index = 0
                teller_sleutel = 0
            tekst_char = " "
        geencrypteerd_bericht.append(tekst_char)
        teller_tekst = teller_tekst + 1
        teller_sleutel = teller_sleutel + 1
    geencrypteerd_bericht = ''.join(geencrypteerd_bericht)
    return geencrypteerd_bericht