genotype= "aabbCcDDee"
phenotype = ''

for allele in genotype:
    if not phenotype:
        phenotype += allele
    else:
        if allele.isupper() and phenotype [-1] != allele:
            phenotype += allele
        elif allele.islower() and genotype[genotype.index(allele)+1].islower() and phenotype[-1] != allele:
            phenotype += allele

print 'El fenotipo es', phenotype
