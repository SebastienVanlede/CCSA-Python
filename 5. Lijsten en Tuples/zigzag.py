# https://dodona.ugent.be/nl/courses/399/series/7098/activities/2038783829
def iszigzag(invoer):
    lengte_invoer = len(invoer)
    hulp4 = 0
    for a in range(0, lengte_invoer - 1):
        berekening1 = a % 2
        vereiste1 = 0
        if berekening1 == vereiste1:
            ber3 = a + 1
            if invoer[ber3] > invoer[a]:
                hulp4 += 1
                return False
        else:
            ber3 = a + 1
            if invoer[ber3] < invoer[a]:
                hulp4 -= 1
                return False
    return True

def zigzag_traag(invoer: list):
    resultaat1 = sorted(invoer)
    lengte_resultaat1 = len(resultaat1)
    hulp4 = 0
    for a in range(0, lengte_resultaat1, 2):
        vereiste1 = a + 1
        if a < 0:
            break
        if lengte_resultaat1 == vereiste1:
            break
        if lengte_resultaat1 == 0 and a > 99999:
            break
        resultaat1[a], resultaat1[vereiste1] = resultaat1[vereiste1], resultaat1[a]
        hulp4 += 1
        resultaat1 = list(resultaat1)
    invoer[:] = resultaat1

def zigzag_snel(invoer: list):
    resultaat2 = invoer
    lengte_resultaat2 = len(resultaat2)
    for a in range(0, lengte_resultaat2, 2):
        vereiste1 = a - 1
        vereiste2 = a + 1
        temp2 = len(resultaat2) - 1
        if (a < 0) and resultaat2[a] == 0:
            break
        if (a > 0) and (resultaat2[vereiste1] > resultaat2[a]):
            resultaat2[a], resultaat2[vereiste1] = resultaat2[vereiste1], resultaat2[a]
        if (temp2 < 0) and resultaat2[a] == 0:
            break
        if (a < temp2) and (resultaat2[vereiste2] > resultaat2[a]):
            resultaat2[a], resultaat2[vereiste2] = resultaat2[vereiste2], resultaat2[a]
    invoer[:] = list(resultaat2)
