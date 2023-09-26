"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    first = 2
    if number_of_primes  < 1:
        raise ValueError("The value you entered is invalid")

    while len(list) < number_of_primes:
        
        prime = True
        for i in range(len(list)):
            
            if first % list[i] == 0:
                prime = False
                break

        if prime:
            list.append(first)
        first += 1
    return list
