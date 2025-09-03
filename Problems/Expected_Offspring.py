#Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

#Variables here are a (AA-AA), b (AA-Aa), c, (AA-aa), d (Aa-Aa), e (Aa-aa)
#Follows the logic of a genetic cross question
def expected_offspring(a, b, c, d, e, f):
    aSum = a*2
    bSum = b*2
    cSum = c*2
    dSum = d*1.5
    eSum = e
    fSum = f*0

    total = aSum + bSum + cSum + dSum + eSum + fSum

    print(total)

expected_offspring(18957,18201,16451,19486,18632,16275)

