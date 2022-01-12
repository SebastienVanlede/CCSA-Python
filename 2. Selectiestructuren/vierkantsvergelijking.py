# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1437422481
import math
a = float(input()) 
b = float(input()) 
c = float(input())

discriminant = (b**2) - (4*a*c)

if discriminant < 0: 
  print("geen wortels")
if discriminant == 0:
    print("een wortel")
    print(-b / (2 * a))
if discriminant > 0:
    res1 = (-b + math.sqrt(discriminant))/ (2 * a)
    res2 = (-b - math.sqrt(discriminant))/ (2 * a)
    print("twee wortels")

    if res1 > res2: 
      print(str(res2) + "\n" + str(res1))
    else: 
      print(str(res1) + "\n" + str(res2))
