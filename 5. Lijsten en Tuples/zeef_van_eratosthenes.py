# https://dodona.ugent.be/nl/courses/399/series/7098/activities/197813628
def zeef(getal):
    getallen_lijst = []
    priem = [True for index in range(getal+1)]
    x = 2

    priem[0] = priem[1] = False
    while x**2 <= getal:
        for index in range(x ** 2, getal + 1, x):
            priem[index] = False
        x += 1

    for i in range(getal + 1):
        if priem[i]:
            getallen_lijst.append(i)
    return getallen_lijst