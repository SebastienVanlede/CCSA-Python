# https://dodona.ugent.be/nl/courses/399/series/3962/activities/1047652305
import math
roodWit = int(input())
witBlauw = int(input())
groterKleiner = input()
blauw = wit = rood = 0

if groterKleiner == '<':
  if roodWit % 2 != 0:
      rood = math.floor(roodWit / 2)
  else:
      rood = math.ceil(roodWit / 2 - 1)
  wit = roodWit - rood
  blauw = witBlauw - wit

if groterKleiner == '>':
  if witBlauw > roodWit:
    if roodWit % 2 != 0:
        wit = math.floor(roodWit / 2)
    else:
        wit = math.ceil(roodWit / 2 - 1)
    rood = roodWit - wit
    blauw = witBlauw - wit
  else:
    if witBlauw % 2 != 0:
        wit = math.floor(witBlauw / 2)
    else:
        wit = math.ceil(witBlauw / 2)
    rood = roodWit - wit
    blauw = witBlauw - wit

print(blauw)
print(wit)
print(rood)
