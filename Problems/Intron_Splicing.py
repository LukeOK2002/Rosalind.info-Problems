#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

from Bio import SeqIO

def splicer(filepath):
    #Codon dictionary, used to match codons with their respective amino acids
    codon_table = {
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "AUG": "M",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

        "UAU": "Y", "UAC": "Y",
        "CAU": "H", "CAC": "H",
        "AAU": "N", "AAC": "N",
        "GAU": "D", "GAC": "D",

        "UAA": "Stop", "UAG": "Stop", "UGA": "Stop",
        "CAA": "Q", "CAG": "Q",
        "AAA": "K", "AAG": "K",
        "GAA": "E", "GAG": "E",

        "UGU": "C", "UGC": "C",
        "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
        "AGA": "R", "AGG": "R",
        "AGU": "S", "AGC": "S",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",

        "UGG": "W"
    }

    #Where the list of introns will be stored
    sequence_list = []
    #Once the introns have been removed, translated protein string will be stored here
    protein_string = ''

    #Using SeqIO to remove the FASTA headers/newline characters, outputting a sequence string
    for sequence in SeqIO.parse(filepath, 'fasta'):
        sequence_list.append(str(sequence.seq))

    main_sequence = sequence_list.pop(0)

    #Finding and removing introns
    for sequence in sequence_list:
        main_sequence = main_sequence.replace(sequence, "")

    #Transcription to RNA
    main_sequence = main_sequence.replace("T", "U")

    #Moving through the RNA sequence in steps of 3 in order to translate it
    for base in range(0, len(main_sequence), 3):
        codon = main_sequence[base:base+3]
        if codon in codon_table:
            protein_string += codon_table[codon]


    return protein_string

def main():
    fasta_file = r"C:\Users\lisbo\Downloads\rosalind_splc.txt"
    print(splicer(fasta_file))

main()

