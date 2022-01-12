# https://dodona.ugent.be/nl/courses/399/series/3961/activities/1301141031
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input()) 
y4 = int(input())
eind = False

if x1 < x2 and x1 <= x3 and x1 <= x4 and (x2 > x3 or x2 > x4):
    if ((y1 > y3 or y1 > y4) and (y2 < y3 or y2 < y4)) or ((y2 > y3 or y2 > y4) and (y1 < y3 or y1 < y4)):
        eind = True
elif x2 < x1 and x2 <= x3 and x2 <= x4 and (x1 > x3 or x1 > x4):
    if ((y1 > y3 or y1 > y4) and (y2 < y3 or y2 < y4)) or ((y2 > y3 or y2 > y4) and (y1 < y3 or y1 < y4)):
        eind = True
if x1 > x2 and x1 > x3 and x1 > x4 and (x2 < x3 or x2 < x4):
    if ((y1 > y3 or y1 > y4) and (y2 < y3 or y2 < y4)) or ((y2 > y3 or y2 > y4) and (y1 < y3 or y1 < y4)):
        eind = True
elif x2 > x1 and x2 > x3 and x2 > x4 and (x1 < x3 or x1 < x4):
    if ((y1 > y3 or y1 > y4) and (y2 < y3 or y2 < y4)) or ((y2 > y3 or y2 > y4) and (y1 < y3 or y1 < y4)):
        eind = True
print("botsing" if eind else "geen botsing")
