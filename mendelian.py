from utils import createGameteAux
from utils import sort

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
    generateGenotypes(totalCount, listGenotypes, phenotypes)

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
def generateGenotypes(n, listGenotypes, phenotypes):
    for v in listGenotypes:
        result = (listGenotypes[v] * 100) / n
        print "Genotype for {} is {}/{} or {}%".format(v, listGenotypes[v], n, result)
        analizePhenotypes(v, phenotypes)

# Generates Phenotypes analysis for EACH genotype
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

# Reads each line for the file, and sets a list with the corresponding characteristics.
# Handle as a hash table
def getPhenotypes(text):
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