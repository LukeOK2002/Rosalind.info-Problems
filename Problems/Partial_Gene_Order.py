#Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
#Return: The total number of partial permutations P(n,k), modulo 1,000,000

import math

def partial_permutations(n, k):

    output = math.factorial(n) / math.factorial(n - k)
    output %= 1000000
    print(output)

partial_permutations(100, 9)