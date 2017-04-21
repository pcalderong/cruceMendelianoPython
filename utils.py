# import numpy as np
def createGametes(caract):
    #["A", "a", "B", "b"]
    gametes = []
    for f in caract: # f = "A"
        for f2 in caract: # f2 = "B"
            if (f.upper() != f2.upper()): #f = "A" y f2 = "B" -> "B"
                gameteTemp = f + f2 # gameteTemp = "AB"
                if gameteTemp not in gametes and gameteTemp[::-1] not in gametes: # si no esta en la lista de ninguna forma (al derecho y al reves)
                    gametes.append(gameteTemp)
                    print gameteTemp
                    print
    return gametes



def generateGametes(value1, value2):
    gameteA = createGametes(value1)
    gameteB = createGametes(value2)
    totalCount = len(gameteA)*len(gameteB)
    matrix = createTable(gameteA, gameteB)
    listGenotypes = analyzeData(matrix)
    generateGenotypes(totalCount, listGenotypes)
    # generateGenotypes(listGenotypes)

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
            tmp = ''.join(sorted(x + y))  # sort by capital letter -> to match alelo
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
        print "Genotype for {} is {}/{} or {}%".format(v, listGenotypes[v], n, result)

generateGametes(["A", "a", "B", "b"], ["A", "a", "B", "b"])