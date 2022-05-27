# function for determining prime factors
def prime_factors(x):
    factors = list()
    divisor = 2
    while(divisor <= x)
        if(x % divisor) == 0:
            factors.append(divisor)
            x = x/divisor
        else
            divisor += 1
    return factors

