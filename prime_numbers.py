import math

# is_prime function definition, parameter variable n must be a number

def is_prime(n):
    #Return false if <=1
    if n <= 1:
        return False
    #Return true if 2
    if n == 2:
        return True
    #Return false if even and not 2
    if n > 2 and n % 2 == 0:
        return False
    # Get closest square root
    root = math.floor(math.sqrt(n))

    # Odd number check
    # From 3 through closest square root, if evenly divisible by any odd numbers,
    # return not prime. Otherwise return True as root is not divisible by even or odd numbers.
    for odd_number in range(3, root+1, 2):

        if n % odd_number == 0:
            return False
    return True