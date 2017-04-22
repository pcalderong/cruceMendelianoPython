from utils import createGameteAux
from utils import sort

def createGamete(source):
   return createGameteAux(source)

def generateGTmatrix(father, mother, phenotypes):
    gameteA = createGamete(father)
    gameteB = createGamete(mother)
    totalCount = len(gameteA)*len(gameteB)
    matrix = createTable(gameteA, gameteB)
    listGenotypes = analyzeData(matrix)
    generateGenotypes(totalCount, listGenotypes, phenotypes)

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


def generateGenotypes(n, listGenotypes, phenotypes):
    for v in listGenotypes:
        result = (listGenotypes[v] * 100) / n
        print "Genotype for {} is {}/{} or {}%".format(v, listGenotypes[v], n, result)
        analizePhenotypes(v, phenotypes)

def analizePhenotypes(genotype, phenotype):
    last = ""
    result = ""
    for g in genotype:
        if last.upper() != g.upper():
            result += phenotype[g]
            result += " - "
            last = g
    print result + "\n"
    return result


def getPhenotypes(text):
    hashPhenotypes = {}
    for l in text:
        if "Phenotypes" not in l and "===" not in l:
            if "\n" in l[4:]:
                hashPhenotypes[l[:1]] = l[4:-1]
            else:
                hashPhenotypes[l[:1]] = l[4:]
    return hashPhenotypes