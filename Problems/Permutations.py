#A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.
#Given: a positive integer < 7
#Return: The total number of permutations of length n, followed by a list of all such permutations (in any order)

import random

def permutations(n):
    # Finding total possible permutations, probably more elegant notation for n!, but this is what I used
    total_permutations = 1
    for number in range(n):
        if number != 0:
            total_permutations += number*total_permutations

    permutations_list = []
    temp_permutation = []
    # Generating permutations until the maximum number of permutations has been achieved
    while len(permutations_list) < total_permutations:
            if len(temp_permutation) < n:
                for possible_number in range(n + 1):
                    possible_number = random.randint(1, n)
                    if possible_number not in temp_permutation:
                        temp_permutation.append(possible_number)
            else:
                # Ensuring randomly generated permutation not already present in list
                if temp_permutation not in permutations_list:
                    permutations_list.append(temp_permutation)
                    temp_permutation = []
                else:
                    # If it's not unique, generation begins from scratch
                    temp_permutation = []

    # Converting everything in the permutation list to achieve correct output
    s_permutation_list = [[str(number) for number in permutation] for permutation in permutations_list]


    # Creating a clean output to be compatible with Rosalind's grading criteria
    output_string = str(total_permutations) + '\n'
    for permutation in s_permutation_list:
        output_string += " ".join(permutation) + '\n'

    return output_string




def main():
    with open(r"C:\Users\lisbo\Downloads\permutations_output.txt", "w") as output:
        output.write(str(permutations(5)))

main()