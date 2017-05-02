from utils import createGameteAux
from utils import sort
# from utils import createPossibleGenAux


# Calls to Aux - Creates gametes for crossing process
def createGamete(source):
   return createGameteAux(source)

# Main method that handles all the mendelian crossing
def generateGTmatrix(father, mother, phenotypes):
    gameteA = createGamete(father)
    gameteB = createGamete(mother)
    totalCount = len(gameteA)*len(gameteB)
    matrix = createTable(gameteA, gameteB)
    listGenotypes = analyzeData(matrix)
    generateGenotypes(totalCount, listGenotypes)
    createMatrixPhenotype(listGenotypes, phenotypes, totalCount)
    return listGenotypes

# Creates mendelian table with results based on gameteA and gameteB
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
            tmp = sort(x + y)
            results[i].append(tmp)
            print " {} ".format(tmp),
        i+=1
        print
    return results

# Generate list for genotype analysis
def analyzeData(matrix):
    results = {}
    for row in matrix:
        for c in row:
            if c in results:
                results[c] += 1
            else:
                results[c] = 1
    return results

# Displays analysis for genotype
def generateGenotypes(n, listGenotypes):
    for v in listGenotypes:
        result = (listGenotypes[v] * 100) / n
        print "Genotype for {} is {}/{} or {}%".format(v, listGenotypes[v], n, result)

# Generates Phenotypes analysis for EACH genotype
def analizePhenotypes(genotype, qty, phenotype, totalCount):
    result = getSinglePhenotype(genotype, phenotype)
    print "{}/{} or {}% : {}\n".format(qty, totalCount,(qty*100)/totalCount, result)
    return result

def getSinglePhenotype(genotype, phenotype):
    last = ""
    result = ""
    for g in genotype:
        if last.upper() != g.upper():
            result += phenotype[g]
            result += " - "
            last = g
    return result
# Reads each line for the file, and sets a list with the corresponding characteristics.
# Handle as a hash table
def getPhenotypesFromFile(text):
    hashPhenotypes = {}
    for l in text:
        if "Phenotypes" not in l and "===" not in l:
            if l[:1] in hashPhenotypes:
                print "Phenotype {} is already on the file".format(l[:1])
                return None
            elif not l[:1].isalpha():
                print "Phenotype {} is not a letter".format(l[:1])
                return None
            elif len(l[4:]) > 3:
                if "\n" in l[4:]:
                    hashPhenotypes[l[:1]] = l[4:-1]
                else:
                    hashPhenotypes[l[:1]] = l[4:]
            else:
                print "Phenotype description for {} is empty".format(l[:1])
                return None
    return hashPhenotypes

def createMatrixPhenotype(genotype, phenotypesFeatures, totalCount):
    matrixPhenotype = {}
    for g in genotype:
        result = phenotypeExists(g, matrixPhenotype)
        if result:
            matrixPhenotype[result] += genotype[g]
        else:
            matrixPhenotype[g] = genotype[g]

    for p in matrixPhenotype:
        analizePhenotypes(p,matrixPhenotype[p], phenotypesFeatures, totalCount)
    return matrixPhenotype

def phenotypeExists(genotype, matrix):
    stringGen = ""
    i = 0
    for key in matrix:
        flag = True
        for g in range(len(genotype)):
            if genotype[g] != key[g] and isEven(i):
                flag = False
                break
            i+=1
        if flag:
            stringGen = key
    return stringGen

def createPossibleGen(list):
    combination = []
    for l in list:
        if len(combination) == 0:
            combination.append(l)
            combination.append(l.upper())
            combination.append(l.lower())
        else:
            newCombination = []
            for c in combination:
                newCombination.append(c + l)
                newCombination.append(c + l.upper())
                newCombination.append(c + l.lower())
            combination = newCombination
    print combination
    return combination

def isEven(value):
    if value % 2 == 0:
        return True
    else:
        return False
