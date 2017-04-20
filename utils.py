# import numpy as np
def createGametes(caract):
    gametes = []
    for f in caract:
        for f2 in caract:
            if (f.upper() != f2.upper()):
                gameteTemp = f + f2
                if gameteTemp not in gametes and gameteTemp[::-1] not in gametes:
                    gametes.append(gameteTemp)
                    print gameteTemp
                    print
    return gametes

def generateGametes(values):
    gameteA = createGametes(values)
    gameteB = createGametes(values)
    totalCount = len(gameteA)*len(gameteB)
    matrix = createTable(gameteA, gameteB)
    listGenotypes = analyzeData(matrix)
    generateGenotypes(totalCount, listGenotypes)

def createTable(gameteA, gameteB):
    results=[]
    i = 0
    j = 0
    print "       ",
    for item in gameteB:
        print "  {}  ".format(item),
    print
    print "--------------------------------------"
    for x in gameteA:
        results.append([])
        print " {} | ".format(x),
        for y in gameteB:
            tmp = ''.join(sorted(x + y))
            results[i].append(tmp)
            print " {} ".format(tmp),
        i+=1
        print
    return results

def analyzeData(matrix):
    results = {}
    for row in matrix:
        for c in row:
            if c in results:
                results[c] += 1
            else:
                results[c] = 1
    return results


def generateGenotypes(n, listGenotypes):
    for v in listGenotypes:
        result = (listGenotypes[v] * 100) / n
        print "Genotype for {} is {} %".format(v, result)

generateGametes(["A", "a", "B", "b"])