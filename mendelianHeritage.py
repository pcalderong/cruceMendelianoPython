from utils import createGameteAux
from utils import sort

def createGamete(source):
   return createGameteAux(source)

def generateGametes(father, mother):
    gameteA = createGamete(father)
    gameteB = createGamete(mother)
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
            tmp = sort(x + y)  # sort by capital letter -> to match alelo
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

generateGametes("AaBbCc", "AaBbCc")