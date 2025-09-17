#Given: A protein string P of length at most 1000 aa.
#Return: The total weight of P. Consult the monoisotopic mass table.

def protein_mass(aa_string):
    amino_acid_weights = {
        "A": 71.037,  # Alanine
        "R": 156.101,  # Arginine
        "N": 114.043,  # Asparagine
        "D": 115.027,  # Aspartic acid
        "C": 103.009,  # Cysteine
        "E": 129.043,  # Glutamic acid
        "Q": 128.059,  # Glutamine
        "G": 57.021,  # Glycine
        "H": 137.059,  # Histidine
        "I": 113.084,  # Isoleucine
        "L": 113.084,  # Leucine
        "K": 128.095,  # Lysine
        "M": 131.040,  # Methionine
        "F": 147.068,  # Phenylalanine
        "P": 97.053,  # Proline
        "S": 87.032,  # Serine
        "T": 101.048,  # Threonine
        "W": 186.079,  # Tryptophan
        "Y": 163.063,  # Tyrosine
        "V": 99.068  # Valine
    }
    weight = 18.010 #Adding one water molecule at the end
    for amino_acid in aa_string:
        if amino_acid in amino_acid_weights:
            weight += amino_acid_weights[amino_acid]
    return weight

def main():
    with open(r"C:\Users\lisbo\Downloads\rosalind_prtm.txt") as input_data:
        aa_string = input_data.read().strip() #Removing /n character from parsed text file
    print(f'{protein_mass(aa_string):.3f}')

main()