# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1647887074
speler1 = input()
speler2 = input()
gebaren = {
    "schaar": {"blad", "hagedis"},
    "blad": {"steen", "Spock"},
    "steen": {"hagedis", "schaar"},
    "hagedis": {"Spock", "blad"},
    "Spock": {"schaar", "steen"}
}
if speler2 in gebaren[speler1]:
    print("speler1 wint")
elif speler1 in gebaren[speler2]:
    print("speler2 wint")
else:
    print("gelijkspel")
