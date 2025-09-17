#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


from Bio import SeqIO

def common_substring(input_string):
    #Using SeqIO to clean up the data, separate sequences into list items
    sequences = [str(record.seq) for record in SeqIO.parse(input_string, "fasta")]

    #The longest common sequence cannot be longer than the shortest sequence
    shortest = min(sequences, key=len)
    length = len(shortest)

    #Goes through longest possible substring lengths stepwise in -1 increments
    for longest_substring in range(length, 0, -1):
        #Goes through possible substrings
        for possible_substring in range(length - longest_substring + 1):
            candidate = shortest[possible_substring:possible_substring+longest_substring]
            if all(candidate in sequence for sequence in sequences):
                return candidate



def main():
    fasta_file = r"C:\Users\lisbo\Downloads\rosalind_lcsm.txt"
    print(common_substring(fasta_file))

main()