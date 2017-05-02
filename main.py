import sys
from utils import readFile
from mendelian import getPhenotypesFromFile
from mendelian import generateGTmatrix

def main(father, mother, characteristics, isFromFile):
    phenotypes = {}
    if isFromFile:
        text = readFile(characteristics)
        phenotypes = getPhenotypesFromFile(text)
    else:
        phenotypes = characteristics

    #Generate whole analysis
    if phenotypes != None:
        generateGTmatrix(father, mother, phenotypes)
