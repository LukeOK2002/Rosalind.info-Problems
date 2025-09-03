#Given: A protein string of length at most 1000 aa.
#Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

#Approached this by multiplying each amino acid by the number of total possible RNA constituents e.g if A, output = 3*4 and so on
def find_strings(AAcids):
    #Dictionary generated using ChatGPT,
    amino_acid_codons = {
        'A': 4,  # Alanine (GCU, GCC, GCA, GCG)
        'C': 2,  # Cysteine (UGU, UGC)
        'D': 2,  # Aspartic acid (GAU, GAC)
        'E': 2,  # Glutamic acid (GAA, GAG)
        'F': 2,  # Phenylalanine (UUU, UUC)
        'G': 4,  # Glycine (GGU, GGC, GGA, GGG)
        'H': 2,  # Histidine (CAU, CAC)
        'I': 3,  # Isoleucine (AUU, AUC, AUA)
        'K': 2,  # Lysine (AAA, AAG)
        'L': 6,  # Leucine (CUU, CUC, CUA, CUG, UUU, UUC)
        'M': 1,  # Methionine (AUG)
        'N': 2,  # Asparagine (AAU, AAC)
        'P': 4,  # Proline (CCU, CCC, CCA, CCG)
        'Q': 2,  # Glutamine (CAA, CAG)
        'R': 6,  # Arginine (CGU, CGC, CGA, CGG, AGA, AGG)
        'S': 6,  # Serine (UCU, UCC, UCA, UCG, AGU, AGC)
        'T': 4,  # Threonine (ACU, ACC, ACA, ACG)
        'V': 4,  # Valine (GUU, GUC, GUA, GUG)
        'W': 1,  # Tryptophan (UGG)
        'Y': 2,  # Tyrosine (UAU, UAC)
        'Z': 0,  # Undefined (no standard codons)
        '*': 3  # Stop codons (UAA, UAG, UGA)
    }

    #Starting with 3, as stop codon not declared in string but required biologically
    output = 3
    for residue in AAcids:
        output = amino_acid_codons[residue]*output

    #Submission portal requires answer to be moduloed by 1000000
    output = output%1000000


    return output

def main():
    with open(r"C:\Users\lisbo\Downloads\rosalind_mrna.txt") as input_data:
        AAcids = input_data.read().strip()
        output = find_strings(AAcids)
        print(output)

main()