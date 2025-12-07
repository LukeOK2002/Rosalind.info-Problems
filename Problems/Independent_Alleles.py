'''A function which returns the factorial result of the
    input parameter, n'''
def factorial(n):
    prev_multiple = 1
    for i in range(n, 1, -1):
        prev_multiple = prev_multiple * i
    return prev_multiple

'''A function which returns the choose result of the
    input parameter, n, k'''
def choose(n, k):
    top_line = factorial(n)
    bottom_line = factorial(k)*factorial(n - k)
    return  int(top_line // bottom_line)

#Now implement a function to calculate odds on AaBb
#based on each generation's size

'''A function which returns the odds of a generation of
    number k containing at least N AaBb phenotypes'''
def odds(n, k):
    #Gives the number of individuals in each generation
    gen_n = 2**k

    #Applies the binomial formula, beginning with 'least' outcome
    #all the way up to complete AaBb phenotype population

    current_odds = 0
    for scenario in range(n, gen_n + 1, 1):
        independent_outcomes = (0.25**scenario)*(0.75**(gen_n - scenario))
        choosing_part = choose(gen_n, scenario)
        current_odds += (choosing_part*independent_outcomes)

    return(current_odds)

print(odds(6, 18))
