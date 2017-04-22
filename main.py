import sys
from utils import readFile
from mendelian import getPhenotypes
from mendelian import generateGTmatrix

def main():
    print sys.argv
    text = readFile(sys.argv[1])
    phenotypes = getPhenotypes(text)
    mendelianResult = generateGTmatrix(sys.argv[2], sys.argv[3], phenotypes)


main()