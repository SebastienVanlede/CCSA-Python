# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1319193582
totaal = 0
blackjack = False

while not blackjack:
    kaart = int(input())
    totaal += kaart

    if kaart == 0:
        print(f"Voorzichtig gespeeld ({totaal})")
        blackjack = True
    if totaal > 21:
        print(f"Verbrand ({totaal})")
        blackjack = True
    if totaal == 21:
        print("Gewonnen!")
        blackjack = True
