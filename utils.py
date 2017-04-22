def sort(string):
    #This sort is intended to have the genotypes displayed by letter, no matter if capital or not
    tmp = ''.join(sorted(string, key=str.lower))
    newString = ""
    for i in range(len(tmp)):
        if (i< len(tmp) -1):
            if tmp[i] == tmp[i+1].upper():
                newString = newString + tmp[i] + tmp[i+1]
            elif tmp[i] == tmp[i+1].lower():
                newString = newString + tmp[i+1] + tmp[i]
    return newString

sort("BBaacc")

def createGameteAux(mother):
    crossList = []
    if len(mother) == 1:
        return [mother]
    elif len(mother) == 2:
        if mother[0] == mother[1]:
            return createGameteAux(mother[0])
        else:
            return [mother[0],mother[1]]
    else:
        crossList = crossingValues(mother[:2], createGameteAux(mother[2:]))
    return crossList

def crossingValues(prefix, list):
    result = []
    for p in prefix:
        for l in list:
            gamete = p + l
            if gamete not in result:
                result.append(gamete)
    return result


