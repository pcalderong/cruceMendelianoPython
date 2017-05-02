import sys
from utils import readFile
from mendelian import getPhenotypesFromFile
from mendelian import generateGTmatrix

def main(father, mother, characteristics):

    #Generate whole analysis
    if characteristics != None:
        return generateGTmatrix(father, mother, characteristics)
