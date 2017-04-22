#This sort is intended to have the genotypes displayed by letter, no matter if capital or not
def sort(string):
    tmp = ''.join(sorted(string, key=str.lower))
    newString = ""
    for i in range(len(tmp)):
        if (i< len(tmp) -1):
            if tmp[i] == tmp[i+1].upper():
                newString = newString + tmp[i] + tmp[i+1]
            elif tmp[i] == tmp[i+1].lower():
                newString = newString + tmp[i+1] + tmp[i]
    return newString

# Recursive call to generate gametes previous to the crossing process
def createGameteAux(source):
    crossList = []
    if len(source) == 1:
        return [source]
    elif len(source) == 2:
        if source[0] == source[1]:
            return createGameteAux(source[0])
        else:
            return [source[0],source[1]]
    else:
        crossList = crossingValues(source[:2], createGameteAux(source[2:]))
    return crossList

# Crossing process to make all the possible matches for each the father and the mother
def crossingValues(prefix, list):
    result = []
    for p in prefix:
        for l in list:
            gamete = p + l
            if gamete not in result:
                result.append(gamete)
    return result

# Reads the file - Only full paths
def readFile(fileName):
    test = open(fileName)
    text = [line.rstrip('\n') for line in open(fileName, 'r')]
    print test
    return test


