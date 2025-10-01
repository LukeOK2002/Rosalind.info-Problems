from Bio import SeqIO

def tt(input_string):
    sequences = [str(record.seq) for record in SeqIO.parse(input_string, "fasta")]

    purines = ["A", "G"]
    pyrimidines = ["T", "C"]

    transversion_count = 0
    transition_count = 0

    for base_index, base in enumerate(sequences[1]):
        if base == sequences[0][base_index]:
            continue
        else:
            if base in purines:
                if sequences[0][base_index] in pyrimidines:
                    transversion_count += 1
                else:
                    transition_count += 1
            if base in pyrimidines:
                if sequences[0][base_index] in purines:
                    transversion_count += 1
                else:
                    transition_count += 1

    ratio = transition_count / transversion_count
    return ratio


def main():
    fasta_file = r"C:\Users\lisbo\Downloads\rosalind_tran.txt"
    print(f'{tt(fasta_file):.11f}')

main()