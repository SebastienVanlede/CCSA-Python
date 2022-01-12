# https://dodona.ugent.be/nl/courses/399/series/7773/activities/522641350
def varkenswoord(word):
    medeklinkers = 0
    hoofdletters = False
    klinkers = ['a', 'e', 'i', 'o', 'u']
    varkenswoord = word

    if len(word) == 0:
        return word
    if word[0].isupper():
        hoofdletters = True
        for a in range(len(word)):
            if word[a].lower() in klinkers:
                if word[a].islower():
                    word = word[:1].lower() + word[1:]
                else:
                    break

    if word[0].lower() in klinkers:
        if word[0].lower() == 'u' and word[1].lower() == 'q':
            varkenswoord += 'ay'
        else:
            varkenswoord += "way"
    else:
        for i in range(len(word)):
            if word[i].lower() not in klinkers:
                medeklinkers += 1
            else:
                break
        if word[0].lower() == 'q' and word[1].lower() == 'u':
            medeklinkers = 2
        toevoegsel = word[:medeklinkers]
        varkenswoord = varkenswoord[medeklinkers:]
        varkenswoord += toevoegsel + 'ay'

    if hoofdletters:
        varkenswoord = varkenswoord[:1].upper() + varkenswoord[1:]
    return varkenswoord


def varkenslatijn(zin):
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    encrypted = ''
    words = zin.split(' ')

    for word in words:
        if '...' in word:
            encrypted += varkenswoord(word.split('...')[0]) + "..."
            encrypted += varkenswoord(word.split('...')[1]) + " "
        elif word[0] == '(':
            encrypted += "(" + varkenswoord(word[1:]) + " "
        elif '-' in word:
            encrypted += varkenswoord(word.split('-')[0]) + "-"
            encrypted += varkenswoord(word.split('-')[1]) + " "
        elif '\'' in word:
            encrypted += varkenswoord(word.split('\'')[0]) + "\'"
            encrypted += varkenswoord(word.split('\'')[1]) + " "
        elif word[0] == '(':
            encrypted += "(" + varkenswoord(word[1:]) + " "
        else:
            tek = ''
            temp = ''
            for i in range(len(word)):
                if word[i].lower() in alfabet:
                    temp += word[i]
                else:
                    tek += word[i]

            encrypted += varkenswoord(temp)
            encrypted += tek + ' '

    return encrypted.strip()