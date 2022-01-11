# https://dodona.ugent.be/nl/courses/399/series/3960/activities/2071746302
aantalAppels = int(input())
aantalKisten = int(aantalAppels//20)
aantalPaletten = int(aantalKisten//35)

print(aantalPaletten)
print(aantalKisten - aantalPaletten * 35)
print(aantalAppels - aantalKisten * 20)

