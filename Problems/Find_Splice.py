#Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
#Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

from Bio import SeqIO

def findsplice(input_string):
    # Separating input file into two separate strings
    sequences = [str(record.seq) for record in SeqIO.parse(input_string, "fasta")]
    main_sequence = str(sequences[0])
    splice = str(sequences[1])

    # Having a separate index counter value that can be checked against len(splice)
    splice_index = 0

    # A list containing the index positions of the bases of the splice string in the order they appear
    index_position = []
    clean_string = ""

    for base_index, base in enumerate(main_sequence):
        #Checking if all the splice bases have been indexed yet
        if splice_index == len(splice):
            break
        # Checking if each base in the sequence corresponds to the bases in the splice string in the order they appear
        if base == splice[splice_index]:
            index_position.append(base_index + 1)
            splice_index += 1

    # The list is then converted to a string with the commas between the numbers removed
    for char in str(index_position):
        if char != ',':
            clean_string += char
        else:
            continue
    return(clean_string)




def main():
    fasta_file = r"C:\Users\lisbo\Downloads\rosalind_sseq.txt"
    print(findsplice(fasta_file))

main()