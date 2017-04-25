import sys
from utils import readFile
from mendelian import getPhenotypes
from mendelian import generateGTmatrix
from mendelian import createMatrixPhenotype

def main():
    # Arguments from command line:
    #   sys.argv[1] => path/to/file
    #   sys.argv[2] => father
    #   sys.argv[3] => mother

    # Reads file from args
    text = readFile(sys.argv[1])

    # Creates phenotype list
    phenotypes = getPhenotypes(text)

    #Generate whole analysis
    if phenotypes != None:
        generateGTmatrix(sys.argv[2], sys.argv[3], phenotypes)



main()