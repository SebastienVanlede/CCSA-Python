# https://dodona.ugent.be/nl/courses/399/series/3962/activities/364433585
hoogte = int(input())
breedte = int(input())
x = y = 0
richtingX = richtingY = 1
done = False

while not done:
    x += richtingX
    y += richtingY
    if x == breedte:
        if y == 0:
            print(f'rechteronderpocket ({breedte}, 0)')
            done = True
            break
        elif y == hoogte:
            print(f'rechterbovenpocket ({breedte}, {hoogte})')
            done = True
            break
        else:
            print(f'rechterband ({breedte}, {y})')
            richtingX = -1
    elif x == 0:
        if y == 0:
            print(f'linkeronderpocket (0, 0)')
            done = True
            break
        elif y == hoogte:
            print(f'linkerbovenpocket (0, {hoogte})')
            done = True
            break
        else:
            print(f'linkerband (0, {y})')
            richtingX = 1

    if y == hoogte:
        if x == 0:
            print(f'linkerbovenpocket (0, {hoogte})')
            done = True
            break
        elif x == breedte:
            print(f'rechterbovenpocket ({breedte}, {hoogte})')
            done = True
            break
        else:
            print(f'bovenband ({x}, {hoogte})')
            richtingY = -1
    elif y == 0:
        if x == 0:
            print(f'linkeronderpocket (0, 0)')
            done = True
        elif x == breedte:
            print(f'rechteronderpocket ({breedte}, 0)')
            done = True
            break
        else:
            print(f'onderband ({x}, 0)')
            richtingY = 1
